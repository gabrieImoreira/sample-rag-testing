# FastRAG API

## English Version

### Overview
FastRAG is a simple API built with FastAPI that retrieves relevant information from a predefined document database and generates AI-based responses using OpenAI's GPT model.

### Features
- Uses `SentenceTransformer` for semantic similarity search.
- Fetches the most relevant document based on cosine similarity.
- Calls OpenAI's API (`GPT-4o-mini`) to generate a response based on the retrieved document.

### Requirements
- Python 3.8+
- OpenAI API key

### Installation
```sh
pip install fastapi uvicorn sentence-transformers requests python-dotenv
```

### Usage
1. Create a `.env` file and add your OpenAI API key:
   ```sh
   OPEN_AI_API_KEY=your_openai_api_key
   ```
2. Run the API:
   ```sh
   uvicorn fastrag:app --reload
   ```
3. Send a request:
   ```sh
   curl -X 'POST' "http://127.0.0.1:8000/query" -H "Content-Type: application/json" -d '{"query": "Tell me something about Corinthians"}'
   ```

---

## Versão em Português

### Visão Geral
FastRAG é uma API simples construída com FastAPI que recupera informações relevantes de um banco de documentos predefinido e gera respostas baseadas em IA usando o modelo GPT da OpenAI.

### Funcionalidades
- Utiliza `SentenceTransformer` para busca semântica por similaridade.
- Obtém o documento mais relevante com base na similaridade do cosseno.
- Chama a API da OpenAI (`GPT-4o-mini`) para gerar uma resposta baseada no documento recuperado.

### Requisitos
- Python 3.8+
- Chave da API da OpenAI

### Instalação
```sh
pip install fastapi uvicorn sentence-transformers requests python-dotenv
```

### Uso
1. Crie um arquivo `.env` e adicione sua chave da API da OpenAI:
   ```sh
   OPEN_AI_API_KEY=sua_chave_openai
   ```
2. Execute a API:
   ```sh
   uvicorn fastrag:app --reload
   ```
3. Envie uma requisição:
   ```sh
   curl -X 'POST' "http://127.0.0.1:8000/query" -H "Content-Type: application/json" -d '{"query": "Diga-me algo sobre o Corinthians"}'
   ```

