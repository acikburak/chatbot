
# 🧠 AIKonuş — Hafızalı Yapay Zeka Chatbotu

Bu proje, **AITool-s YouTube** sayfası için hazırlanan örnek bir yapay zeka proje demosudur.  
Kali Linux üzerinde çalışmak üzere tasarlanmış, **Ollama tabanlı hafızalı bir yapay zeka sohbet botudur**.

---

## 🎯 Proje Amacı

Kurumlar için geliştirilebilir ve genişletilebilir bir **örnek yapay zeka sohbet sistemi** sunmaktır.  
Gelecekte belge tabanlı bilgi yanıt sistemi de entegre edilecektir.

---

## 🚀 Özellikler

- ✅ Ollama destekli **Mistral LLM modeli**
- ✅ Kullanıcı dostu **Gradio arayüzü**
- ✅ Oturum bazlı hafıza (Session Memory)
- ⏳ Dokümana dayalı cevap verme (yakında)

---

## 🛠 Kurulum ve Başlatma

### 1. (Opsiyonel) GPU Desteği
```bash
sudo apt install nvidia-cuda-toolkit -y
```

### 2. Ollama Kurulumu
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 3. Ollama Servisini Başlat
```bash
ollama serve
```

### 4. Modeli İndir
```bash
ollama pull mistral
```

### 5. Test Et (Komut Satırından)
```bash
ollama run mistral "Merhaba! Kitaplarımı işlemeye hazır mısın?"
```

---

## 🎥 Eğitim ve Tanıtım Videosu

Projeyle ilgili detaylı anlatımı AITool-s YouTube kanalında izleyebilirsiniz:

🔗 [YouTube Kanalı: AITool-s](https://www.youtube.com/@aitool-s)

---

## 📁 Klasör Yapısı

```bash
aikonus/
├── app/
│   ├── document_loader.py
│   └── ollama_runner.py
├── documents/
│   ├── bilişim_hukuku.txt
│   ├── parola_politikasi_ozel.txt
│   └── siber_guvenlik.txt
├── main.py
└── requirements.txt
```

---

## 📄 Lisans

MIT Lisansı
