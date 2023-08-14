#####
# IP/DNS
#####

# Note: if  you use google_compute_address, it won't work with load balancer
resource "google_compute_global_address" "cloud_resume_lb_address" {
  name         = "${var.app_name}-lb-address"
  address_type = "EXTERNAL"
  ip_version   = "IPV4"
  project      = var.project_id
}

resource "google_dns_managed_zone" "cloud_resume_dns" {
  name        = "${var.app_name}-dns"
  dns_name    = "ajpcloudblog.com." # TODO: Turn into var
  description = "Cloud Resume DNS Zone"
  project     = var.project_id

  labels = {
    created_by = "terraform"
  }
}

#####
# BACKEND ENDPOINT
#####
resource "google_compute_region_network_endpoint_group" "backend_endpoint" {
  name                  = "${var.app_name}-lb-backend-endpoint"
  region                = "australia-southeast1"
  network_endpoint_type = "SERVERLESS"

  cloud_run {
    service = var.app_name
  }
}

# This was created in the UI then ported to TF based on the "equivalent code" output from GCP.
resource "google_compute_backend_service" "backend_service" {
  name                            = "${var.app_name}-lb-backend-service"
  enable_cdn                      = true
  timeout_sec                     = 10
  connection_draining_timeout_sec = 10

  backend {
    balancing_mode = "UTILIZATION"
    group          = google_compute_region_network_endpoint_group.backend_endpoint.id
  }
}

#####
# FORWARDING/PROXIES
#####

resource "google_compute_url_map" "https_redirect" {
  project     = var.project
  name        = "${var.app_name}-https-lb-frontend-redirect"
  description = "HTTP to HTTPS redirect for the ${var.app_name}-lb-frontend forwarding rule"

  default_url_redirect {
    https_redirect         = true
    redirect_response_code = "MOVED_PERMANENTLY_DEFAULT"
    strip_query            = false
  }
}

resource "google_compute_target_http_proxy" "default" {
  project = var.project
  name    = "${var.app_name}-http-proxy"
  url_map = google_compute_url_map.https_redirect.id
}

# This needs a target.
resource "google_compute_global_forwarding_rule" "forwarding_http" {
  project               = var.project_id
  name                  = "${var.app_name}-lb-frontend-forwarding-rule-http"
  ip_address            = google_compute_global_address.cloud_resume_lb_address.id
  port_range            = "80"
  ip_protocol           = "TCP"
  load_balancing_scheme = "EXTERNAL_MANAGED"
  target                = google_compute_target_http_proxy.default.id

  labels = {
    created_by = "terraform"
  }
}