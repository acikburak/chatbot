
# 🧠 AIKonuş — Hafızalı Yapay Zeka Chatbotu

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
### 6. projeyi indir
🔗 GitHub Bağlantısı:
```bash
git clone https://github.com/acikburak/chatbot.git
```
## 7. Aşağıdaki kodları çalıtırarak kurulumu tamamla
```bash
cd chatbot/aikonus
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```
## Çalıştırmak için 
```bash
cd chatbot/aikonus
source venv/bin/activate
python3 main.py
## gelen url adresini aç.
```




---

## 🎥 Eğitim ve Tanıtım Videosu

Projeyle ilgili detaylı anlatımı AITool-s YouTube kanalında izleyebilirsiniz:
https://www.youtube.com/watch?v=U7Q0ScGtr1I Ollama ve mistal modeli kurulmalıdır. video'dan takip ederek indirebilirsiniz.
Yazılım sırasındaki video kaydı.
https://www.youtube.com/watch?v=O0hjRj15QRc 
🔗 [YouTube Kanalı: AITool-s](https://www.youtube.com/@aitool-s)
Topluluk Sayafası : https://www.bilgiveteknoloji.com/forum/public/d/95-aikonus-hafizali-yapay-zeka-chatbotu
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
