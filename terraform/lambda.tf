module "lambda_function" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "~> 2.0"

  function_name = "${local.prefix}-lambda"
  description   = "Hug-a-ton lambda handler for Slack integration"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.9"

  publish = true

  source_path = "../src/hugaton"
  environment_variables = {
    DYNAMODB_TABLE    = aws_dynamodb_table.hugs.name
    HUGS_PER_MONTH    = 20
    MIN_HUG_TO_DONATE = 50
    # -hugs_ test env
    SLACK_TOKEN         = local.slack_token
    SLACK_KUDOS_CHANNEL = "C02P6RXLQ83"
    SLACK_ADMIN_CHANNEL = "C02P6RXLQ83"
  }

  allowed_triggers = {
    AllowExecutionFromAPIGateway = {
      service    = "apigateway"
      source_arn = "${module.api_gateway.apigatewayv2_api_execution_arn}/*/*"
    }
  }

  attach_policy_json = true
  policy_json        = <<-EOF
      {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": [
              "dynamodb:BatchGetItem",
              "dynamodb:GetItem",
              "dynamodb:Query",
              "dynamodb:Scan",
              "dynamodb:BatchWriteItem",
              "dynamodb:PutItem",
              "dynamodb:UpdateItem"
            ],
            "Resource": "${aws_dynamodb_table.hugs.arn}"
          },
          {
            "Effect": "Allow",
            "Action": [
              "logs:CreateLogStream",
              "logs:PutLogEvents"
            ],
            "Resource": "${aws_cloudwatch_log_group.logs.arn}"
          },
          {
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "*"
          }
        ]
      }
      EOF
}
