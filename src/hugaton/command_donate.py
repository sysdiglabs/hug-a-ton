import os

import dynamodb
import slack


def command_donate(params, body):
    if not validate_params(params):
        message = (f"Usage: {body['command'][0]} donate <num_hugs> <charity_link>",)
    else:
        user_id = body["user_id"][0]
        user_name = body["user_name"][0]
        num_hugs = params[0]
        charity_link = params[1]
        min_hub_to_donate = int(os.getenv("MIN_HUG_TO_DONATE", 50))
        slack_admin_channel = int(os.getenv("SLACK_ADMIN_CHANNEL", "12345"))
        slack_kudos_channel = int(os.getenv("SLACK_KUDOS_CHANNEL", "12346"))
        message = {"blocks": []}
        hugs_received = dynamodb.hugs_received(body["user_id"][0], body["user_name"][0])
        if hugs_received < min_hub_to_donate:
            message["blocks"] = less_than_min_hugs_available_block(
                hugs_received, min_hub_to_donate
            )
        elif num_hugs < hugs_received:
            message["blocks"] = less_than_hugs_available_block(num_hugs, hugs_received)
        else:
            message = f"<@{user_id}|{user_name}> has donated {num_hugs} hugs to {charity_link}"
            slack.notify_channel(message, slack_admin_channel)
            slack.notify_channel(message, slack_kudos_channel)
    return {
        "statusCode": 200,
        "headers": {"Content-type": "application/json"},
        "body": message,
    }


def validate_params(params):
    return len(params) == 2


def less_than_hugs_available_block(num_hugs, hugs_received):
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f":sad_panda: *You only have received {hugs_received} hugs. You can not donate {num_hugs}, as it is bigger*",
            },
        },
    ]


def less_than_min_hugs_available_block(num_hugs, min_hub_to_donate):
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f":sad_panda: *You only have received {num_hugs} hugs, and min required is {min_hub_to_donate}*",
            },
        },
    ]
