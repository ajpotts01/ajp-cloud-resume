resource "google_storage_bucket" "build_logs_bucket" {
  name     = "${var.app_name}-cloud-build-logs"
  location = var.region

  uniform_bucket_level_access = true
  public_access_prevention    = "enforced" # The documentation on this is woeful
  force_destroy               = true
}

resource "google_storage_bucket" "webapp_static" {
  name     = "${var.app_name}-webapp-static"
  location = var.region

  uniform_bucket_level_access = false
  force_destroy               = "true"
}

resource "google_storage_bucket_acl" "webapp_static_public_read" {
  bucket = google_storage_bucket.webapp_static.name
  predefined_acl = "publicRead"
}