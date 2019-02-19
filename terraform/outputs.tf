output "command_endpoint" {
  description = "FQDN of the endpoint for the Slack command"
  value       = "https://${aws_route53_record.api.fqdn}"
}
