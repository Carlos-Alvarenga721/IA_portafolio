import os
from dotenv import load_dotenv
import ollama

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración del modelo (por defecto 'mistral' si no encuentra nada en .env)
MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:1b")

def main():
    print(f"Chat con memoria temporal usando modelo: {MODEL}")
    print("Escribe '/exit' para terminar.\n")

    # Aquí guardaremos el historial de conversación
    conversation = []

    while True:
        # 1. Recibir entrada del usuario
        user_input = input("Tú: ")

        # Comando de salida
        if user_input.lower() in ["/exit", "salir", "quit"]:
            print("Chat finalizado.")
            break

        # 2. Guardar mensaje del usuario en historial
        conversation.append({"role": "user", "content": user_input})

        # 3. Enviar historial completo al modelo
        response = ollama.chat(
            model=MODEL,
            messages=conversation
        )

        # 4. Guardar respuesta del modelo en historial
        assistant_message = response["message"]["content"]
        conversation.append({"role": "assistant", "content": assistant_message})

        # 5. Mostrar respuesta en consola
        print("Asistente:", assistant_message)

if __name__ == "__main__":
    main()
