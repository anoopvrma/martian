# api.py
import uvicorn
from fastapi import FastAPI
from models.model import Model
from exceptions.error import InternalServerError

app = FastAPI()

# Replace "your_api_key_here" with your actual OpenAI API key

openai_api_key = ""
openai_model = Model(provider_name='openai', api_key=openai_api_key)

anthropic_api_key = ""
anthropic_model = Model(provider_name='anthropic', api_key=anthropic_api_key)

together_api_key = ""
together_model = Model(provider_name='together', api_key=together_api_key)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/complete")
def complete(prompt: str, provider: str, max_tokens: int, temperature: float, top_p: float, stream: bool = False):
    if prompt and provider and max_tokens and temperature and top_p:
        try:
            model = get_model(provider)
            response = model.complete(prompt, max_tokens, temperature, top_p, stream)
            return {"response": response}
        except InternalServerError as error:
            print(error)
            return {"error": error.message}
    else:
        return {"error": "Missing required parameters"}


def get_model(provider: str):
    if provider == 'openai':
        return openai_model
    elif provider == 'anthropic':
        return anthropic_model
    elif provider == 'together':
        return together_model
    else:
        raise InternalServerError("Unsupported engine")


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)