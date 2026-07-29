import os
import subprocess

db_url = os.environ.get("DB_URL")
if not db_url:
    raise ValueError("DB_URL secret is not set!")

port = os.environ.get("PORT", "10000")

# 1. Автоматически приводим схему базы Neon в соответствие
print("Upgrading database schema...")
subprocess.run(["mlflow", "db", "upgrade", db_url], check=True)

# 2. Запускаем сервер MLflow
print("Starting MLflow server...")
cmd = [
    "mlflow", "server",
    "--backend-store-uri", db_url,
    "--default-artifact-root", "./mlartifacts",
    "--host", "0.0.0.0",
    "--port", port
]

subprocess.run(cmd)
