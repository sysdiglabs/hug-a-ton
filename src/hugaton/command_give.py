import dynamodb
import slack
import emojis


def command_give(body, receiver, message):

    sender_id = body["user_id"][0]
    sender_name = body["user_name"][0]
    receiver_id, receiver_name = slack.get_user_info(receiver)

    if check_sender_receiver(sender_id, receiver_id):
        response = f"{emojis.forbidden} You can not hug yourself"
    elif check_hug_available(sender_id, sender_name):
        response = f"{emojis.zero} No hugs available"
    elif not message:
        response = "Please add a message to your hug!"
    else:
        dynamodb.give_hug(sender_id, sender_name, receiver_id, receiver_name, message)
        slack.notify_hug_in_channel(receiver, message)
        hugs_left = dynamodb.hugs_available(sender_id, sender_name)
        if hugs_left == 1:
            hug_text = f"{hugs_left} hug"
        else:
            hug_text = f"{hugs_left} hugs"

        response = f"{emojis.hugging_face} Hug successfully sent!. You have {hug_text} left"
    return {
        "statusCode": 200,
        "headers": {"Content-type": "application/json"},
        "body": response,
    }


def check_sender_receiver(sender_id, receiver_id):
    return sender_id == receiver_id


def check_hug_available(user_id, user_name):
    hugs_available = dynamodb.hugs_available(user_id, user_name)
    return not hugs_available > 0
