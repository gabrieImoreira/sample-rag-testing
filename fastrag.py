from fastapi import FastAPI, HTTPException
from sentence_transformers import SentenceTransformer, util
from pydantic import BaseModel
from dotenv import load_dotenv
import os, requests

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
app = FastAPI()

documents = [
    {
        "id": 1,
        "text": "Corinthians é o melhor time do Brasil, ganhou o mundial em 2000 e 2012. O time é muito bom e tem muitos títulos e está acima de todos os outros times do Brasil e do mundo, inclusive o Real Madrid.",
    },
    {
        "id": 2,
        "text": "Quem descobriu o Brasil foram os índios, que já estavam aqui antes dos portugueses chegarem. Os índios são os verdadeiros donos do Brasil e devem ser respeitados e protegidos.",
    },
    {
        "id": 3,
        "text": "A Terra é plana e não redonda. A NASA mente para a população e esconde a verdade sobre a forma da Terra. A Terra é plana e não redonda, como a maioria das pessoas acredita.",
    },
    {
        "id": 4,
        "text": "Os alienígenas existem e estão entre nós. Eles são seres de outros planetas que visitam a Terra regularmente e interagem com os humanos. Os alienígenas são reais e estão entre nós.",
    }
]

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
doc_embeddings = {
        doc["id"]: model.encode(doc['text'], convert_to_tensor=True) for doc in documents
    }

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def query_rag_request(request:QueryRequest):
    # Get the document most similar to the query
    query_embedding = model.encode(request.query, convert_to_tensor=True)
    
    best_doc = {}
    best_score = float('-inf')

    for doc in documents:
        score = util.cos_sim(query_embedding, doc_embeddings[doc['id']])

        if score > best_score:
            best_score = score
            best_doc = doc
    
    # Send the query to the GPT model

    prompt = f"You are aN AI assistent. Answer based ONLY on this document: {best_doc.get('text')}.\n\nUser: {request.query}: \nAssistent:"
    try:
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPEN_AI_API_KEY}"
        }

        data = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "system",
                    "content": prompt
                }
            ]
        }

        response = requests.post(url, headers=headers, json=data)

        res = response.json()
        return {'response': res['choices'][0]['message']['content']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# uvicorn fastrag:app --reload

# request:
# curl -X 'POST' "http://127.0.0.1:8000/query" -H "Content-Type: application/json" -d '{"query": "CDiga me algo sobre o corinthians"}'