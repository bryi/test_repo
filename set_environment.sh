export FLASK_ENV='development'
export DATABASE_URL='postgres://postgres:1@127.0.0.1:5432/blog_api_db'
export JWT_SECRET_KEY=$(python3 -c 'import os; print(os.urandom(24))')
export PYTHONPATH='$(pwd)'
