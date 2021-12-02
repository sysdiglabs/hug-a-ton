import os
import urllib3
import emojis


def get_user_info(user):
    # <@id|nombre>
    id, name = user.split("|")
    return id.split("@")[1], name[:-1]


def notify_hug_in_channel(receiver, message):
    channel = os.getenv("SLACK_KUDOS_CHANNEL", "C02P6RXLQ83")
    text = f"{emojis.hugging_face} {receiver} got hugged: *{message.capitalize()}*"
    notify(channel, text)


def notify(channel_id, message):
    url = "https://slack.com/api/chat.postMessage"
    token = os.getenv[
        "SLACK_TOKEN", "xoxb-2734598559365-2739893395668-zZ6AXbxzLbQSnxqnddwb6aLK"
    ]
    fields = {
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
        fields=fields,
    )
    return response
