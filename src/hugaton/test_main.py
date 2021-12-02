from unittest import mock

import pytest

import dynamodb
from lambda_function import lambda_handler, execute_command


class mockTable:
    def query(*args, **kwords):
        return {"Items": []}

    def put_item(*args, **kwords):
        return


HELP_EVENT = {
    "version": "2.0",
    "routeKey": "ANY /AlvarL1",
    "rawPath": "/default/AlvarL1",
    "rawQueryString": "",
    "headers": {
        "accept": "application/json,*/*",
        "accept-encoding": "gzip,deflate",
        "content-length": "436",
        "content-type": "application/x-www-form-urlencoded",
        "host": "q4tn2nao5e.execute-api.us-east-1.amazonaws.com",
        "user-agent": "Slackbot 1.0 (+https://api.slack.com/robots)",
        "x-amzn-trace-id": "Root=1-61a78c64-0b228a010f22f11026f1cd43",
        "x-forwarded-for": "3.95.131.167",
        "x-forwarded-port": "443",
        "x-forwarded-proto": "https",
        "x-slack-request-timestamp": "1638370404",
        "x-slack-signature": "v0=b4a792d8368a0f50a88973ed1c1f3e5d4cc69179f66f50d0a6757f90ff76ccbb",
    },
    "requestContext": {
        "accountId": "059797578166",
        "apiId": "q4tn2nao5e",
        "domainName": "q4tn2nao5e.execute-api.us-east-1.amazonaws.com",
        "domainPrefix": "q4tn2nao5e",
        "http": {
            "method": "POST",
            "path": "/default/AlvarL1",
            "protocol": "HTTP/1.1",
            "sourceIp": "3.95.131.167",
            "userAgent": "Slackbot 1.0 (+https://api.slack.com/robots)",
        },
        "requestId": "JrLfwi_9IAMEPjw=",
        "routeKey": "ANY /AlvarL1",
        "stage": "default",
        "time": "01/Dec/2021:14:53:24 +0000",
        "timeEpoch": 1638370404644,
    },
    "body": "dG9rZW49cXlzRUFnSUtQY3FNelJQa2FHVGRYV2ZaJnRlYW1faWQ9VDAyTUxITEdGQVImdGVhbV9kb21haW49YWx2YXJ0ZXN0aW5nd29ya3NwYWNlJmNoYW5uZWxfaWQ9RDAyUDRCRTEzOTgmY2hhbm5lbF9uYW1lPWRpcmVjdG1lc3NhZ2UmdXNlcl9pZD1VMDJQNEM4MzQxMSZ1c2VyX25hbWU9YW5nZWwuYmxhc2NvJmNvbW1hbmQ9JTJGaHVnJnRleHQ9aGVscCZhcGlfYXBwX2lkPUEwMk04U1o5UlBIJmlzX2VudGVycHJpc2VfaW5zdGFsbD1mYWxzZSZyZXNwb25zZV91cmw9aHR0cHMlM0ElMkYlMkZob29rcy5zbGFjay5jb20lMkZjb21tYW5kcyUyRlQwMk1MSExHRkFSJTJGMjc4Nzc4MDk0MjI5MSUyRkR2cXU1WFVLRGlpVDdtRHc5TlFiMnZhdCZ0cmlnZ2VyX2lkPTI3ODEwNTc2Mjc1NDIuMjczNDU5ODU1OTM2NS42M2U1YTFmZWYzODg4Y2M4ZjFiM2Q4ZmM2ZGEzOTZhYQ==",
    "isBase64Encoded": True,
}

