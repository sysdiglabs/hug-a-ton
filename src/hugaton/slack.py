import os
import json
import urllib3
import emojis


def format_text(receiver, message):
    return [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f":hugging_face: {receiver} got hugged"},
        },
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"{message.capitalize()}"},
        },
    ]


def get_user_info(user):
    # <@id|nombre>
    id, name = user.split("|")
    return id.split("@")[1], name[:-1]


def notify_hug_in_channel(receiver, message):
    url = "https://slack.com/api/chat.postMessage"
    token = os.getenv("SLACK_TOKEN")
    slack_fields = {
        "channel": os.environ["SLACK_KUDOS_CHANNEL"],
        "blocks": json.dumps(format_text(receiver, message)),
    }
    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        url,
        headers={
            "Content-type": "application/json",
            "Authorization": f"Bearer {token}",
        },
        fields=slack_fields,
    )
    return response


def notify(channel_id, message):
    url = "https://slack.com/api/chat.postMessage"
    token = os.getenv("SLACK_TOKEN")
    slack_fields = {
        "channel": channel_id,
        "text": message,
    }
    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        url,
        headers={
            "Content-type": "application/json",
            "Authorization": f"Bearer {token}",
        },
        fields=slack_fields,
    )
    return response
