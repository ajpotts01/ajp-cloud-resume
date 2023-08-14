resource "google_project_service" "cloud_run_service" {
  project = var.project_id
  service = "run.googleapis.com"
}

resource "google_project_service" "cloud_build_service" {
    project = var.project_id
    service = "cloudbuild.googleapis.com"
}