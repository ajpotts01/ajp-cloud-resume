module "service-api" {
  source     = "./service_api"
  project_id = var.project_id
}

module "service-account" {
  source     = "./service_account"
  project_id = var.project_id
  depends_on = [module.service-api]
}