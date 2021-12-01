from dynamodb import something
from slack import get_userid_from_user
from slack import something
from command_balance import get_hug_available

def command_give(sender, receiver, message):

    if check_sender_receiver(sender, receiver):
        return {
            'statusCode': 200,
            'headers': {'Content-type': 'application/json'},
            'body': ":no_entry_sign: You can not send shovels to yourself"
        }

    if check_hug_available(sender):
        return {
            'statusCode': 200,
            'headers': {'Content-type': 'application/json'},
            'body': "You ran out of hugs"
        }

    return {
        'statusCode': 200,
        'headers': {'Content-type': 'application/json'},
        'body': "Sended"
    }   

def check_sender_receiver(sender, receiver):
    return sender != get_userid_from_user(receiver)

def check_hug_available(sender):
    return False


