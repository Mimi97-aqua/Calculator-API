from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Calculation(BaseModel):
    num1: float
    num2: float
    operator: str

@app.get("/")
async def hello():
    return {"message": "Visit http://localhost:8000/calculate"}

@app.post("/calculate")
async def calculate(calculation: Calculation):
    num1 = calculation.num1
    num2 = calculation.num2
    operator = calculation.operator

    if operator == "add":
        result = num1 + num2
    elif operator == "subtract":
        result = num1 - num2
    elif operator == "multiply":
        result = num1 * num2
    elif operator == "divide":
        result = num1 / num2
    else:
        result = "Invalid operator"

    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

