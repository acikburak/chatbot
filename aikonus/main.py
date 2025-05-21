import gradio as gr
from app.ollama_runner import call_ollama
from app.document_loader import load_documents

# Belgeleri oku ve sistem mesajı olarak belleğe ekle
document_knowledge = load_documents()

# 🧠 Konuşma geçmişini tutan liste (başta sistem mesajı ile başlıyor)
conversation_transcript = [
    {"role": "system", "content": f"Aşağıdaki belgeler dışına çıkmadan cevap ver:\n{document_knowledge}"}
]

def ai_chatbot(user_input, history):
    global conversation_transcript

    # Kullanıcıdan gelen mesajı hafızaya ekle
    conversation_transcript.append({"role": "user", "content": user_input})

    # Ollama'dan cevap al
    response = call_ollama(conversation_transcript)

    # AI cevabını da ekle
    conversation_transcript.append({"role": "assistant", "content": response})

    return response

# 🎛️ Gradio arayüzü
demo = gr.ChatInterface(fn=ai_chatbot, title="🧐 AIKonuş — Hafızalı Sohbet Botu")
demo.launch()
