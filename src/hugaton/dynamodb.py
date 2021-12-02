import boto3
import os
import datetime
import uuid
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Attr

###### Doc schema
# Table of hugs
# {
#  timestamp: string
#  sender_name: string
#  sender_id: string
#  receiver_name: string
#  receiver_id: string
#  message: string
#  spent: boolean
# }
#
# Table of donations
# {
#  transaction_id: string
#  timestamp: string
#  donator_name: string
#  donator_id: string
#  amount: number
#  destination: string
# }
########################

# https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html
dynamodb = boto3.resource("dynamodb")


def hugs_available(user_id, user_name):
    table = dynamodb.Table(
        os.getenv("DYNAMODB_HUG_TABLE", "aws_dynamodb_table.hugs.name")
    )
    response = table.query(KeyConditionExpression=Key("sender_id").eq(user_id))
    # TODO: Filter this in DB to improve performance
    hugs_given_this_month = [
        item
        for item in response["Items"]
        if is_hug_given_this_month(item, datetime.datetime.utcnow())
    ]
    hug_per_month = int(os.getenv("HUGS_PER_MONTH", 20))

    return hug_per_month - len(hugs_given_this_month)


def hugs_received(user_id, user_name):
    table = dynamodb.Table(
        os.getenv("DYNAMODB_HUG_TABLE", "aws_dynamodb_table.hugs.name")
    )
    # TODO: Add index into "receiver_id" and change scan for query
    scan_kwargs = {
        "FilterExpression": Key("receiver_id").eq(user_id),
        "ProjectionExpression": "receiver_id, spent",
    }

    done = False
    start_key = None
    hugs_not_spent = 0
    while not done:
        if start_key:
            scan_kwargs["ExclusiveStartKey"] = start_key
        response = table.scan(**scan_kwargs)
        hugs_not_spent += len(
            [item for item in response["Items"] if not is_hug_spent(item)]
        )
        start_key = response.get("LastEvaluatedKey", None)
        done = start_key is None

    return hugs_not_spent


def give_hug(sender_id, sender_name, receiver_id, receiver_name, message):
    table = dynamodb.Table(
        os.getenv("DYNAMODB_HUG_TABLE", "aws_dynamodb_table.hugs.name")
    )
    table.put_item(
        Item={
            "timestamp": str(datetime.datetime.utcnow()),
            "sender_name": sender_name,
            "sender_id": sender_id,
            "receiver_name": receiver_name,
            "receiver_id": receiver_id,
            "message": message,
            "spent": False,
        }
    )


def is_hug_given_this_month(hug, now):
    when = datetime.datetime.fromisoformat(hug["timestamp"])
    return when.year == now.year and when.month == now.month


def is_hug_spent(hug):
    return hug["spent"]


def donate(donator_id, donator_name, amount, charity_link):
    table = dynamodb.Table(
        os.getenv("DYNAMODB_DONATIONS_TABLE", "aws_dynamodb_table.donations.name")
    )
    transaction_id = str(uuid.uuid1())
    table.put_item(
        Item={
            "transaction_id": transaction_id,
            "timestamp": str(datetime.datetime.utcnow()),
            "donator_name": donator_name,
            "donator_id": donator_id,
            "amount": amount,
            "destination": charity_link,
        }
    )
    mark_received_hugs_as_spent(donator_id, donator_name, amount)
    return transaction_id


def mark_received_hugs_as_spent(receiver_id, receiver_name, amount):
    table = dynamodb.Table(
        os.getenv("DYNAMODB_HUG_TABLE", "aws_dynamodb_table.hugs.name")
    )
    # TODO: Add index into "receiver_id" and change scan for query
    scan_kwargs = {
        "FilterExpression": Key("receiver_id").eq(receiver_id),
    }

    hugs_spent = 0
    start_key = None

    while hugs_spent < amount:
        if start_key:
            scan_kwargs["ExclusiveStartKey"] = start_key
        response = table.scan(**scan_kwargs)
        hugs_to_spend = [item for item in response["Items"] if not is_hug_spent(item)]
        for hug in hugs_to_spend:
            if hugs_spent >= amount:
                return
            table.update_item(
                Key={"sender_id": hug["sender_id"], "timestamp": hug["timestamp"]},
                UpdateExpression="SET spent = :val1",
                ExpressionAttributeValues={":val1": True},
            )
            hugs_spent += 1

        start_key = response.get("LastEvaluatedKey", None)
