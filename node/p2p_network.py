class P2PNode:
    def __init__(self, node_name, port):
        self.node_name = node_name
        self.port = port

    def broadcast_model(self, params):
        # Gerçek bir libp2p entegrasyonu için JS subprocess veya REST call yapılmalı
        print(f"{self.node_name} model parametrelerini P2P ağına yayınladı: {params}")