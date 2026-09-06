import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse

from app.core.config import settings
from app.api.routes import router as api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Intelligent Decision Support System for Vessel Chartering & Bulk Cargo TLC Optimization (SIH262006)",
    version=settings.PROJECT_VERSION
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include core REST API endpoints
app.include_router(api_router, prefix="/api")

static_dir = os.path.join(os.path.dirname(__file__), "..", "static")

@app.get("/")
def serve_root():
    index_file = os.path.join(static_dir, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return RedirectResponse(url="/docs")

@app.get("/fallback_data.js")
def serve_fallback_js():
    file_path = os.path.join(static_dir, "fallback_data.js")
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="application/javascript")
    return {"error": "not found"}

if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
