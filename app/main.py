from fastapi import FastAPI
from app.api.routes import router
import uvicorn

app = FastAPI()

# 라우터 등록
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")