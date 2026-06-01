from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
from llama_index.vector_stores.milvus import MilvusVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding

# Cargar PDF
documents = SimpleDirectoryReader(
    input_files=["mi_documento.pdf"]
).load_data()

# Chunking
splitter = SentenceSplitter(chunk_size=512, chunk_overlap=64)

# Modelo de embedding local
embedding_model = OpenAIEmbedding(
    model="text-embedding-3-small",
    api_base="http://localhost:8000/v1",
    api_key="fake-key"
)

# Milvus
vector_store = MilvusVectorStore(
    uri="http://localhost:19530",
    collection_name="mis_docs",
    dim=1536
)

# Crear pipeline de ingestión
pipeline = IngestionPipeline(
    transformations=[splitter, embedding_model],
    vector_store=vector_store
)
print("Ingestión completada con exito! :D")