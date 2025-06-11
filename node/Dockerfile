FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# nodejs ve orbitdb için
RUN apt-get update && apt-get install -y curl nodejs npm
RUN npm install -g pm2

# OrbitDB ve libp2p için ilgili js scriptleri yükle
RUN npm install orbit-db ipfs libp2p

CMD ["python", "app.py"]