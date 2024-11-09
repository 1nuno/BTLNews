import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from database.config import get_session
from database.models import DreappDocumentText

# Load the embedding's model
model = SentenceTransformer('all-MiniLM-L6-v2')


def search_semantic_documents(query, top_k=5, file_name='document_embeddings.txt'):
    # Load the embeddings of the documents:
    with open(file_name, 'rb') as f:
        embeddings_dict = pickle.load(f)

    # Generating the embedding of the user search (query):
    query_embedding = model.encode(query)

    # Calc the similarity between the user search embedding and each embedding of document:
    similarities = []
    for doc_id, doc_embedding in embeddings_dict.items():
        similarity = cosine_similarity([query_embedding], [doc_embedding])[0][0]
        similarities.append(similarity)


    # Ordering the similarities by descendent order:
    similarities = sorted(similarities, key=lambda x: x[1], reverse=True)

    # return the top_k documents:
    return similarities[:top_k]

def show_results(query, top_k=5):
    # Picking the top_k documents more similarity with the user search (query):
    results = search_semantic_documents(query, top_k)

    # Show them:
    session = get_session()
    for doc_id, score in results:
        # Selecting text document from doc_id:
        document = session.query(DreappDocumentText).get(doc_id)
        print(f"ID document: {doc_id}   |   Similarity: {score:.4f}")
        print(f"Document Text: {document.text}")


