#####
# NOTE:
# This is only for use if you want to run Postgres for cheap.
# 
#####

resource "google_compute_address" "app_database_server_address" {
  name         = "${var.app_name}-db-server-address"
  address_type = "EXTERNAL"
  ip_version   = "IPV4"
  region = var.region
}

resource "google_compute_instance" "app_database_server" {
  name         = "${var.app_name}-db-server"
  machine_type = "e2.micro" # Free tier in us-central1
  zone         = "${var.region}-a"

  # This disk config + e2.micro + us-central1-a should qualify for free tier
  boot_disk {
    initialize_params {
      size  = 30
      image = "ubuntu-os-cloud/ubuntu-2004-lts"
      type  = "pd-standard"
    }
  }

  network_interface {
    network = "default"
    access_config {
      nat_ip = google_compute_address.app_database_server_address.address
    }
  }
}