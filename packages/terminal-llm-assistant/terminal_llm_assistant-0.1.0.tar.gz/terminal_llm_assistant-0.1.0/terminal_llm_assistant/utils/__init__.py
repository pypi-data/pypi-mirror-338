"""
Utilitários para o assistente de terminal
"""

import os
import sys
import time
import subprocess
import requests
from pathlib import Path

def get_config_dir():
    """Retorna o diretório de configuração do assistente"""
    if sys.platform == "win32":
        config_base = os.getenv("APPDATA")
        if not config_base:
            config_base = os.path.expanduser("~")
    else:
        config_base = os.path.expanduser("~/.config")
    
    return Path(config_base) / "terminal-llm-assistant"

def ensure_server_running():
    """Garante que o servidor LLM está rodando"""
    port = int(os.getenv("PORT", 8089))
    
    # Verificar se o servidor já está rodando
    try:
        response = requests.get(f"http://localhost:{port}/")
        if response.status_code == 200:
            return  # Servidor já está rodando
    except:
        pass  # Servidor não está rodando, vamos iniciá-lo
    
    # Iniciar o servidor em background
    if sys.platform == "win32":
        subprocess.Popen([sys.executable, "-m", "terminal_llm_assistant.server"],
                        creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        subprocess.Popen([sys.executable, "-m", "terminal_llm_assistant.server"],
                        start_new_session=True)
    
    # Aguardar o servidor iniciar
    for _ in range(30):  # Tenta por 30 segundos
        try:
            response = requests.get(f"http://localhost:{port}/")
            if response.status_code == 200:
                return
        except:
            pass
        time.sleep(1)
    
    raise Exception("Não foi possível iniciar o servidor LLM")
