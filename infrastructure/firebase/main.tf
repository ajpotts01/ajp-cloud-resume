# Terraform configuration to set up providers by version.
terraform {
  required_providers {
    google-beta = {
      source  = "hashicorp/google-beta"
      version = "~> 4.0"
      configuration_aliases = [ google-beta.main, google-beta.no_user_project_override ]
    }
  }
}

resource "google_project_service" "firebase" {
  project = var.project_id
  provider = google-beta.no_user_project_override
  service  = "firebase.googleapis.com"
}

# Enables Firebase services for the new project created above.
resource "google_firebase_project" "default" {
  provider = google-beta.no_user_project_override
  project  = var.project_id
  depends_on = [ google_project_service.firebase ]
}