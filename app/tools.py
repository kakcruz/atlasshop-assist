import pandas as pd

class ToolExecutor:
    def __init__(self):
        self.clientes = pd.read_csv("data/clientes.csv")
        self.pedidos = pd.read_csv("data/pedidos.csv")
        self.reembolsos = pd.read_csv("data/reembolsos.csv")

    def buscar_cliente(self, cliente_id: str):
        result = self.clientes[self.clientes["cliente_id"] == cliente_id]

        if result.empty:
            return None

        return result.iloc[0].to_dict()

    def buscar_pedido(self, pedido_id: str):
        result = self.pedidos[self.pedidos["pedido_id"] == pedido_id]

        if result.empty:
            return None

        return result.iloc[0].to_dict()

    def buscar_reembolso_por_pedido(self, pedido_id: str):
        result = self.reembolsos[self.reembolsos["pedido_id"] == pedido_id]

        if result.empty:
            return None

        return result.to_dict(orient="records")