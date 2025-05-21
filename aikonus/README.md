
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
├──  main.py 
├── app/
│   └── ollama_runner.py            # Gradio + Ollama entegrasyonu
│   └── document_loader.py  ✅
├── documents/             # Kullanılacak dökümanlar buraya eklenecek
│   └── parola_politikasi_ozel.txt #Temsilidir.
│   └── bilişim_hukuku.txt #temsilidir.
│   └── siber_guvenlik.txt #temsilidir.

├── requirements.txt       # Gerekli Python paketleri
└── README.md              # Proje açıklaması
```

---

## 📄 Lisans

MIT Lisansı
