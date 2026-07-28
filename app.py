import os
import subprocess

db_url = os.environ.get("DB_URL")
if not db_url:
    raise ValueError("DB_URL secret is not set!")

port = os.environ.get("PORT", "10000")

cmd = [
    "mlflow", "server",
    "--backend-store-uri", db_url,
    "--default-artifact-root", "./mlartifacts",
    "--host", "0.0.0.0",
    "--port", port,
    "--workers", "1",
    "--uvicorn-opts", "--loop uvloop --http h11 --workers 1"
]

subprocess.run(cmd)
