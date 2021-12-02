import os
import urllib3
import emojis


def get_user_info(user):
    # <@id|nombre>
    id, name = user.split("|")
    return id.split("@")[1], name[:-1]


def notify_hug_in_channel(receiver, message):
    url = "https://slack.com/api/chat.postMessage"
    token = os.environ['SLACK_TOKEN']
    message = {
        "channel": os.environ["SLACK_CHANNEL_ID"],
        "text": f"{emojis.hugging_face} {receiver} got hugged: *{message.capitalize()}*",
    }
    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        url,
        headers={
            "Content-type": "application/json",
            "Authorization": f"Bearer {token}",
        },
        fields=message,
    )
    return response

