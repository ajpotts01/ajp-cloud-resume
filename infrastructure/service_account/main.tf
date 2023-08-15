resource "google_service_account" "cloud_resume_service_account" {
  account_id = "ajp-${var.app_name}-sa"
  #project      = var.project_id
  display_name = "Cloud Resume Service Account"
}

# For some reason, this still requires a project to be set.
resource "google_project_iam_member" "cloud_run_invoker_binding" {
  project = var.project_id
  role    = "roles/run.invoker"
  member  = "serviceAccount:${google_service_account.cloud_resume_service_account.email}"
}