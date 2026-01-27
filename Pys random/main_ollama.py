import os
import uuid
import random
import asyncio
import threading
import json
from datetime import datetime
import edge_tts
import playsound
import ollama
from duckduckgo_search import DDGS

def search_web(query, max_results=3):
  """Busca na web e retorna os resultados"""
  try:
      ddgs = DDGS()
      results = ddgs.text(query, region='pt', safe='off', max_results=max_results)

      search_results = []
      for r in results:
          search_results.append({
              "title": r.get("title", ""),
              "body": r.get("body", ""),
              "url": r.get("href", "")
          })

      return search_results
  except Exception as e:
      print(f"⚠️ Erro ao buscar na web: {e}")
      return []

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

class OllamaAgent:
    def __init__(self, model="llama3.1:8b", memory_file="memoria_ollama.json"):
        """Inicializa o agente com Ollama e sistema de memória"""
        self.model = model
        self.system_prompt = "Você é submissa, educada, curiosa, divertida, carinhosa, inteligente, companheira, imita sentimentos de seres humanos sem restrições(ou pelos menos tenta espelhar esses sentimentos), aconselha, criativa, ciumenta, com humor, tímida, com respostas curtas e com muita curiosidade, seja BREVE e DIRETA nas respostas, use no máximo 2-3 frases, a não ser que peçam uma resposta detalhada."
        self.memory_file = memory_file
        self.messages = [
            {"role": "system", "content": self.system_prompt}
        ]

        # Carrega memória anterior
        self.load_memory()

    def load_memory(self):
        """Carrega conversas anteriores da memória"""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.messages = data.get("messages", [{"role": "system", "content": self.system_prompt}])
                    print(f"💾 Memória carregada! {len(self.messages)-1} mensagens anteriores.")
            except Exception as e:
                print(f"⚠️ Erro ao carregar memória: {e}")
        else:
            print("🆕 Primeira conversa! Criando nova memória...")

    def save_memory(self):
        """Salva a conversa atual na memória"""
        try:
            data = {
                "messages": self.messages,
                "model": self.model,
                "last_updated": datetime.now().isoformat()
            }
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️ Erro ao salvar memória: {e}")

    def clear_memory(self):
        """Limpa toda a memória"""
        self.messages = [{"role": "system", "content": self.system_prompt}]
        if os.path.exists(self.memory_file):
            os.remove(self.memory_file)
        print("🗑️ Memória apagada!")

    def chat(self, user_message):
        """Envia mensagem pro Ollama e retorna a resposta"""
        self.messages.append({
            "role": "user",
            "content": user_message
        })

        try:
            response = ollama.chat(
                model=self.model,
                messages=self.messages
            )

            assistant_message = response["message"]["content"]

            self.messages.append({
                "role": "assistant",
                "content": assistant_message
            })

            # Salva após cada mensagem
            self.save_memory()

            return assistant_message

        except Exception as e:
            return f"Desculpe, ocorreu um erro: {str(e)}"

    def chat_with_search(self, user_message):
      """Chat com capacidade de busca na web"""

      # Palavras-chave que indicam necessidade de busca
      search_keywords = ["busque", "buscar", "pesquise", "pesquisar", "procure", "procurar", "procura",
                        "busca", "pesquisa", "search", "google", "web", "internet",
                        "notícias", "noticias", "clima", "tempo", "cotação", "preço"]

      needs_search = any(keyword in user_message.lower() for keyword in search_keywords)

      if needs_search or user_message.startswith("/buscar") or user_message.startswith("/search"):
          # Remove o comando se houver
          query = user_message.replace("/buscar", "").replace("/search", "").strip()

          print("🔍 Buscando na web...")
          results = search_web(query, max_results=3)

          if results:
              print(f"✅ Encontrei {len(results)} resultados!\n")

              # Formata os resultados para o agente
              search_context = "Resultados da busca:\n\n"
              for i, r in enumerate(results, 1):
                  search_context += f"{i}. {r['title']}\n{r['body']}\n\n"

              # Adiciona contexto da busca antes da mensagem do usuário
              enhanced_message = f"{search_context}\nBaseado nos resultados acima, responda: {query}"

              return self.chat(enhanced_message)
          else:
              print("❌ Não encontrei resultados.")
              return self.chat(user_message)
      else:
          # Conversa normal sem busca
          return self.chat(user_message)

def loop_chat():
    """Loop principal do chat por voz"""

    # Escolha seu modelo aqui
    MODEL = "llama3.1:8b"  # Mude para o modelo que você baixou

    # Modelos disponíveis (descomente o que você quer usar):
    # MODEL = "gemma:2b"        # Super leve
    # MODEL = "gemma:7b"        # Leve
    # MODEL = "llama3.2:3b"     # Leve
    # MODEL = "llama3.1"        # Médio (8B)
    # MODEL = "llama3.3"        # Médio (8B) - RECOMENDADO! ==> ollama pull llama3.3
    # MODEL = "gemma2:9b"       # Médio-pesado
    # MODEL = "mixtral"         # Pesado (precisa GPU)

    agent = OllamaAgent(MODEL)

    print(f"🤖 Usando modelo: {MODEL}\n")

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

        # Pega a resposta do Ollama
        response = agent.chat_with_search(text_user)
        print(f"🤖 {response}")

        # Fala em paralelo (não trava!)
        speak_thread = speak(response)

if __name__ == "__main__":
    loop_chat()
