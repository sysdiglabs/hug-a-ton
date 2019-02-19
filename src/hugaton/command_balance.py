import dynamodb
import json
import emojis


def command_balance(_, body):
    hugs_available = dynamodb.hugs_available(body["user_id"][0], body["user_name"][0])
    hugs_received = dynamodb.hugs_received(body["user_id"][0], body["user_name"][0])

    message = format_message(hugs_available, hugs_received)
    return {
        "statusCode": 200,
        "headers": {"Content-type": "application/json"},
        "body": json.dumps(message),
    }


def format_message(hugs_available, hugs_received):
    message = {"blocks": []}
    if hugs_available > 0:
        message["blocks"] += hugs_available_block(hugs_available)
    else:
        message["blocks"] += no_hugs_available_block()

    if hugs_received > 0:
        message["blocks"] += hugs_received_block(hugs_received)
    else:
        message["blocks"] += no_hugs_received_block()
    return message


def hugs_available_block(hugs):
    if hugs == 1:
        hugs_text = f"{hugs} hug"
    else:
        hugs_text = f"{hugs} hugs"
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"{emojis.hugging_face} *{hugs_text} available*",
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Hug away! Remember hugs are reset at the beginning of the month",
            },
        },
    ]


def no_hugs_available_block():
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"{emojis.sad_face} *No hugs available*",
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Don't get too sad, new hugs are delivered every month!",
            },
        },
    ]


def hugs_received_block(hugs):
    if hugs == 1:
        hugs_text = f"{hugs} hug"
    else:
        hugs_text = f"{hugs} hugs"
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"{emojis.party} *{hugs_text} received*",
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Your teammates are recognizing your contributions! Keep up the great work!",
            },
        },
    ]


def no_hugs_received_block():
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"{emojis.sad_face} *No hugs received yet*",
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Don't give up! Keep trying, soon your effort will be recognized!",
            },
        },
    ]
