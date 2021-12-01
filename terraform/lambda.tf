module "lambda_function" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "~> 2.0"

  function_name = "hug-a-ton-lambda"
  description   = "Hug-a-ton lambda handler for Slack integration"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.9"

  publish = true

  source_path = "../src/hugaton"

  allowed_triggers = {
    AllowExecutionFromAPIGateway = {
      service    = "apigateway"
      source_arn = "${module.api_gateway.apigatewayv2_api_execution_arn}/*/*"
    }
  }
}
