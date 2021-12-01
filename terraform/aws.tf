provider "aws" {
  region = "us-east-1"
  ignore_tags {
    keys = ["AutoTag_Creator"]
  }
  
  # Make it faster by skipping something
  skip_get_ec2_platforms      = true
  skip_metadata_api_check     = true
  skip_region_validation      = true
  skip_credentials_validation = true

  # skip_requesting_account_id should be disabled to generate valid ARN in apigatewayv2_api_execution_arn
  skip_requesting_account_id = false
}

terraform {
  backend "s3" {
    bucket         = "hug-a-ton"
    key            = "terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "qa-tf-shared-backend-lock"
  }
}
