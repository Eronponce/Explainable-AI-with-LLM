import requests
import json
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

def get_gemini_response(prompt_text, model="gemini-2.0-flash"):
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        return "Erro: Chave API da Gemini não configurada."

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={gemini_api_key}"
    headers = {"Content-Type": "application/json"}
    body = {"contents": [{"parts": [{"text": prompt_text}]}]}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(body))
        if response.status_code == 200:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        return f"Erro {response.status_code}: {response.text}"
    except Exception as e:
        return f"Erro na API Gemini: {e}"
