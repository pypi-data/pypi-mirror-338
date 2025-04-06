import os
import logging
import pickle
from typing import List, Optional, Union

import torch
from transformers import AutoModel, AutoTokenizer, BatchEncoding
import numpy as np

"""
Embedder module for llamaplastics_project.

This module provides functionality for the llamaplastics_project project.
"""


logger = logging.getLogger(__name__)

# Define a type hint for the output
EmbeddingTensor = Union[torch.Tensor, np.ndarray]


class LLMEmbedder:
    """Handles loading LLM models and extracting embeddings."""

    def __init__(
        self,
        model_name: str,
        embedding_layer: int = -1,
        device: str = "cpu",
        cache_dir: Optional[str] = None,
    ):
        """Initialize the LLM Embedder.

        Args:
            model_name: Name of the Hugging Face model (e.g., 'bert-base-uncased').
            embedding_layer: Index of the hidden layer to extract embeddings from.
                             -1 typically refers to the last hidden layer.
            device: Device to run the model on ('cpu', 'cuda', 'mps').
            cache_dir: Directory to cache embeddings.
        """
        self.model_name = model_name
        self.embedding_layer = embedding_layer
        self.device = device
        self.cache_dir = cache_dir
        self.embedding_cache = {}

        if self.cache_dir:
            os.makedirs(self.cache_dir, exist_ok=True)
            self._load_cache()

        logger.info(f"Loading tokenizer for {model_name}...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        logger.info(f"Loading model {model_name} onto {self.device}...")
        self.model = AutoModel.from_pretrained(model_name, output_hidden_states=True)
        self.model.to(self.device)
        self.model.eval()  # Set model to evaluation mode
        logger.info("LLM Embedder initialized.")

    def _get_cache_path(self) -> Optional[str]:
        """Get the path to the persistent cache file."""
        if not self.cache_dir:
            return None
        # Use a filename based on the model name to avoid conflicts
        safe_model_name = self.model_name.replace("/", "_")
        return os.path.join(self.cache_dir, f"embeddings_{safe_model_name}.pkl")

    def _load_cache(self) -> None:
        """Load embeddings from the cache file."""
        cache_path = self._get_cache_path()
        if cache_path and os.path.exists(cache_path):
            try:
                with open(cache_path, "rb") as f:
                    self.embedding_cache = pickle.load(f)
                logger.info(
                    f"Loaded {len(self.embedding_cache)} embeddings from cache: {cache_path}"
                )
            except (pickle.UnpicklingError, EOFError, FileNotFoundError) as e:
                logger.warning(
                    f"Could not load embedding cache from {cache_path}: {e}. Starting fresh."
                )
                self.embedding_cache = {}

    def _save_cache(self) -> None:
        """Save the current embedding cache to a file."""
        cache_path = self._get_cache_path()
        if cache_path:
            try:
                with open(cache_path, "wb") as f:
                    pickle.dump(self.embedding_cache, f)
                # logger.debug(f"Saved {len(self.embedding_cache)} embeddings to cache: {cache_path}")
            except (IOError, pickle.PicklingError) as e:
                logger.error(f"Could not save embedding cache to {cache_path}: {e}")

    @torch.no_grad()
    def get_embeddings(
        self,
        texts: List[str],
        batch_size: int = 16,
        use_cache: bool = True,
        return_numpy: bool = True,
    ) -> EmbeddingTensor:
        """Extract embeddings for a list of text prompts.

        Args:
            texts: List of text prompts.
            batch_size: Processing batch size.
            use_cache: Whether to use the embedding cache.
            return_numpy: Whether to return embeddings as NumPy arrays (default) or Torch tensors.

        Returns:
            A tensor (Torch or NumPy) containing the embeddings (n_texts, embedding_dim).
        """
        all_embeddings = []
        uncached_texts = []
        uncached_indices = []

        # Check cache first
        if use_cache:
            cached_embeddings = [None] * len(texts)
            for i, text in enumerate(texts):
                if text in self.embedding_cache:
                    cached_embeddings[i] = self.embedding_cache[text]
                else:
                    uncached_texts.append(text)
                    uncached_indices.append(i)
            if not uncached_texts:
                logger.debug("All embeddings found in cache.")
                # Ensure consistent return type
                embeddings_list = [
                    torch.tensor(emb) if isinstance(emb, np.ndarray) else emb
                    for emb in cached_embeddings
                ]
                final_embeddings = torch.stack(embeddings_list)
                return final_embeddings.numpy() if return_numpy else final_embeddings
            else:
                logger.info(
                    f"Processing {len(uncached_texts)} uncached texts ({len(texts) - len(uncached_texts)} cached)..."
                )
        else:
            uncached_texts = texts
            uncached_indices = list(range(len(texts)))
            cached_embeddings = [None] * len(texts)

        # Process uncached texts in batches
        computed_embeddings = {}
        for i in range(0, len(uncached_texts), batch_size):
            batch_texts = uncached_texts[i : i + batch_size]
            inputs: BatchEncoding = self.tokenizer(
                batch_texts,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=self.tokenizer.model_max_length,
            )
            inputs = inputs.to(self.device)

            outputs = self.model(**inputs)

            # Extract hidden states
            hidden_states = outputs.hidden_states

            # Get embeddings from the specified layer
            # Use pooling (e.g., mean pooling of the sequence) for a single vector per text
            layer_embeddings = hidden_states[self.embedding_layer]

            # Mean pooling (ignoring padding tokens)
            attention_mask = (
                inputs["attention_mask"].unsqueeze(-1).expand(layer_embeddings.size()).float()
            )
            sum_embeddings = torch.sum(layer_embeddings * attention_mask, 1)
            sum_mask = torch.clamp(attention_mask.sum(1), min=1e-9)
            pooled_embeddings = sum_embeddings / sum_mask

            # Move to CPU and store
            pooled_embeddings_cpu = pooled_embeddings.cpu()
            for j, text in enumerate(batch_texts):
                embedding = pooled_embeddings_cpu[j]
                computed_embeddings[text] = embedding
                if use_cache:
                    # Store as numpy array in cache for wider compatibility (e.g., pickling)
                    self.embedding_cache[text] = embedding.numpy()

        # Combine cached and computed embeddings in the original order
        final_embeddings_list = []
        computed_idx = 0
        for i in range(len(texts)):
            if cached_embeddings[i] is not None:
                # Ensure it's a tensor before stacking
                emb = cached_embeddings[i]
                final_embeddings_list.append(
                    torch.tensor(emb) if isinstance(emb, np.ndarray) else emb
                )
            else:
                # This index corresponds to an uncached text
                text = uncached_texts[computed_idx]
                final_embeddings_list.append(computed_embeddings[text])
                computed_idx += 1

        # Save cache if updated
        if use_cache and computed_embeddings:
            self._save_cache()

        # Stack final embeddings into a single tensor
        final_embeddings_tensor = torch.stack(final_embeddings_list)

        return final_embeddings_tensor.numpy() if return_numpy else final_embeddings_tensor
