from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
from llama_index.vector_stores.milvus import MilvusVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Cargar PDF
documents = SimpleDirectoryReader(input_files = ["mi_documento.pdf"]).load_data()

# Chunking
splitter = SentenceSplitter(chunk_size=512, chunk_overlap=64)

# Modelo de embedding local
embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Milvus Lite: guardar archivo localmente
vector_store = MilvusVectorStore(uri="./milvus.db", collection_name="mis_docs", dim=384)

# Crear pipeline de ingestión
pipeline = IngestionPipeline(trasnformations=[splitter, embedding_model], vector_store=vector_store)
pipeline.run(documents=documents)
print("Ingestión completada con exito! :)")