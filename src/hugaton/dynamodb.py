import boto3
import os
import datetime

###### Doc schema
#{
#  timestamp: string
#  sender_name: string
#  sender_id: string
#  receiver_name: string
#  receiver_id: string
#  message: string
#  spent: boolean
#}
########################

# https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])


def hugs_available(user_id, user_name):
    # TODO
    return 1


def hugs_received(user_id, user_name):
    # TODO
    return 2


def give_hug(sender_id, sender_name, receiver_id, receiver_name, message):
    table.put_item(
        Item={
            'timestamp': str(datetime.datetime.utcnow()),
            'sender_name': sender_name,
            'sender_id': sender_id,
            'receiver_name': receiver_name,
            'receiver_id': receiver_id,
            'message': message,
            'spent': False
        }
    )
