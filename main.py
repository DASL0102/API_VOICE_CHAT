from fastapi import FastAPI
from controllers.chatVoice_controller import router as image_router

app = FastAPI()

# Incluir el router de imágenes
app.include_router(image_router)
