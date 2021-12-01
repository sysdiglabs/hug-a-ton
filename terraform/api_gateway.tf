module "api_gateway" {
  source = "terraform-aws-modules/apigateway-v2/aws"

  name          = "${local.prefix}-slack"
  description   = "Hug-a-ton Slack integration"
  protocol_type = "HTTP"

  cors_configuration = {
    allow_headers = ["content-type", "x-amz-date", "authorization", "x-api-key", "x-amz-security-token", "x-amz-user-agent"]
    allow_methods = ["*"]
    allow_origins = ["*"]
  }

  domain_name                 = "${local.subdomain}.${local.domain_name}"
  domain_name_certificate_arn = local.cert_arn

  default_stage_access_log_destination_arn = aws_cloudwatch_log_group.logs.arn
  default_stage_access_log_format          = "$context.identity.sourceIp - - [$context.requestTime] \"$context.httpMethod $context.routeKey $context.protocol\" $context.status $context.responseLength $context.requestId $context.integrationErrorMessage"

  default_route_settings = {
    detailed_metrics_enabled = true
    throttling_burst_limit   = 100
    throttling_rate_limit    = 100
  }

  integrations = {
    "$default" = {
      lambda_arn = module.lambda_function.lambda_function_arn
    }
  }

  tags = {
    Name = "${local.prefix}-slack-integration"
  }
}

resource "aws_cloudwatch_log_group" "logs" {
  name = "${local.prefix}-api-logs"
}
