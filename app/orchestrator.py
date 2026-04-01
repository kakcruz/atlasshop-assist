from app.rag import RAGSystem
from app.tools import ToolExecutor
from typing import Tuple, List

class Orchestrator:

    
    def __init__(self):
   
        self.rag = RAGSystem()
        self.tools = ToolExecutor()
    
    def process(self, user_message: str, conversation_context: List[dict]) -> Tuple[str, list]:
        intent = self._classify_intent(user_message)
        
        sources = []
        relevant_docs = []
        
        if intent["needs_knowledge"]:
            relevant_docs, doc_sources = self.rag.search(user_message)
            sources.extend(doc_sources)
        
        if intent["needs_tools"]:
            tool_results, tool_sources = self.tools.execute(
                user_message,
                intent["tool_type"]
            )
            sources.extend(tool_sources)
        else:
            tool_results = None

        response = self._generate_response(
            user_message,
            relevant_docs,
            tool_results,
            conversation_context,
            intent
        )
        
        return response, sources
    
    def _classify_intent(self, message: str) -> dict:
        message_lower = message.lower()
        
        intent = {
            "needs_knowledge": False,
            "needs_tools": False,
            "tool_type": None
        }
        
        knowledge_keywords = ["explique", "como", "o que é", "quem", "onde", "quando"]
        customer_keywords = ["cliente", "customer", "conta", "cadastro", "perfil"]
        order_keywords = ["pedido", "order", "compra", "venda", "histórico"]
        refund_keywords = ["reembolso", "refund", "devolução", "return", "cancel"]

        if any(kw in message_lower for kw in knowledge_keywords):
            intent["needs_knowledge"] = True

        if any(kw in message_lower for kw in customer_keywords):
            intent["needs_tools"] = True
            intent["tool_type"] = "customer"
        elif any(kw in message_lower for kw in order_keywords):
            intent["needs_tools"] = True
            intent["tool_type"] = "order"
        elif any(kw in message_lower for kw in refund_keywords):
            intent["needs_tools"] = True
            intent["tool_type"] = "refund"
        
        return intent
    
    def _generate_response(self, user_message: str, docs: list, 
                          tool_results: any, context: list, intent: dict) -> str:

        
        response_parts = []
        
        if tool_results:
            response_parts.append(f"Baseado nos dados consultados: {tool_results}")
        
        if docs:
            doc_summary = "\n".join([f"- {doc}" for doc in docs[:3]])
            response_parts.append(f"Documentação relevante:\n{doc_summary}")
        
        if not response_parts:
            response_parts.append(self._basic_response(user_message))
        
        return "\n\n".join(response_parts)
    
    def _basic_response(self, message: str) -> str:
        return (
            f"Entendi sua pergunta: '{message}'\n\n"
            "Para obter uma resposta mais completa, você pode:\n"
            "- Consultar dados de cliente\n"
            "- Verificar pedidos\n"
            "- Solicitar informações de reembolso\n"
            "\nComo posso ajudar especificamente?"
        )
