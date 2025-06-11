"""
Sistemin giriş noktası.
Buradan madencilik istemcisi, model güncelleyici ve blockchain arayüzü başlatılır.
"""

from mining_client import MiningClient

if __name__ == "__main__":
    miner = MiningClient()
    miner.run()