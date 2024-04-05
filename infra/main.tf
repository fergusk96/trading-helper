terraform {
  required_providers {
    google-beta = {
      source = "hashicorp/google-beta"
      version = "5.23.0"
    }
  }
}

provider "google-beta" {
  credentials = file("~/.gcloud/trading-helper-419411-a1b53c67e2f8.json")
  project = "trading-helper-419411"
}

resource "google_firestore_database" "database" {
  project     = "trading-helper-419411"
  name        = "trading-helper"
  location_id = "us-central1"
  type        = "FIRESTORE_NATIVE"
}
