# https://usher.dev/posts/django-on-flyio-with-litestream-litefs/
if [[ -z "$GCS_DB_URL" ]]; then
    echo "S3_DB_URL env var not specified - this should be an S3-style URL to the location of the replicated database file"
    exit 1
fi

echo $GCS_DB_URL
litestream restore -if-db-not-exists -if-replica-exists -o "/tmp/db.sqlite3" "$GCS_DB_URL"

python manage.py migrate
python manage.py createcachetable
python manage.py collectstatic --verbosity 2 --no-input

chmod -R a+rwX /tmp

exec litestream replicate -config litestream.yml # Should execute the gunicorn command