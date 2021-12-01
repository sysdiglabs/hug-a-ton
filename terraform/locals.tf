locals {
  prefix      = terraform.workspace == "default" ? "hug-a-ton" : terraform.workspace
  domain_name = "dev.draios.com"
  subdomain   = local.prefix
  cert_arn    = "arn:aws:acm:us-east-1:059797578166:certificate/0b0aee91-88a7-4bce-9931-c026bcadd213" # *.dev.draios.com
}
