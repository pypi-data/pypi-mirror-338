"""
Servidor HTTP que se comunica com a API Google Gemini
"""

import http.server
import socketserver
import json
import urllib.parse
import os
from pathlib import Path
from dotenv import load_dotenv
from litellm import completion

from terminal_llm_assistant.utils import get_config_dir

# Porta do servidor
PORT = os.getenv("PORT", 8089)
# Verifica se a variável de ambiente PORT foi definida
if PORT is None:
    print("A variável de ambiente PORT não está definida. Usando a porta padrão 8089.")
    PORT = 8089
# Verifica se a variável de ambiente PORT é um número
try:
    PORT = int(PORT)
except ValueError:
    print(f"A variável de ambiente PORT deve ser um número. Usando a porta padrão 8089.")
    PORT = 8089
# Verifica se a variável de ambiente PORT está dentro do intervalo permitido
if PORT < 1024 or PORT > 65535:
    print(f"A variável de ambiente PORT deve estar entre 1024 e 65535. Usando a porta padrão 8089.")
    PORT = 8089
# Verifica se a variável de ambiente PORT é um número inteiro
if not isinstance(PORT, int):
    print(f"A variável de ambiente PORT deve ser um número inteiro. Usando a porta padrão 8089.")
    PORT = 8089

MODEL = os.getenv("MODEL", "gemini/gemini-1.5-flash")
# Verifica se a variável de ambiente MODEL foi definida
if MODEL is None:
    print("A variável de ambiente MODEL não está definida. Usando o modelo padrão 'gemini/gemini-1.5-flash'.")
    MODEL = "gemini/gemini-1.5-flash"
# Verifica se a variável de ambiente MODEL é uma string
if not isinstance(MODEL, str):
    print(f"A variável de ambiente MODEL deve ser uma string. Usando o modelo padrão 'gemini/gemini-1.5-flash'.")
# Verifica se a variável de ambiente MODEL é um modelo válido
if MODEL not in ["gemini/gemini-1.5-flash", "gemini/gemini-2.0-flash"]:
    print(f"A variável de ambiente MODEL deve ser um modelo válido. Usando o modelo padrão 'gemini/gemini-1.5-flash'.")


class LLMHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Sobrescreve o método de log para não exibir as requisições
        pass
    def do_POST(self):
        if self.path == "/shutdown":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Shutting down...")
            self.server.shutdown()
            return
    
    def do_GET(self):
        # Rota de verificação (healthcheck)
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Server running")
            return
            
        # Rota para fazer perguntas
        if self.path.startswith('/ask'):
            # Extrair a pergunta da URL
            query_components = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            if 'q' in query_components:
                question = query_components['q'][0]
                
                # Obter resposta da API LLM 
                response = self.get_llm_response(question)
                
                # Enviar resposta
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"response": response}).encode())
            else:
                self.send_error(400, "Parâmetro 'q' não encontrado")
        else:
            self.send_error(404, "Rota não encontrada")
    
    def get_llm_response(self, question):
        """
        Função que se comunica com a API do Google Gemini via LiteLLM
        """
        try:
            # Obter a chave da API
            api_key = os.getenv("GEMINI_API_KEY")
            
            if not api_key or api_key == "your_google_api_key_here":
                return "Erro: API key do Gemini não configurada. Execute 'terminal-llm setup' para configurar."
            
            # Configurar a chave da API para o LiteLLM
            os.environ["GOOGLE_API_KEY"] = api_key
             # Fazer a chamada para a API usando o LiteLLM com Gemini
            response = completion(
                model=f"{MODEL}",  # Modelo do Gemini
                messages=[{
                    "role": "system",
                    "content": "Responda de forma clara e direta, sem usar formatação markdown ou caracteres especiais. Use linguagem simples e evite símbolos como *, `, #. Sempre apresente um exemplo do que for pedido ser for pessível."
                },
                {
                    "role": "user",
                    "content": question
                }]
            )
            
            # Extrair o conteúdo da resposta
            return response.choices[0].message.content
                
        except Exception as e:
            return f"Erro ao acessar a API Gemini: {str(e)}"

def run_server():
    """Inicia o servidor HTTP"""
    # Carregar configurações
    config_dir = get_config_dir()
    env_path = config_dir / ".env"
    
    # Verificar se o arquivo .env existe
    if not env_path.exists():
        print(f"Arquivo .env não encontrado em {env_path}")
        print("Execute 'terminal-llm setup' para configurar o assistente.")
        return
    
    # Carregar variáveis de ambiente
    load_dotenv(env_path)
    
    # Iniciar o servidor
    with socketserver.TCPServer(("", PORT), LLMHandler) as httpd:
        print(f"Servidor LLM rodando na porta {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
