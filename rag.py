
import numpy as np
from sentence_transformers import SentenceTransformer


# ============================================
# LOAD EMBEDDING MODEL
# ============================================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# ============================================
# SPLIT TEXT INTO CHUNKS
# ============================================

def create_chunks(text, chunk_size=500):

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):

        chunk = " ".join(
            words[i:i + chunk_size]
        )

        if chunk.strip():
            chunks.append(chunk)

    return chunks


# ============================================
# CREATE EMBEDDINGS
# ============================================

def create_embeddings(chunks):

    embeddings = embedding_model.encode(
        chunks,
        convert_to_numpy=True
    )

    return embeddings.astype("float32")


# ============================================
# CREATE VECTOR DATABASE
# ============================================

def create_faiss_index(embeddings):

    # We keep the same function name so app.py
    # does not need to change.
    #
    # Instead of FAISS, we store the embeddings
    # as a NumPy matrix.

    return embeddings


# ============================================
# RETRIEVE RELEVANT CHUNKS
# ============================================

def retrieve_chunks(
    query,
    chunks,
    index,
    top_k=3
):

    # Create query embedding
    query_embedding = embedding_model.encode(
        [query],
        convert_to_numpy=True
    )[0].astype("float32")


    # ----------------------------------------
    # Calculate cosine similarity
    # ----------------------------------------

    query_norm = np.linalg.norm(
        query_embedding
    )

    document_norms = np.linalg.norm(
        index,
        axis=1
    )

    # Prevent division by zero
    query_norm = max(query_norm, 1e-10)

    document_norms = np.maximum(
        document_norms,
        1e-10
    )

    similarities = np.dot(
        index,
        query_embedding
    ) / (
        document_norms * query_norm
    )


    # ----------------------------------------
    # Get Top-K results
    # ----------------------------------------

    top_k = min(
        top_k,
        len(chunks)
    )

    top_indices = np.argsort(
        similarities
    )[-top_k:][::-1]


    # ----------------------------------------
    # Return relevant chunks
    # ----------------------------------------

    retrieved_chunks = []

    for idx in top_indices:

        retrieved_chunks.append(
            chunks[idx]
        )

    return retrieved_chunks

