from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse,StreamingResponse
from services.chatVoice_service import process_question
from pydantic import BaseModel
from starlette.responses import Response

router = APIRouter()



# Define el modelo que representa el cuerpo de la solicitud
class QuestionRequest(BaseModel):
    question: str

@router.post("/getVoice/")
async def get_voice(question_request: QuestionRequest):
    # Obtener la pregunta desde el modelo Pydantic
    question = question_request.question
    
    # Generar el audio a partir de la pregunta
    audio_buffer = await process_question(question)

    if audio_buffer:
        # Preparar la respuesta como un archivo descargable (MP3)
        return StreamingResponse(
            audio_buffer, 
            media_type="audio/mpeg",
            headers={
                "Content-Disposition": "attachment; filename=audio.mp3"
            }
        )
    else:
        # En caso de error, retornar un mensaje JSON con el código de error
        return JSONResponse(content={"message": "Error al generar el audio"}, status_code=500)


@router.get("/help")
async def help_inf():
    
    return {
        "description": "Este programa permite enviar una pregunta, la cual es procesada por gemini y devuelve una respuesta en formato de audio.",
        "steps": [
            "Envía una pregunta.",
            "El programa usara la api de gemini.",
            "Se generaráa una respuesta en formato mp3."
        ],
        "endpoints": {
            "/getVoice": "Envía tu pregunta.",
            
        },
    }