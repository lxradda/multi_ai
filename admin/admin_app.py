import gradio as gr
import requests

NODE_PORTS = [8001, 8002, 8003]

def get_node_statuses():
    status = []
    for port in NODE_PORTS:
        try:
            r = requests.get(f"http://node{NODE_PORTS.index(port)+1}:8000/")
            status.append(f"Node{NODE_PORTS.index(port)+1}: ONLINE")
        except:
            status.append(f"Node{NODE_PORTS.index(port)+1}: OFFLINE")
    return "\n".join(status)

with gr.Blocks() as admin_panel:
    gr.Markdown("# Admin Panel - Node Durumları")
    status_btn = gr.Button("Node Durumunu Kontrol Et")
    status_output = gr.Textbox(label="Node Durumları")
    status_btn.click(fn=get_node_statuses, inputs=None, outputs=status_output)

if __name__ == "__main__":
    admin_panel.launch(server_name="0.0.0.0", server_port=8000)
    