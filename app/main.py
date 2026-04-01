from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import RAGSystem
from app.tools import ToolExecutor
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AtlasShop Assist")

app.mount("/front-end", StaticFiles(directory="front-end"), name="front-end")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rag = RAGSystem()
tools = ToolExecutor()

class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.get("/")
def serve_front():
    return FileResponse("front-end/index.html")

@app.post("/chat")
def chat(request: ChatRequest):
    message = request.message.lower()

    # detectar cliente
    for word in message.upper().split():
        if word.startswith("C"):
            cliente = tools.buscar_cliente(word)

            if cliente:
                return {
                    "answer": f"Cliente {cliente['nome_cliente']} está no plano {cliente['plano']} com status {cliente['status_cliente']}."
                }

    # detectar pedido
    for word in message.upper().split():
        if word.startswith("P"):
            pedido = tools.buscar_pedido(word)

            if not pedido:
                return {"answer": "Pedido não encontrado."}

            reembolsos = tools.buscar_reembolso_por_pedido(word)

            if reembolsos:
                return {
                    "answer": f"Pedido {word} tem {len(reembolsos)} reembolso(s). Status: {[r['status_reembolso'] for r in reembolsos]}"
                }

            return {
                "answer": f"Pedido {word} está com status {pedido['status_pedido']} e pagamento {pedido['status_pagamento']}."
            }

    # fallback documentos
    results = rag.search(request.message)

    if not results:
        return {"answer": "Não encontrei informações."}

    top_results = results[:2]
    context = "\n\n".join([r["snippet"] for r in top_results])

    return {
        "answer": f"Com base nos documentos:\n\n{context}",
        "sources": [r["filename"] for r in top_results]
    }