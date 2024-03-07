import uvicorn

from fastapi import FastAPI
from use_case.process_file import ProcessFileUseCase


app = FastAPI()
@app.get("/create-user-summary/{filename}/{account}")
async def search(filename: str, account: str):
    try:
        use_case = ProcessFileUseCase(filename=filename, account=account)
        result = use_case.execute()
        return {"status": 1, "code": 200, "message": "Success", "data": result}
    except FileNotFoundError as e:
        return {"status": 0, "code": 404, "message": str(e)}
    except Exception as e:
        return {"status": 0, "code": 500, "message": str(e)}

