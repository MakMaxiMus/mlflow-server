
import os
import subprocess

db_url = os.environ.get("DB_URL")
port = os.environ.get("PORT", "10000")

cmd = [
    "mlflow", "server",
    "--backend-store-uri", db_url,
    "--default-artifact-root", "./mlartifacts",
    "--host", "0.0.0.0",
    "--port", port
]

subprocess.run(cmd)
