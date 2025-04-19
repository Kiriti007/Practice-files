from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS so frontend can talk to it
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev only, restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Render!"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    # TODO: Process the file content (e.g. OCR + GPT)
    return {"filename": file.filename, "size": len(content)}
