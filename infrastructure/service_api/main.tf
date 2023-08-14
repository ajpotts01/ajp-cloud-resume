resource "google_project_service" "cloud_run_service" {
  #project = var.project_id
  service = "run.googleapis.com"
}

resource "google_project_service" "cloud_build_service" {
  #project = var.project_id
  service = "cloudbuild.googleapis.com"
}

resource "google_project_service" "compute_service" {
  #project = var.project_id
  service = "compute.googleapis.com"
}

resource "google_project_service" "dns_service" {
  #project = var.project_id
  service = "dns.googleapis.com"
}