import os
import sys

# 1. Заглушаем тяжелые фоновые задачи MLflow до импорта
os.environ["MLFLOW_DISABLE_ENV_CREATION"] = "true"
os.environ["GUNICORN_CMD_ARGS"] = "--workers 1 --threads 1"

# 2. Получаем секреты
db_url = os.environ.get("DB_URL")
if not db_url:
    raise ValueError("DB_URL secret is not set!")

port = os.environ.get("PORT", "10000")

# 3. Запускаем сервер с 1 воркером и без артефактов
import subprocess

cmd = [
    "mlflow", "server",
    "--backend-store-uri", db_url,
    "--default-artifact-root", "./mlartifacts",
    "--host", "0.0.0.0",
    "--port", port,
    "--workers", "1"
]

subprocess.run(cmd)
