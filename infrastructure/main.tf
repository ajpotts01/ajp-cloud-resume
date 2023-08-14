module "service-apis" {
  source     = "./service_apis"
  project_id = var.project_id
}

module "service-accounts" {
  source     = "./service_accounts"
  project_id = var.project_id
  depends_on = [module.service-apis]
}