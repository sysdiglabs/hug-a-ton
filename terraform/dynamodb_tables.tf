resource "aws_dynamodb_table" "hugs" {
  name           = "${local.prefix}-hugs"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "sender_id"
  range_key      = "timestamp"

  attribute {
    name = "sender_id"
    type = "S"
  }

  attribute {
    name = "timestamp"
    type = "S"
  }

  tags = {
    Name = "${local.prefix}-hugs"
  }
}

resource "aws_dynamodb_table" "donations" {
  name           = "${local.prefix}-donations"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "transaction_id"
  range_key      = "timestamp"

  attribute {
    name = "transaction_id"
    type = "S"
  }

  attribute {
    name = "timestamp"
    type = "S"
  }

  tags = {
    Name = "${local.prefix}-donations"
  }
}
