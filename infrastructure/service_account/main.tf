resource "google_service_account" "cloud_resume_service_account" {
  account_id = "ajp-${var.app_name}-sa"
  #project      = var.project_id
  display_name = "Cloud Resume Service Account"
}