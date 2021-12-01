import base64
import urllib.parse
from command_balance import command_balance
from command_donate import command_donate
from command_give import command_give
from command_help import command_help

#https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html


def lambda_handler(event, context):
    body = event['body']
    if event['isBase64Encoded']:
         body = base64.b64decode(event['body'])
    body = body.decode('utf-8')
    body = urllib.parse.parse_qs(body)
    validate_command(body)
    
    return parse_command(body)


def validate_command(body):
    command = body['command'][0]
    if command != '/hug':
        raise RuntimeError("We got an unexpected command: %s", command)


def parse_command(body):
    command = body['text'][0]
    if command == 'help':
    	return command_help()
    elif command == 'balance':
    	return command_balance(command)
    elif command.startswith('donate'):
    	return command_donate(command)
    elif command.startswith('<@'):
    	return command_give(command)
    else:
        return {
            'statusCode': 200,
            'body': f":wave: unknown command {command}"
        }
        
