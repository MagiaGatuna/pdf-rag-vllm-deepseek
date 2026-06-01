# pdf-rag-vllm-deepseek
Corina Matheus

## Curso: Seminario de IA - Facultad de Ciencias, UCV. Mayo 2026
## Profesor: Dr. Julio Cesar Carrasquel

Sistema de preguntas y respuestas basado en RAG(Retrieval-Augmented Generation) que permite hacerle preguntas en lenguaje natural a un documento PDF y obtener respuestas basadas en su contenido

### Tecnologia usada
LLM: API de Deepseek
Embeddings: HuggingFaceEmbedding BAAI/bge-small-en-v1.5
Base de datos vetorial: Milvus
Framework RAG: LlamaIndex
### Requisitos
```
pip install llama-index-core
pip install llama-index-llms-deepseek
pip install llama-index-vector-stores-milvus
pip install llama-index-embeddings-openai
pip install pymilvus
### Como usarlo
1. Lanzar servidor vLLM en puerto 8000
2. Lanzar Milvus en puerto 19530
3. Correr: python ingest.py
4. Correr: python rag.py
