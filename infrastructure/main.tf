provider "google" {
  project = var.project_id
  region  = "australia-southeast1"
  zone    = "australia-southeast1-a"
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