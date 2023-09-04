provider "google" {
  project = var.project_id
  region  = "us-central1"
  zone    = "us-central1-a"
}

module "service-api" {
  source   = "./service_api"
  app_name = var.app_name
}

module "service-account" {
  source     = "./service_account"
  project_id = var.project_id
  app_name   = var.app_name
  depends_on = [module.service-api]
}

module "load-balancer" {
  source      = "./load_balancer"
  app_name    = var.app_name
  domain_name = var.domain_name
  depends_on  = [module.service-account]
}

module "storage-bucket" {
  source     = "./storage_bucket"
  app_name   = var.app_name
  region     = "us-central1"
  depends_on = [module.service-account]
}

module "secret-manager" {
  source     = "./secret_manager"
  app_name   = var.app_name
  region     = "us-central1"
  depends_on = [module.service-api]
}

# module "compute-engine" {
#   source     = "./compute_engine"
#   app_name   = var.app_name
#   region     = "us-central1"
#   depends_on = [module.service-api]
# }