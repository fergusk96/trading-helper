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

# Create a Pub/Sub topic for Cloud Scheduler
resource "google_pubsub_topic" "scheduler_topic" {
  project     = "trading-helper-419411"
  name = "scheduler-topic"
}

# Create a Cloud Scheduler job to publish to the scheduler-topic
resource "google_cloud_scheduler_job" "job" {
  project     = "trading-helper-419411"
  region      = "us-central1"
  name        = "trigger-publish-event"
  description = "Job to publish message to Pub/Sub topic"
  schedule    = "*/15 * * * *"
  time_zone   = "UTC"

  pubsub_target {
    topic_name = google_pubsub_topic.scheduler_topic.id
    data       = base64encode("{\"message\":\"Hello, World!\"}")
  }
}
