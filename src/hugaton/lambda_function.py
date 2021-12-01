import base64
import urllib.parse
from command_balance import command_balance
from command_donate import command_donate
from command_give import command_give
from command_help import command_help


def lambda_handler(event, context):
    body = event['body']
    if event['isBase64Encoded']:
        body = base64.b64decode(event['body'])
    body = body.decode('utf-8')
    body = urllib.parse.parse_qs(body)
    return execute_command(body)


def execute_command(body):
    params = body['text'][0].split()
    keyword = params[0]
    if keyword == 'balance':
        return command_balance(params[1:], body)
    elif keyword == 'donate':
        return command_donate(params[1:], body)
    elif keyword.startswith('<@'):
        return command_give(body, keyword, ' '.join(params[1:]))
    else:
        return command_help()
        