from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from engine import DrumMachine

dm = DrumMachine()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown lifecycle for FastAPI"""
    dm.load_samples("config.json")
    print("🎵 DrumMachine initialized and samples loaded.")
    yield
    print("👋 Server shutting down.")

app = FastAPI(lifespan=lifespan)

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/config")
def get_config():
    return dm.get_config()

@app.get("/pattern")
def get_pattern():
    return {"pattern": dm.make_pattern()}

@app.post("/bpm/{bpm}")
def set_bpm(bpm: int):
    dm.bpm = bpm
    return {"bpm": bpm}

@app.post("/swing/{value}")
def set_swing(value: float):
    dm.swing = value
    return {"swing": value}


