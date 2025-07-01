# https://metis-backend.onrender.com/
from fastapi import FastAPI, Depends
from supabase_api import create_supabase_client
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
supabase = create_supabase_client()

@app.post("/account")
def create_user(email, password):
    response = supabase.auth.sign_up({"email": email, "password": password,})
    return {
        "session": result.session.access_token,
        "user": result.user
    }
@app.get("/account")
def login_user(email: str, password: str):
    result = supabase.auth.sign_in_with_password({"email": email, "password": password})
    supabase.auth.set_session(result.session.access_token, result.session.refresh_token)
    return {
        "token": result.session.access_token,
        "user": result.user
    }

@app.post("/simulations")
def new_simulation(user_id: str, start_date: str, end_date: str, start_capital: float):
    response = supabase.table("Simulations").insert({
        "user_id": user_id,
        "start_date": start_date,
        "end_date": end_date,
        "current_date": start_date,
        "start_capital": start_capital,
        "current_capital": start_capital
    }).execute()

    return response