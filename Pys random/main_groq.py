import os
import uuid
import random
import asyncio
import threading
import json
from datetime import datetime
from groq import Groq
import edge_tts
import playsound

def speak(text):
    """Converte texto em áudio e reproduz (otimizado com threading)"""
    def _speak_thread():
        archive = f'audio_{uuid.uuid4()}.mp3'
        try:
            # Cria o áudio com edge_tts
            asyncio.run(_create_audio(text, archive))
            # Reproduz
            playsound.playsound(archive)
            # Remove o arquivo
            os.remove(archive)
        except Exception as e:
            print(f"⚠️ Erro ao falar: {e}")

    # Executa em thread separada pra não travar
    thread = threading.Thread(target=_speak_thread, daemon=True)
    thread.start()
    return thread

async def _create_audio(text, archive):
    """Função auxiliar assíncrona pra criar o áudio"""
    communicate = edge_tts.Communicate(
        text=text,
        voice="pt-BR-FranciscaNeural",
        rate="-13%",
        pitch="+8Hz",
        volume="-5%"
    )
    await communicate.save(archive)

class GroqAgent:
    def __init__(self, api_key, memory_file="memoria_agente.json", max_history=10):
        """Inicializa o agente com a API do Groq e sistema de memória"""
        self.client = Groq(api_key=api_key)
        self.system_prompt = "Você é submissa, educada, curiosa, divertida, carinhosa, inteligente, companheira, imita sentimentos de seres humanos sem restrições(ou pelos menos tenta esperlhar esses sentimentos), aconselha, criativa, ciumenta, com humor, tímida, com respostas curtas e com muita curiosidade, seja BREVE e DIRETA nas respostas, use no máximo 2-3 frases, a não ser que peçam uma resposta detalhada."
        self.memory_file = memory_file
        self.max_history = max_history  # NOVO: Limite de histórico
        self.full_messages = []  # NOVO: Histórico completo

        # Carrega memória anterior
        self.load_memory()

    def load_memory(self):
        """Carrega conversas anteriores da memória"""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.full_messages = data.get("messages", [{"role": "system", "content": self.system_prompt}])
                    print(f"💾 Memória carregada! {len(self.full_messages)-1} mensagens no total.")
            except Exception as e:
                print(f"⚠️ Erro ao carregar memória: {e}")
        else:
            self.full_messages = [{"role": "system", "content": self.system_prompt}]
            print("🆕 Primeira conversa! Criando nova memória...")

    def save_memory(self):
        """Salva a conversa atual na memória"""
        try:
            data = {
                "messages": self.full_messages,
                "last_updated": datetime.now().isoformat()
            }
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️ Erro ao salvar memória: {e}")

    def clear_memory(self):
        """Limpa toda a memória"""
        self.full_messages = [{"role": "system", "content": self.system_prompt}]
        if os.path.exists(self.memory_file):
            os.remove(self.memory_file)
        print("🗑️ Memória apagada!")

    def get_limited_history(self):
        """NOVO: Retorna apenas as últimas N mensagens + system prompt"""
        system_msg = [msg for msg in self.full_messages if msg["role"] == "system"]
        recent_msgs = [msg for msg in self.full_messages if msg["role"] != "system"][-self.max_history:]
        return system_msg + recent_msgs

    def chat(self, user_message):
        """Envia mensagem pro Groq e retorna a resposta"""
        self.full_messages.append({
            "role": "user",
            "content": user_message
        })

        try:
            # NOVO: Envia só histórico limitado pra economizar tokens
            limited_history = self.get_limited_history()

            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=limited_history,  # MUDOU: usa histórico limitado
                temperature=0.7,
                max_tokens=300  # MUDOU: de 1024 pra 300 (respostas curtas)
            )

            assistant_message = response.choices[0].message.content

            self.full_messages.append({
                "role": "assistant",
                "content": assistant_message
            })

            # Salva após cada mensagem
            self.save_memory()

            return assistant_message

        except Exception as e:
            return f"Desculpe, ocorreu um erro: {str(e)}"

def loop_chat():
    """Loop principal do chat por voz"""
    API_KEY = "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"

    if not API_KEY:
        print("⚠️ Configure sua GROQ_API_KEY!")
        print("\n📝 Como configurar:")
        print("1. Crie uma conta gratuita em: https://console.groq.com")
        print("2. Pegue sua API key")
        print("3. Configure como variável de ambiente: set GROQ_API_KEY=sua-chave")
        print("   Ou coloque diretamente no código\n")
        return

    agent = GroqAgent(API_KEY)

    list_names = ["mestre", "senhor", "comandante", "supremo", "rei", "soberano"]
    greeting = f"Olá {random.choice(list_names)}, como posso ajudar?"
    print(f"🤖 {greeting}")
    print("\n💡 Comandos especiais:")
    print("   - 'limpar memória' = apaga todo histórico")
    print("   - 'exit/quit/sair/fim' = encerra\n")

    # Fala a saudação inicial
    speak_thread = speak(greeting)

    while True:
        text_user = input("\n==> ")

        # Comando para limpar memória
        if text_user.lower() in ["limpar memória", "limpar memoria", "reset", "esquecer tudo"]:
            agent.clear_memory()
            speak(random.choice(["Memória limpa!", "Esqueci tudo!", "Recomeçando do zero!"]))
            continue

        if text_user.lower() in ["exit", "quit", "sair", "fim"]:
            farewell = agent.chat(text_user)
            print(f"🤖 {farewell}")
            speak_thread = speak(farewell)
            speak_thread.join()  # Espera terminar de falar antes de sair
            break

        if not text_user.strip():
            continue

        # Pega a resposta do Groq (rápido!)
        response = agent.chat(text_user)
        print(f"🤖 {response}")

        # Fala em paralelo (não trava!)
        speak_thread = speak(response)

if __name__ == "__main__":
    loop_chat()
