def command_give(command):
    return {
        "statusCode": 200,
        "headers": {"Content-type": "application/json"},
        "body": f"give {command} {type(command)} {command.split()}",
    }
