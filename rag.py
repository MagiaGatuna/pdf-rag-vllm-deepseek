from llama_index.core import VectorStoreIndex, Settings
from llama_index.vector_stores.milvus import MilvusVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.deepseek import DeepSeek

# Modelo de embedding 
Settings.embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# DeepSeek como LLM
MI_API_KEY = ""
Settings.llm = DeepSeek(model=deepseek-chats, api_key=MI_API_KEY)

# Conectar Milvus Lite
vector_store = MilvusVectorStore(uri="./milvus.db", collection_name="mis_docs", dim=384)

index = VectorStoreIndex.from_vector_store(vector_store=vector_store)

query_engine = index.as_query_engine(similarity_top_k=3)

# Loop interactivo
print("\nBienvenido! Sistema RAG Activo! Haz tus preguntas sobre el documento.\n")
print("Escribe 'EXIT' para terminar la sesión.\n")

while True:
    pregunta = input("Escribe tu pregunta: ")
    if pregunta.strip().upper() == "EXIT":
        print("¡Hasta luego! :)")
        break
    if pregunta.strip() == "":
        print("Por favor, ingresa una pregunta.")
        continue

    print("Buscando en la base de datos...")
    try:
        respuesta = query_engine.query(pregunta)
        print(f"\nRespuesta:\n{respuesta}\n")
        print("-" * 50)
    except Exception as e:
        print(f"\nError al procesar la pregunta: {e}")
        continue
