locals {
  prefix      = terraform.workspace == "default" ? "hug-a-ton" : terraform.workspace
  domain_name = "dev.draios.com"
  subdomain   = local.prefix
  cert_arn    = data.sops_file.secrets.data.cert_arn # *.dev.draios.com
  slack_token = data.sops_file.secrets.data.slack_token
}

data "sops_file" "secrets" {
  source_file = "secrets.json"
}
