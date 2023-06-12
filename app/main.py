from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import users, auth

app = FastAPI()

# CORS middleware to allow requests from any origin
app.add_middleware(CORSMiddleware, allow_origins=[
                   "*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
async def root():
    return {"message": "E-Commerce API"}


# app routes
app.include_router(users.router)
app.include_router(auth.router)