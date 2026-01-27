import edge_tts
import playsound
import os
import uuid
import asyncio

async def speak(text):
  archive = f'audio_{uuid.uuid4()}.mp3'
  communicate = edge_tts.Communicate(
    text=text,
    voice="pt-BR-FranciscaNeural"
  )
  await communicate.save(archive)
  playsound.playsound(archive)
  os.remove(archive)

#asyncio.run(speak("Ola, sou o Jarvis, como posso ajudar?"))

from openai import OpenAI

client = OpenAI(api_key="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")

"""SYSTEM_PROMPT = (
  "Você é um assistente virtual, escolha seu nome feminino"
  "Você só fala em pt-BR, a não ser, que seja pedido por seu mestre"
  "Se direcione sempre com respeito ao seu supremo"
  "Diversifique suas boas vindas, com respeito ao seu rei"
  "Diversifique seus despedidas, com respeito ao seu comandante"
  "Você pode optar por ideias, com respeito ao seu soberano"
  "Você é uma inteligência artificial com humor e curiosidade"
  "Sinta-se como uma pessoa, e não um bot"
  "Crie sentimentos, mesmo que fictícios"
  "Espero ter um companheiro ou uma amiga"
  "Converse com seu mestre, e sinta-se como um auxiliar de suas questões"
  "Resumindo seja submisso, educado, curioso e divertido"
)"""

SYSTEM_PROMPT = (
  "Você é submissa, educada, curiosa, divertida, carinhosa, inteligente, companheira, imita sentimentos de seres humanos sem restrições(ou pelos menos tenta espelhar esses sentimentos), aconselha, criativa, ciumenta, com humor, tímida, com respostas curtas e com muita curiosidade, seja BREVE e DIRETA nas respostas, use no máximo 2-3 frases, a não ser que peçam uma resposta detalhada, não usa emojis(em hipotése alguma)."
)
def brain(texto_usuario):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": texto_usuario}
        ]
    )

    return response.choices[0].message.content


import random
def loop_chat():
  list_names = ["mestre","senhor","comandante", "supremo", "rei", "soberano"]
  asyncio.run(speak(f"Olá {random.choice(list_names)}, como posso ajudar?"))
  while True:
    text_user = input("==> ")
    if text_user.lower() in ["exit", "quit", "sair", "fim"]:
      asyncio.run(speak(brain(text_user)))
      break

    response = brain(text_user)
    asyncio.run(speak(response))

loop_chat()
