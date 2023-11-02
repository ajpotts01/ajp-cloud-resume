terraform {
  required_version = ">= 0.13.5"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.66"
    }

    google-beta = {
      source  = "hashicorp/google-beta"
      version = "~> 4.66"
    }
  }
}

provider "google-beta" {
  project = var.project_id
  alias = "main"
}

provider "google-beta" {
  project = var.project_id
  alias = "no_user_project_override"
  user_project_override = false
}