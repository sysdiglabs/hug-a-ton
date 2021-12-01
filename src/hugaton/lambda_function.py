import base64
import json
import boto3
from botocore.exceptions import ClientError
import pprint
import urllib.parse
from command_balance import command_balance
from command_donate import command_donate
from command_give import command_give
from command_help import command_help


# https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html

def lambda_handler(event, context):
    print(f"  aaa {type(event)} {event=}")
    table_name = 'AlvarFirstTest'
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    body = event['body']
    if event['isBase64Encoded']:
        body = base64.b64decode(event['body'])
    body = body.decode('utf-8')
    body = urllib.parse.parse_qs(body)
    print(body)
    validate_command(body)
    return execute_command(body)


def validate_command(body):
    command = body['command'][0]
    if command != '/hug':
        raise RuntimeError("We got an unexpected command: %s", command)


def execute_command(body):
    params = body['text'][0].split()
    keyword = params[0]
    if keyword == 'balance':
        return command_balance(params[1:], body)
    elif keyword == 'donate':
        return command_donate(params[1:], body)
    elif keyword.startswith('<@'):
        return command_give(body['user_id'], keyword, ' '.join(params[1:]))
    else:
        return command_help()
