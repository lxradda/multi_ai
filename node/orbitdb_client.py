class OrbitDBClient:
    def __init__(self, node_name, port):
        self.node_name = node_name
        self.port = port

    def save_model(self, params):
        # Gerçek bir OrbitDB kaydı için Node.js subprocess veya REST call yapılmalı
        print(f"{self.node_name} OrbitDB'ye model kaydı yaptı: {params}")

    def fetch_latest_model(self):
        # Gerçek bir OrbitDB'den veri çekmek için buraya ekleme yapılacak
        return f"{self.node_name} OrbitDB'den model çekti (örnek veri)"