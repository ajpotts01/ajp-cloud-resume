# https://usher.dev/posts/django-on-flyio-with-litestream-litefs/
python manage.py migrate
python manage.py createcachetable
python manage.py collectstatic --verbosity 2 --no-input

litestream restore -if-db-not-exists -if-replica-exists -o "/tmp/db.sqlite3" "$GCS_DB_URL"

chmod -R a+rwX /tmp

exec litestream replicate -config litestream.yml # Should execute the gunicorn command