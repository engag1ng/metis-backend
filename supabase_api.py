from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

def create_supabase_client() -> Client:
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    client: Client = create_client(url, key)
    return client