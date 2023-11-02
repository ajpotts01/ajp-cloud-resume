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

resource "google_project_service" "secret_manager" {
  service = "secretmanager.googleapis.com"
}

resource "google_project_service" "cloud_resource_manager" {
  project = var.project_id
  service = "cloudresourcemanager.googleapis.com"
}

resource "google_project_service" "service_usage" {
  project = var.project_id
  service = "serviceusage.googleapis.com"
}