HELP_RESPONSE = {
    "statusCode": 200,
    "headers": {"Content-type": "application/json"},
    "body": '{"blocks": [{"type": "section", "text": {"type": "mrkdwn", "text": ":wave: *Welcome to Hug-a-ton*"}}, {"type": "section", "text": {"type": "mrkdwn", "text": "Use this command to share love & appreciation with your coworkers"}}, {"type": "section", "text": {"type": "mrkdwn", "text": "*Give a hug*"}}, {"type": "section", "text": {"type": "mrkdwn", "text": "Somebody helped you out? Have you seen an awesome contribution? Just sent a hug to a coworker with:```/hug @john.doe [message]```"}}, {"type": "section", "text": {"type": "mrkdwn", "text": "An anonimous message will be posted to #-hugs_ with your message tagging the _hugee_"}}, {"type": "section", "text": {"type": "mrkdwn", "text": "*Check your balance*"}}, {"type": "section", "text": {"type": "mrkdwn", "text": "Wanna know the hugs you have available to give or the hugs you\'ve received? Use:```/hug balance```"}}, {"type": "section", "text": {"type": "mrkdwn", "text": "You\'ll get a private messsage with your balance"}}, {"type": "section", "text": {"type": "mrkdwn", "text": "*Pay it forward*"}}, {"type": "section", "text": {"type": "mrkdwn", "text": "Got enough hugs from your cowokers? Share the love outside Sysdig with:```/hug donate [quantity] [charity_link]```"}}, {"type": "section", "text": {"type": "mrkdwn", "text": "A message will be post to #-hugs_ with about the donation and HR will reach out to proceed with the donation."}}]}',
}


def test_command_decode():
    r = lambda_handler(HELP_EVENT, context="")
    assert r == HELP_RESPONSE


BODY = {
    "token": ["qysEAgIKPcqMzRPkaGTdXWfZ"],
    "team_id": ["T02MLHLGFAR"],
    "team_domain": ["alvartestingworkspace"],
    "channel_id": ["C02M8SNFCBH"],
    "channel_name": ["general"],
    "user_id": ["U02P3MKFSEQ"],
    "user_name": ["jorge.maroto"],
    "command": ["/hug"],
    "text": ["foo bar"],
    "api_app_id": ["A02M8SZ9RPH"],
    "is_enterprise_install": ["false"],
    "response_url": [
        "https://hooks.slack.com/commands/T02MLHLGFAR/2772185740519/AlO1wICrdSygOWaOwZt0Qb0p"
    ],
    "trigger_id": ["2780128633110.2734598559365.54c2941fa85ac26ccd49961d5b4626a5"],
}

BALANCE_RESPONSE = {
    "statusCode": 200,
    "headers": {"Content-type": "application/json"},
    "body": '{"blocks": [{"type": "section", "text": {"type": "mrkdwn", "text": ":hugging_face: *20 hugs available*"}}, {"type": "section", "text": {"type": "mrkdwn", "text": "Hug away! Remember hugs are reset at the beginning of the month"}}, {"type": "section", "text": {"type": "mrkdwn", "text": ":sad_panda: *No hugs received yet*"}}, {"type": "section", "text": {"type": "mrkdwn", "text": "Don\'t give up! Keep trying, soon your effort will be recognized!"}}]}',
}
DONATE_RESPONSE = {
    "statusCode": 200,
    "headers": {"Content-type": "application/json"},
    "body": {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":sad_panda: *You only have received 0 hugs, and min required is 50*",
                },
            }
        ]
    },
}
GIVE_RESPONSE = {
    "statusCode": 200,
    "headers": {"Content-type": "application/json"},
    "body": ":hugging-face: Hug successfully sent!",
}


@pytest.mark.parametrize(
    "text, response",
    [
        pytest.param(
            "<@U02NYLASM52|andres.fuentes> He helps me too much",
            GIVE_RESPONSE,
            id="give",
        ),
        pytest.param("balance foo bar", BALANCE_RESPONSE, id="balance"),
        pytest.param("donate foo bar", DONATE_RESPONSE, id="donate"),
        pytest.param("help", HELP_RESPONSE, id="help"),
    ],
)
@mock.patch("dynamodb.table", mockTable)
def test_parse_command(text, response, mocker):
    body = BODY
    body["text"] = [f"{text}"]
    assert execute_command(body) == response
