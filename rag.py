from llama_index.core import VectorStoreIndex, Settings
from llama_index.vector_stores.milvus import MilvusVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.deepseek import DeepSeek


# Modelo de embedding 
Settings.embed_model = OpenAIEmbedding(
    model="text-embedding-3-small",
    api_base="http://localhost:8000/v1",
    api_key="fake-key"
)
# DeepSeek como LLM
MI_API_KEY = "TU_API_KEY_AQUI"
Settings.llm = DeepSeek(model="deepseek-chats", api_key=MI_API_KEY)

# Conectar Milvus
vector_store = MilvusVectorStore(
    uri="http://localhost:19530",
    collection_name="mis_docs",
    dim=1536
)

index = VectorStoreIndex.from_vector_store(
    vector_store=vector_store
)

query_engine = index.as_query_engine(
    similarity_top_k=3
)

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
