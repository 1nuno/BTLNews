import pickle
from sentence_transformers import SentenceTransformer
from database.config import get_session
from database.models import DreappDocumentText


# Load the embedding's model
model = SentenceTransformer('all-MiniLM-L6-v2')


def save_embeddings(embeddings_dict, file_name='document_embeddings.txt'):
    # Open and save the embeddings_dict on the file 'file_name':
    with open(file_name, 'wb') as f:
        pickle.dump(embeddings_dict, f)
    print("Dictionary of embeddings saved with success")


def generate_embeddings():
    session = get_session()

    documents = session.query(DreappDocumentText).all()

    # Dict to save the embeddings documents:
    embedding_dict = {}

    for doc in documents:
        embedding = model.encode(doc.text)  # Generate the embedding for the document text
        embedding_dict[doc.id] = embedding  # Save the embedding with the ID of the document

    # Save the embeddings dict to a file for posterior use:
    save_embeddings(embedding_dict)
