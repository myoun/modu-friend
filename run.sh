poetry install
gunicorn -k uvicorn.workers.UvicornWorker --access-logfile ./gunicorn-access.log mfriend.main:app --bind 0.0.0.0:8000 --workers 4

echo Successfully started gunicorn service