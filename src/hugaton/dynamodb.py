def hugs_available(user_id, user_name):
    # TODO
    return 0


def hugs_received(user_id, user_name):
    # TODO
    return 2


def give_hug(sender_id, receiver_id, message):
    # TODO
    pass


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
# print(f"  aaa {type(event)} {event=}")
# table_name = 'AlvarFirstTest'
# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table(table_name)