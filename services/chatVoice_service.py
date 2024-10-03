
import google.generativeai as genai
import os
from gtts import gTTS
from io import BytesIO

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")


async def process_question(question):
    try:
        # Generar la respuesta del modelo (simulado)
        response = model.generate_content("responde esta pergunta de manera que simules que estas hablando para convertirla a voz, evita usar * y #, ademas eres un experto en el tema de la pregunta: "+ question)
        texto = response.text
        
        # Crear el objeto gTTS con el texto generado
        tts = gTTS(text=texto, lang='es')

        # Crear un objeto BytesIO para almacenar el audio en memoria
        audio_buffer = BytesIO()

        # Guardar el archivo de audio en el objeto BytesIO en lugar de en un archivo
        tts.write_to_fp(audio_buffer)

        # Mover el puntero del buffer al principio
        audio_buffer.seek(0)

        # print("El audio ha sido generado correctamente y está listo para ser retornado.")

        # Retornar el audio en formato de BytesIO
        return audio_buffer

    except Exception as e:
        print(f"Error procesando la pregunta: {e}")
        return None
