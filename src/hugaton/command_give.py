import dynamodb
import slack
import pprint


    def command_give(body, receiver, message):

    sender_id = body["user_id"][0]
    sender_name = body["user_name"][0]
    receiver_id, receiver_name = slack.get_user_info(receiver)

    if check_sender_receiver(sender_id, receiver_id):
        return {
            "statusCode": 200,
            "headers": {"Content-type": "application/json"},
            "body": ":no_entry_sign: You can not send shovels to yourself",
        }

    if check_hug_available(sender_id, sender_name):
        return {
            "statusCode": 200,
            "headers": {"Content-type": "application/json"},
            "body": "You ran out of hugs",
        }

    dynamodb.give_hug(sender_id, sender_name, receiver_id, receiver_name, message)
    slack.notify_channel()
    return {
        "statusCode": 200,
        "headers": {"Content-type": "application/json"},
        "body": "Sended",
    }


def check_sender_receiver(sender_id, receiver_id):
    print(f"sender_id: {sender_id}")
    print(f"receiver_id: {receiver_id}")
    return sender_id == receiver_id


def check_hug_available(user_id, user_name):
    hugs_available = dynamodb.hugs_available(user_id, user_name)
    return not hugs_available > 0
