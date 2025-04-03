"""
Utilitários para o assistente de terminal LLM
"""

import os
import sys
import subprocess
import time
import requests
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

def get_config_dir():
    """Retorna o diretório de configuração do assistente"""
    return Path.home() / ".terminal_llm_assistant"

def is_server_running():
    """Verifica se o servidor LLM está rodando"""
    try:
        port = int(os.getenv("PORT", 8000))
        response = requests.get(f"http://localhost:{port}", timeout=1)
        return True
    except:
        return False

def start_server_background():
    """Inicia o servidor LLM em segundo plano"""
    config_dir = get_config_dir()
    
    # Criar diretório de configuração se não existir
    if not config_dir.exists():
        config_dir.mkdir(parents=True)
    
    # Caminho para o módulo do servidor
    server_module = "terminal_llm_assistant.server"
    
    # Arquivo de log
    log_file = config_dir / "server.log"
    
    # Iniciar o servidor em segundo plano
    if sys.platform == "win32":
        # Versão para Windows
        subprocess.Popen(
            ["pythonw", "-m", server_module],
            stdout=open(log_file, "a"),
            stderr=subprocess.STDOUT,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
    else:
        # Versão para Unix/Linux/Mac
        subprocess.Popen(
            ["python", "-m", server_module],
            stdout=open(log_file, "a"),
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
    
    # Aguardar o servidor iniciar
    time.sleep(2)

def ensure_server_running():
    """Garante que o servidor esteja rodando, iniciando-o se necessário"""
    if not is_server_running():
        print("Iniciando o servidor LLM...")
        start_server_background()
        
        # Verificar novamente após iniciar
        if not is_server_running():
            print("Erro ao iniciar o servidor. Verifique os logs em:", get_config_dir() / "server.log")