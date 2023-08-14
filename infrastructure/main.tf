module "service-api" {
  source     = "./service_api"
  project_id = var.project_id
  app_name   = var.app_name
}

module "service-account" {
  source     = "./service_account"
  project_id = var.project_id
  app_name   = var.app_name
  depends_on = [module.service-api]
}

module "load-balancer" {
  source     = "./load_balancer"
  project_id = var.project_id
  app_name   = var.app_name
  depends_on = [module.service-account]
}