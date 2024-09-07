from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from domain.fixture import fixture_router
from domain.player import player_router
from domain.team import team_router

app = FastAPI()

# cors origin setting area
origins = [
    "http://127.0.0.1:5173",
    "https://benchmark-frontend.vercel.app",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(fixture_router.router)
app.include_router(player_router.router)
app.include_router(team_router.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)