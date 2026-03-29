from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


def ingest(pdf_path):
    loader = PyPDFLoader(pdf_path)

    # load documents
    try:
        docs = loader.load()
    except Exception as e:
        print(f"Can't load PDF: {e}")
        return

    # break document into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    all_splits = text_splitter.split_documents(docs)

    # define embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # initialize vector DB
    vector_store = Chroma(
        collection_name="pdf_collection",
        embedding_function=embeddings,
        persist_directory="./chroma_db",
    )

    # saves chunks into vector DB
    vector_store.reset_collection()
    vector_store.add_documents(all_splits)

    print(f"Stored {len(all_splits)} chunks in ChromaDB")
