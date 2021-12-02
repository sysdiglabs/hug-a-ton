import json
import os
import emojis
import dynamodb
import slack
from exception import SysdigException


def hubs_received(body):
    return dynamodb.hugs_received(body["user_id"][0], body["user_name"][0])


def command_donate(params, body):
    if not validate_params(params):
        message = f"Usage: {body['command'][0]} donate <num_hugs> <charity_link>"
    else:
        user_id = body["user_id"][0]
        user_name = body["user_name"][0]
        try:
            num_hugs = int(params[0])
        except ValueError as exc:
            raise SysdigException(
                f"{emojis.forbidden} Number of hugs should be an integer. Current value = {params[0]}"
            )

        charity_link = params[1]
        min_hub_to_donate = int(os.getenv("MIN_HUG_TO_DONATE", "50"))
        slack_admin_channel = os.getenv("SLACK_ADMIN_CHANNEL", "U02P4C83411")
        slack_kudos_channel = os.getenv("SLACK_KUDOS_CHANNEL", "C02P6RXLQ83")
        hugs_received = hubs_received(body)
        if num_hugs < min_hub_to_donate:
            message = less_than_min_hugs_available_block(num_hugs, min_hub_to_donate)
        elif num_hugs > hugs_received:
            message = less_than_hugs_available_block(num_hugs, hugs_received)
        else:
            public_message = f"{emojis.tada} <@{user_id}|{user_name}> has donated {num_hugs} hugs to {charity_link}"
            slack.notify(slack_admin_channel, public_message)
            slack.notify(slack_kudos_channel, public_message)
            dynamodb.update_hugs(user_id, user_name, num_hugs)
            message = (
                f"{emojis.tada} You have donated {num_hugs} hugs to {charity_link}"
            )
    return {
        "statusCode": 200,
        "headers": {"Content-type": "application/json"},
        "body": message,
    }


def validate_params(params):
    return len(params) == 2


def less_than_hugs_available_block(num_hugs, hugs_received):
    return json.dumps(
        {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"{emojis.sad_face} *You only have received {hugs_received} hugs. You can not donate {num_hugs}, as it is bigger*",
                    },
                },
            ]
        }
    )


def less_than_min_hugs_available_block(num_hugs, min_hub_to_donate):
    return json.dumps(
        {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"{emojis.sad_face} *You want to donate {num_hugs} hugs, but min required is {min_hub_to_donate}*",
                    },
                },
            ]
        }
    )
