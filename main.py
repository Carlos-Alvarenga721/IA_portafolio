import os 
from dotenv import load_dotenv

# Cargar variables desde .env si existe
load_dotenv()

# Configuración
MODEL = os.getenv("OLLAMA_MODEL", "mistral")

# 1) Opción A: usar el cliente oficial de Python
try:
    import ollama

    print(f"Usando modelo: {MODEL}")
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": "Responde 'OK' si todo está funcionando."},
        ],
    )
    print("Respuesta de Ollama:", response["message"]["content"])

except Exception as e:
    print("No se pudo usar el cliente 'ollama' de Python.")
    print(
        "¿Está el servicio de Ollama corriendo? Prueba con 'ollama serve' en otra ventana."
    )
    print("Error:", repr(e))
