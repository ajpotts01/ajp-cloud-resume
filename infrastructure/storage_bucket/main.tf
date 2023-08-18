resource "google_storage_bucket" "build_logs_bucket" {
  name = "${var.app_name}-cloud-build-logs"
  location = var.region

  uniform_bucket_level_access = true
  public_access_prevention = "enforced" # The documentation on this is woeful
}