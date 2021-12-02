locals {
  prefix      = terraform.workspace == "default" ? "hug-a-ton" : terraform.workspace
  domain_name = var.domain_name
  subdomain   = local.prefix
}
