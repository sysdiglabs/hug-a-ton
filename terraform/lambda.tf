module "lambda_function" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "~> 2.0"

  function_name = "${var.prefix}-lambda"
  description   = "Hug-a-ton lambda handler for Slack integration"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.9"

  publish = true

  source_path = "../src/hugaton"
  environment_variables = {
    DYNAMODB_TABLE = aws_dynamodb_table.hugs.name
  }

  allowed_triggers = {
    AllowExecutionFromAPIGateway = {
      service    = "apigateway"
      source_arn = "${module.api_gateway.apigatewayv2_api_execution_arn}/*/*"
    }
  }

  attach_policy_json = true
  policy_json = <<-EOF
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
