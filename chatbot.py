from fastapi import FastAPI
import ollama

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to your AI chatbot!"}

@app.get("/chat")
def chat(message: str):
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": message}])
    return {"reply": response["message"]}
