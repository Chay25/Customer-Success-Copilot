# Deployment Guide

## Option 1: Local Demo
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open API docs: `http://127.0.0.1:8000/docs`

## Option 2: Render
1. Create a new Web Service.
2. Connect your GitHub repository.
3. Build command: `pip install -r requirements.txt`
4. Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

## Optional LLM Mode
Create `.env`:
```env
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key_here
```
Without an API key, the project still works using local rule-based logic.
