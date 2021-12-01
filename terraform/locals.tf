locals {
  domain_name = "dev.draios.com"
  subdomain   = var.prefix
  cert_arn    = "arn:aws:acm:us-east-1:059797578166:certificate/0b0aee91-88a7-4bce-9931-c026bcadd213" # *.dev.draios.com
}
