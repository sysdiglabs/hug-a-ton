variable "slack_token" {
  description = "Slack API token"
}
variable "domain_name" {
  default     = "dev.draios.com"
  description = "Domain zone for API gateway"
}
variable "cert_arn" {
  description = "AMC certificate ARN for the API gateway"
}
variable "kudos_channel" {
  description = "Slack channel to post hugs and donations"
}
variable "admin_channel" {
  description = "Slack channel to post only donations"
}
