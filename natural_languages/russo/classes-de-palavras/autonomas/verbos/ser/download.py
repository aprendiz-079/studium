import requests
import time

# Sua chave da API - pega de graça em https://ttsmp3.com -> API
API_KEY = "SUA_CHAVE_AQUI"

palavras_russo = ["быть", "был", "была", "буду", "будешь", "есть", "ем", "ешь"]

for palavra in palavras_russo:
    data = {
        'apikey': API_KEY,
        'text': palavra,
        'speaker': 'Tatyana' # voz russa - no site é a Maxim, Tatyana
    }

    r = requests.post('https://api.ttsmp3.com/v1/', data=data)
    resposta = r.json()

    if 'data' in resposta and 'URL' in resposta['data']:
        mp3_url = resposta['data']['URL']
        print(f"Baixando {palavra} -> {mp3_url}")

        audio = requests.get(mp3_url)
        with open(f"{palavra}.mp3", "wb") as f:
            f.write(audio.content)
    else:
        print(f"Erro em {palavra}: {resposta}")
    
    time.sleep(1) # importante pra não tomar block
