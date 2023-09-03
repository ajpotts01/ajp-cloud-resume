#####
# SSL CERT
#####
resource "google_compute_managed_ssl_certificate" "lb_ssl_certificate" {
  #project     = var.project_id
  name        = "${var.app_name}-lb-ssl"
  description = "SSL certificate for load balancer"

  managed {
    # Sticking a www in front of the domain name - this will fix things so
    # both non-www and www URLs work.
    domains = ["www.${var.domain_name}", var.domain_name]
  }
}

#####
# IP/DNS
#####

# Note: if  you use google_compute_address, it won't work with load balancer
resource "google_compute_global_address" "cloud_resume_lb_address" {
  name         = "${var.app_name}-lb-address"
  address_type = "EXTERNAL"
  ip_version   = "IPV4"
}

resource "google_dns_managed_zone" "cloud_resume_dns" {
  name        = "${var.app_name}-dns"
  dns_name    = "${var.domain_name}."
  description = "Cloud Resume DNS Zone"

  labels = {
    created_by = "terraform"
  }
}

resource "google_dns_record_set" "cloud_resume_lb_dns" {
  name         = google_dns_managed_zone.cloud_resume_dns.dns_name
  managed_zone = google_dns_managed_zone.cloud_resume_dns.name

  type = "A"
  ttl  = 300

  rrdatas = [
    google_compute_global_address.cloud_resume_lb_address.address
  ]
}

resource "google_dns_record_set" "cloud_resume_lb_dns_www" {
  name         = "www.${google_dns_managed_zone.cloud_resume_dns.dns_name}"
  managed_zone = google_dns_managed_zone.cloud_resume_dns.name

  type = "A"
  ttl  = 300

  rrdatas = [
    google_compute_global_address.cloud_resume_lb_address.address
  ]
}

#####
# BACKEND ENDPOINT
#####
resource "google_compute_region_network_endpoint_group" "backend_endpoint" {
  name = "${var.app_name}-lb-backend-endpoint"
  #project               = var.project_id
  region                = "us-central1"
  network_endpoint_type = "SERVERLESS"

  cloud_run {
    service = var.app_name
  }
}

# This was created in the UI then ported to TF based on the "equivalent code" output from GCP.
resource "google_compute_backend_service" "backend_service" {
  name = "${var.app_name}-lb-backend-service"
  #project                         = var.project_id
  protocol                        = "HTTPS"
  session_affinity                = "NONE"
  load_balancing_scheme           = "EXTERNAL_MANAGED"
  locality_lb_policy              = "ROUND_ROBIN"
  enable_cdn                      = true
  timeout_sec                     = 30
  connection_draining_timeout_sec = 0
  compression_mode                = "DISABLED"

  log_config {
    enable = false
  }

  cdn_policy {
    cache_key_policy {
      include_host         = true
      include_protocol     = true
      include_query_string = true
    }
    cache_mode        = "CACHE_ALL_STATIC"
    client_ttl        = 3600
    default_ttl       = 3600
    max_ttl           = 86400
    negative_caching  = false
    serve_while_stale = 0
  }

  backend {
    balancing_mode = "UTILIZATION"
    group          = google_compute_region_network_endpoint_group.backend_endpoint.id
  }
}

#####
# PROXIES
#####

resource "google_compute_url_map" "frontend_redirect" {
  #project     = var.project_id
  name        = "${var.app_name}-https-lb-frontend-redirect"
  description = "HTTP to HTTPS redirect for the ${var.app_name}-lb-frontend forwarding rule"

  default_url_redirect {
    https_redirect         = true
    redirect_response_code = "MOVED_PERMANENTLY_DEFAULT"
    strip_query            = false
  }
}

resource "google_compute_url_map" "backend_redirect" {
  name            = "${var.app_name}-https-lb-backend-redirect"
  default_service = google_compute_backend_service.backend_service.id
}

resource "google_compute_target_http_proxy" "default" {
  name    = "${var.app_name}-http-proxy"
  url_map = google_compute_url_map.backend_redirect.id
}

resource "google_compute_target_https_proxy" "target_proxy" {
  name             = "${var.app_name}-lb-target-proxy"
  quic_override    = "NONE"
  ssl_certificates = [google_compute_managed_ssl_certificate.lb_ssl_certificate.name]
  url_map          = google_compute_url_map.backend_redirect.id
}

#####
# FORWARDING
#####
resource "google_compute_global_forwarding_rule" "forwarding_http" {
  #project               = var.project_id
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

resource "google_compute_global_forwarding_rule" "forwarding_https" {
  #project               = var.project_id
  name                  = "${var.app_name}-lb-frontend-forwarding-rule-https"
  ip_address            = google_compute_global_address.cloud_resume_lb_address.id
  port_range            = "443"
  ip_protocol           = "TCP"
  load_balancing_scheme = "EXTERNAL_MANAGED"
  target                = google_compute_target_https_proxy.target_proxy.id

  labels = {
    created_by = "terraform"
  }
}