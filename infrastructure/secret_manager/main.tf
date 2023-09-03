# Only the secret is created.
# Not storing passwords in Terraform state.

resource "google_secret_manager_secret" "django_superuser_password" {
  secret_id = "${var.app_name}-django-superuser-password"

  replication {
    user_managed {
      replicas {
        location = var.region
      }
    }
  }
}