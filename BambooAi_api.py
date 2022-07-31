from re import S
from fastapi import FastAPI, HTTPException
from BambooAi import generate_branding_snippet, generate_keywords, validate_length

app = FastAPI()

@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet}


@app.get("/generate_keywords")
async def generate_keywords_api(prompt: str):
    validate_input_length(prompt)
    snippet = generate_keywords(prompt)
    return {"Keywords": snippet}


def validate_input_length(prompt: str):
    if len(prompt) >= 12:
        raise HTTPException(
            status_code=400, detail="input length is too long, must be under 12 characters")
    pass

# uvicorn copykitt_api:app --reload
