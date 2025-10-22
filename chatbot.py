import os
import google.generativeai as genai
from dotenv import load_dotenv
from retriever import retrieve

load_dotenv()

try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY bulunamadı. Lütfen .env dosyanızı kontrol edin.")
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(model_name="gemini-2.5-flash") 

except Exception as e:
    print(f"API Yapılandırma Hatası: {e}")
    model = None 


def ask_bot(query):
    if model is None:
        return "Hata: API modeli başlatılamadı. Lütfen terminal loglarını kontrol edin."

    try:
        context_docs = retrieve(query)
        context_text = "\n".join(context_docs)

        prompt = f"""Sen bir e-ticaret destek asistanısın. 
Kullanıcının sorusunu cevaplamak için öncelikle aşağıdaki bağlamı kullanmaya çalış.
Eğer bağlamda yeterli bilgi yoksa veya bağlam boşsa, genel bilgini kullanarak yardımcı olmaya çalış.

Bağlam:
{context_text}

Soru: {query}

Cevap:
"""

        response = model.generate_content(prompt)
        
        return response.text

    except Exception as e:
        print(f"Gemini API Hatası: {e}")
        return f"Bir hata oluştu. Lütfen daha sonra tekrar deneyin. (Detay: {e})"