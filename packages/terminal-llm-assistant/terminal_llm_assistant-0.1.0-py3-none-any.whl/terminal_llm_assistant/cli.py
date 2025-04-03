#!/usr/bin/env python3
"""
Módulo CLI para o assistente de terminal LLM
"""

import os
import sys
import argparse
import subprocess
import time
import json
import urllib.parse
import requests
from pathlib import Path
import pkg_resources
from dotenv import load_dotenv

from terminal_llm_assistant.utils import ensure_server_running, get_config_dir

def setup_command():
    """Configura o assistente LLM pela primeira vez"""
    config_dir = get_config_dir()
    
    # Criar diretório de configuração se não existir
    if not config_dir.exists():
        config_dir.mkdir(parents=True)
    
    # Solicitar a chave da API
    print("Configuração da API do Google Gemini")
    print("Uma chave da API do Google Gemini é necessária para este assistente.")
    print("Você pode obter uma chave em: https://makersuite.google.com/app/apikey")
    print("")
    
    api_key = input("Digite sua chave da API do Google Gemini: ").strip()
    
    if not api_key:
        print("Nenhuma chave fornecida. Configure manualmente o arquivo .env mais tarde.")
        api_key = "your_google_api_key_here"
    
    # Criar arquivo .env
    env_path = config_dir / ".env"
    with open(env_path, "w") as f:
        f.write(f"GEMINI_API_KEY={api_key}\n")
    
    print(f"\nConfigurações salvas em {env_path}")
    print("Agora você pode usar o comando 'ai' seguido da sua pergunta:")
    print("Exemplo: ai qual é a capital do Brasil?")
    
    return 0

def server_command():
    """Inicia o servidor LLM em primeiro plano"""
    from terminal_llm_assistant.server import run_server
    run_server()
    return 0

def ask_command(args):
    """Envia uma pergunta para o servidor LLM"""
    ensure_server_running()
    
    # Juntar os argumentos para formar a pergunta
    question = " ".join(args)
    
    if not question.strip():
        print("Uso: ai <sua pergunta aqui>")
        return 1
    
    # Codificar a pergunta para URL
    query = urllib.parse.quote(question)
    
    try:
        port = int(os.getenv("PORT", 8089))
        # Enviar a pergunta para o servidor
        response = requests.get(f"http://localhost:{port}/ask?q={query}")
        
        if response.status_code == 200:
            result = response.json()
            print("\n"+result["response"])
        else:
            print(f"Erro: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Erro ao comunicar com o servidor: {e}")
        return 1
    
    return 0

def main():
    """Ponto de entrada principal do CLI"""
    parser = argparse.ArgumentParser(description="Assistente de terminal LLM")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponíveis")
    
    # Comando de configuração
    setup_parser = subparsers.add_parser("setup", help="Configurar o assistente")
    
    # Comando do servidor
    server_parser = subparsers.add_parser("server", help="Iniciar o servidor")
    
    # Comando para perguntar
    ask_parser = subparsers.add_parser("ask", help="Fazer uma pergunta")
    ask_parser.add_argument("question", nargs="*", help="Sua pergunta")
    
    # Comando para parar o servidor
    stop_parser = subparsers.add_parser("stop", help="Para o servidor LLM")
    
    # Comando de versão
    version_parser = subparsers.add_parser("version", help="Mostra a versão")
    
    args = parser.parse_args()
    
    # Se nenhum comando for especificado, mostra a ajuda
    if args.command is None:
        parser.print_help()
        return 1
    
    # Executar o comando especificado
    if args.command == "setup":
        return setup_command()
    elif args.command == "server":
        return server_command()
    elif args.command == "ask":
        return ask_command(args.question)
    elif args.command == "stop":
        try:
            port = int(os.getenv("PORT", 8089))
            requests.post(f"http://localhost:{port}/shutdown")
            print("Servidor LLM parado com sucesso.")
        except:
            print("Servidor LLM já está parado ou não foi possível pará-lo.")
        return 0
    elif args.command == "version":
        print(f"terminal-llm-assistant versão {pkg_resources.get_distribution('terminal-llm-assistant').version}")
        return 0
    
    return 0

def ask():
    """Ponto de entrada para o comando 'ai'"""
    # Ignora o primeiro argumento (nome do script)
    return ask_command(sys.argv[1:])

if __name__ == "__main__":
    sys.exit(main())
