#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de teste para API do OpenWeatherMap
"""

import requests

print("=" * 60)
print("🧪 TESTE DE API - OPENWEATHERMAP")
print("=" * 60)

# COLOQUE SUA KEY AQUI:
API_KEY = "96462feb20e6faea1fe9344be8361596"  # ← Cole sua key entre as aspas

if not API_KEY:
    print("\n❌ ERRO: Cole sua API key na variável API_KEY acima!")
    print("   Edite este arquivo e coloque a key entre as aspas")
    exit()

print(f"\n🔑 API Key: {API_KEY[:10]}...{API_KEY[-5:]}")

# Teste 1: Validar key
print("\n📡 Teste 1: Validando API key...")
cidade = "Sao Paulo"
url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt"

try:
    response = requests.get(url, timeout=10)

    print(f"   Status Code: {response.status_code}")

    if response.status_code == 200:
        print("   ✅ API Key VÁLIDA!")

        data = response.json()

        print("\n🌡️ Dados recebidos:")
        print(f"   Cidade: {data['name']}")
        print(f"   Temperatura: {data['main']['temp']}°C")
        print(f"   Sensação: {data['main']['feels_like']}°C")
        print(f"   Condição: {data['weather'][0]['description']}")
        print(f"   Umidade: {data['main']['humidity']}%")

        print("\n✅ TUDO FUNCIONANDO PERFEITAMENTE!")

    elif response.status_code == 401:
        print("   ❌ API Key INVÁLIDA!")
        print("   Verifique se:")
        print("   1. Copiou a key correta do site")
        print("   2. A key foi ativada (pode demorar alguns minutos)")
        print("   3. Está usando a key certa da sua conta")

    elif response.status_code == 404:
        print("   ⚠️ Cidade não encontrada")
        print("   Tentando com outra cidade...")

    else:
        print(f"   ⚠️ Erro desconhecido: {response.status_code}")
        print(f"   Resposta: {response.text}")

except requests.exceptions.Timeout:
    print("   ❌ Timeout: API não respondeu a tempo")
    print("   Sua conexão com internet está ok?")

except requests.exceptions.ConnectionError:
    print("   ❌ Erro de conexão")
    print("   Verifique sua internet!")

except Exception as e:
    print(f"   ❌ Erro: {e}")

# Teste 2: Testar com outra cidade
print("\n📡 Teste 2: Testando com Rio de Janeiro...")
url2 = f"http://api.openweathermap.org/data/2.5/weather?q=Rio de Janeiro&appid={API_KEY}&units=metric&lang=pt"

try:
    response2 = requests.get(url2, timeout=10)
    if response2.status_code == 200:
        data2 = response2.json()
        print(f"   ✅ {data2['name']}: {data2['main']['temp']}°C")
    else:
        print(f"   ⚠️ Status: {response2.status_code}")
except:
    print("   ❌ Falhou")

print("\n" + "=" * 60)
print("🔍 DIAGNÓSTICO:")

if response.status_code == 200:
    print("✅ API OpenWeatherMap funcionando PERFEITAMENTE!")
    print("✅ Você pode usar esta key no Luna!")
elif response.status_code == 401:
    print("❌ Problema com a API Key")
    print("\n📝 CHECKLIST:")
    print("   [ ] Copiou a key correta?")
    print("   [ ] Esperou alguns minutos após criar?")
    print("   [ ] Confirmou o email da conta?")
    print("\n🔗 Acesse: https://home.openweathermap.org/api_keys")
    print("   Verifique se a key está 'Active'")
else:
    print(f"⚠️ Erro HTTP {response.status_code}")
    print("   Tente novamente em alguns minutos")

print("=" * 60)
