variable "project_id" {
  description = "Target project ID"
  type        = string
}

variable "app_name" {
  description = "Name of the app - prefix for every resource"
  type        = string
}

variable "domain_name" {
  description = "Domain name for your application/load balancer"
  type        = string
}