import os
from dotenv import load_dotenv
import ollama

# Cargar variables de entorno (.env)
load_dotenv()

MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:1b")

def main():
    print(f"Chat con modelo local: {MODEL}")
    print("Escribe 'salir' para terminar.\n")

    while True:
        user_input = input("Tú: ")

        if user_input.lower() in ["salir", "exit", "quit"]:
            print("Cerrando chat...")
            break

        response = ollama.chat(
            model=MODEL,
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        # Mostrar respuesta del modelo
        print("Modelo:", response["message"]["content"])

if __name__ == "__main__":
    main()
