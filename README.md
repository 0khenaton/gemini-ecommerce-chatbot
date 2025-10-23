````markdown
# 🛒 E-Ticaret Destek Chatbot (Gemini RAG)

**[➡️ CANLI DEMOYU DENEMEK İÇİN TIKLAYIN ⬅️](https://gemini-ecommerce-chatbot-btjfkg2rttjkqefkjqykzt.streamlit.app)**

Bu proje, Google'ın en güncel `gemini-2.5-flash` modelini ve RAG (Retrieval-Augmented Generation) tekniğini kullanarak oluşturulmuş, Streamlit tabanlı bir e-ticaret destek asistanıdır.

Chatbot, `data` klasöründeki özel CSV veritabanını kullanarak "iade, sipariş, kargo" gibi spesifik sorulara bağlamdan cevap verir. Eğer cevap veritabanında yoksa, genel bilgisini kullanarak kullanıcıya yardımcı olmaya çalışır.

![Chatbot Arayüzü](https://hizliresim.com/bg6dzsr) 


## ✨ Temel Özellikler
* **RAG Entegrasyonu:** `data/ecommerce_faq_tr.csv` dosyasındaki Soru&Cevap verilerini kullanarak kullanıcıya özel cevaplar üretir.
* **Akıllı Yanıtlama:** Eğer cevap veritabanında bulunamazsa, Gemini'ın genel bilgisiyle sohbete devam eder.
* **Sohbet Geçmişi:** Streamlit'in `session_state` özelliği sayesinde tüm konuşma geçmişini hatırlar.
* **Basit Arayüz:** Streamlit ile hızlı ve temiz bir web arayüzü sunar.

## 🛠️ Kullanılan Teknolojiler
* **Dil Modeli:** Google Gemini 2.5 Flash
* **Kütüphane:** `google-generativeai`
* **Arayüz:** `streamlit`
* **RAG (Retrieval):** `scikit-learn` (TF-IDF & Cosine Similarity)
* **Veri İşleme:** `pandas`
* **API Anahtar Yönetimi:** `python-dotenv`

## 🚀 Kurulum ve Çalıştırma

Bu projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları sırasıyla izleyin.

### 1. Projeyi Klonlayın
```bash
git clone [https://github.com/0khenaton/gemini-ecommerce-chatbot.git](https://github.com/0khenaton/gemini-ecommerce-chatbot.git)
cd gemini-ecommerce-chatbot
````

### 2\. Sanal Ortam (venv) Oluşturun ve Aktif Edin

Proje bağımlılıklarını sisteminizden izole tutmak için bir sanal ortam (virtual environment) kullanmak en iyi yöntemdir.

Proje klasörünün içindeyken bir sanal ortam oluşturun:

```bash
python -m venv venv
```

Oluşturduğunuz sanal ortamı aktif hale getirin:

**Windows (CMD / PowerShell):**

```bash
.\venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

*(Terminalinizin başında `(venv)` ibaresini görmelisiniz.)*

### 3\. Gerekli Kütüphaneleri Yükleyin

Sanal ortamınız aktifken, `requirements.txt` dosyasındaki tüm Python kütüphanelerini yükleyin:

```bash
pip install -r requirements.txt
```

### 4\. API Anahtarınızı Ayarlayın

Projenin çalışması için bir Google API anahtarına ihtiyacınız var.

1.  `.env.example` dosyasını kopyalayıp `.env` adında yeni bir dosya oluşturun.
    *(Windows'ta `copy .env.example .env` / macOS/Linux'ta `cp .env.example .env`)*

2.  `.env` dosyasını bir metin editörü ile açın.

3.  `GOOGLE_API_KEY=` kısmına [Google AI Studio](https://aistudio.google.com/app/apikey)'dan aldığınız API anahtarınızı yapıştırın.

    ```env
    GOOGLE_API_KEY="AIzaSy...SİZİN_GERÇEK_ANAHTARINIZ"
    ```

### 5\. Uygulamayı Başlatın

Tüm kurulumlar tamamlandıktan ve sanal ortamınız hala aktifken, Streamlit uygulamasını çalıştırın:

```bash
streamlit run app.py
```

Uygulama otomatik olarak tarayıcınızda açılacaktır (genellikle `http://localhost:8501`).


## 📂 Proje Yapısı

```
.
├── 📄 .env.example       # API anahtarı için şablon
├── 📄 .gitignore          # Git'in hangi dosyaları görmezden geleceğini belirler
├── 📄 README.md           # Bu dosya
├── 📄 app.py              # Streamlit arayüzünü (UI) çalıştıran ana dosya
├── 📄 chatbot.py          # Gemini API ile konuşmayı ve RAG mantığını yöneten dosya
├── 📄 requirements.txt    # Gerekli Python kütüphaneleri
├── 📄 retriever.py        # TF-IDF kullanarak veritabanından ilgili bilgiyi çeken (retrieve) dosya
└── 📁 data/
    └── 📄 ecommerce_faq_tr.csv  # Chatbot'un cevapları için kullandığı Soru&Cevap veritabanı
```

```
```