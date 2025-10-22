import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# CSV dosyasını oku
df = pd.read_csv("data/ecommerce_faq_tr.csv")

# TF-IDF vektörlemesi
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['question'].astype(str))

def retrieve(query, top_k=3):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = scores.argsort()[-top_k:][::-1]
    return [df.iloc[i]['answer'] for i in top_indices]
