variable "app_name" {
  description = "Name of the app - prefix for every resource"
  type        = string
}

variable "region" {
  description = "Region to create buckets in"
  type        = string
}

variable "project_id" {
  description = "Target project ID"
  type        = string
}