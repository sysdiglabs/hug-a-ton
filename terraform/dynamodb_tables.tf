resource "aws_dynamodb_table" "hugs" {
  name           = "hug-a-ton-hugs"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "sender"
  range_key      = "receiver"

  attribute {
    name = "sender"
    type = "S"
  }

  attribute {
    name = "receiver"
    type = "S"
  }

  tags = {
    Name = "hug-a-ton-hugs"
  }
}
