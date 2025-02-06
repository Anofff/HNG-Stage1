from fastapi import FastAPI, HTTPException
from app.utils import classify_number
from app.models import NumberResponse, ErrorResponse
from app.services import get_fun_fact

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
