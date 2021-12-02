locals {
  prefix      = terraform.workspace == "default" ? "hug-a-ton" : terraform.workspace
  domain_name = var.domain_name
  subdomain   = local.prefix
  cert_arn    = sensitive(var.cert_arn)
  slack_token = sensitive(var.slack_token)
}
