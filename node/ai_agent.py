class AIAgent:
    def __init__(self, node_name):
        self.node_name = node_name
        self.model_param = 0  # Basit bir parametre, örnek için

    def train(self, data):
        # Basitçe veri uzunluğunu parametreye ekle (örnek amaçlı)
        self.model_param += len(data)

    def get_model_params(self):
        return f"Node: {self.node_name}, Param: {self.model_param}"