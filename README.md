# pdf-rag-vllm-deepseek
Corina Matheus

## Curso: Seminario de IA - Facultad de Ciencias, UCV. Mayo 2026
## Profesor: Dr. Julio Cesar Carrasquel

Sistema de preguntas y respuestas basado en RAG(Retrieval-Augmented Generation) que permite hacerle preguntas en lenguaje natural a un documento PDF y obtener respuestas basadas en su contenido

### Cambios respecto al enfoque original del seminario 
Dado que el entorno de desarrollo disponible contaba con recursos limitados y conexion a internet restringida, se realizaron los siguientes ajustes
1. Se elimino vLLM reemplazado por HuggingFaceEmbedding que descarga y ejecuta el modelo directamente en CPU sin necesidad de un servidor separado 
2. Se elimino Milvus con Docker reemplazado con Milvus Lite (uri="./milvus.db") que funciona como una base de datos local en un solo archivo sin necesidad de docker ni servicios externos
Estos cambios no alteran la logica del sistema RAG solo simplifican la infraestructura para correr en un entorno local con recursos limitados

### Tecnologia usada
- LLM: API de Deepseek
- Embeddings: HuggingFaceEmbedding BAAI/bge-small-en-v1.5
- Base de datos vetorial: Milvus Lite
- Framework RAG: LlamaIndex
### Requisitos
```
pip install llama-index-core
pip install llama-index-llms-deepseek
pip install llama-index-embeddings-huggingface
pip install llama-index-vector-stores-milvus
pip install sentence-transformers
pip install milvus-lite
```
### Como usarlo
1. Configurar API key de DeepSeek en rag.py:
   ```
   MY_API_KEY = "tu_api_key_aqui"
   ``
2. Ejecutar ingest
   ```
   python ingest.py
   ``
3. Ejecutar rag
   ```
   python rag.py
   ```
