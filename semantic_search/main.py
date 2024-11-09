from database.config import get_session
from database.models import DreappDocument, DreappDocumentText, DreappDocumentConnectsTo

from embeddings.generate_embeddings import generate_embeddings
from embeddings.search import show_results

def test_connection():
    session = get_session()

    # Testing connection: Access to the database
    try:
        documents = session.query(DreappDocument).limit(5).all()
        if documents:
            print("Connection successfully. Some Documents found.")
            for doc in documents:
                print(f"ID: {doc.id}, Type: {doc.doc_type}, emiting_body: {doc.emiting_body}")
        else:
            print("Connection successfully. No documents found.")
    except Exception as e:
        print(f"Error on the connection: {e}")

    finally:
        # Ending session:
        session.close()


if __name__ == "__main__":
    # Testing the database connection:
    print("Testing connection with the Database...")
    test_connection()

    # Generate embeddings. Run just one time to create and save the files with the embeddings:
    generate_embeddings()

    test_search_query = "Presidente da republica"
    show_results(test_search_query)





