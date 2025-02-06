import httpx

async def get_fun_fact(number: int) -> str:
    url = f"http://numbersapi.com/{number}/math"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text if response.status_code == 200 else "No fact available"
