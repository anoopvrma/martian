# api.py
import uvicorn
from fastapi import FastAPI
from models.model import Model

app = FastAPI()

# Replace "your_api_key_here" with your actual OpenAI API key

openai_api_key = "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"
openai_model = Model(provider_name='openai', api_key=openai_api_key)

anthropic_api_key = "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"
anthropic_model = Model(provider_name='anthropic', api_key=anthropic_api_key)

together_api_key = "f67e3d65823db01cf45e224a07e06362a58d2d08f513af14a1af9a24cee6a6e2"
together_model = Model(provider_name='together', api_key=together_api_key)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/complete")
def complete(prompt: str, provider: str, max_tokens: int, temperature: float, top_p: float):
    if prompt and provider and max_tokens and temperature and top_p:
        if provider == 'openai':
            response = openai_model.complete(prompt, max_tokens, temperature, top_p)
            return {"response": response}
        elif provider == 'anthropic':
            response = anthropic_model.complete(prompt, max_tokens, temperature, top_p)
            return {"response": response}
        elif provider == 'together':
            response = together_model.complete(prompt, max_tokens, temperature, top_p)
            return {"response": response}
        else:
            return {"error": "Unsupported engine"}
    else:
        return {"error": "Missing required parameters"}

# Additional endpoints can be added for other providers


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)