# https://usher.dev/posts/django-on-flyio-with-litestream-litefs/
echo $GCS_DB_URL
ls
litestream restore -if-db-not-exists -if-replica-exists -o "/db/db.sqlite3" "$GCS_DB_URL"

python manage.py migrate
python manage.py createcachetable
python manage.py collectstatic --verbosity 2 --no-input

chmod -R a+rwX /tmp

exec litestream replicate -config ./litestream.yml # Should execute the gunicorn command