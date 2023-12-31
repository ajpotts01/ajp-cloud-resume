module "service-api" {
  source   = "./service_api"
  app_name = var.app_name
  project_id = var.project_id
}

module "service-account" {
  source     = "./service_account"
  project_id = var.project_id
  app_name   = var.app_name
  depends_on = [module.service-api]
}

module "storage-bucket" {
  source     = "./storage_bucket"
  app_name   = var.app_name
  project_id = var.project_id
  region     = "us-central1"
  depends_on = [module.service-account]
}

module "firebase" {
  source     = "./firebase"
  app_name   = var.app_name
  project_id = var.project_id
  depends_on = [module.service-api]
  providers = {
    google-beta.main = google-beta.main
    google-beta.no_user_project_override = google-beta.no_user_project_override
  }
}