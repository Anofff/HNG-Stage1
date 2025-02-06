from fastapi import FastAPI, HTTPException
from utils import classify_number
from models import NumberResponse, ErrorResponse
from services import get_fun_fact

app = FastAPI()

@app.get("/api/classify-number", response_model=NumberResponse, responses={400: {"model": ErrorResponse}})
async def classify_number_api(number: str):
    try:
        num = int(number)
    except ValueError:
        raise HTTPException(status_code=400, detail={"number": number, "error": True})

    classification = classify_number(num)
    fun_fact = await get_fun_fact(num)
    
    return {**classification, "fun_fact": fun_fact}
