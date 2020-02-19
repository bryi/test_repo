psql -U postgres -d blog_api_db -c "DROP TABLE alembic_version"
psql -U postgres -d blog_api_db -c "DROP TABLE blogposts"
psql -U postgres -d blog_api_db -c "DROP TABLE users"
export FLASK_ENV=development
export DATABASE_URL=postgres://postgres:1@127.0.0.1:5432/blog_api_db
export JWT_SECRET_KEY=$(python3 -c 'import os; print(os.urandom(24))')
#echo $JWT_SECRET_KEY
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
python3 run.py
