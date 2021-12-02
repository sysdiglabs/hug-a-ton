import os
import urllib3


def get_user_info(user):
    # <@id|nombre>
    id, name = user.split("|")
    return id.split("@")[1], name[:-1]


def notify_hug_in_channel(receiver, message):
    url = "https://slack.com/api/chat.postMessage"
    # TODO move it to config and encrypt it
    token = "xoxb-2734598559365-2739893395668-zZ6AXbxzLbQSnxqnddwb6aLK"
    message = {
        "channel": os.environ["SLACK_CHANNEL_ID"],
        "text": f":hugging_face:{receiver} got hugged: *{message.capitalize()}*",
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
    # TODO: check response for errors and return proper feedback to the user
