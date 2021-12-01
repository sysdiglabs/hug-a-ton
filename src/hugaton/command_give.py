def command_give(sender, receiver, message):
    return {
        'statusCode': 200,
        'headers': {'Content-type': 'application/json'},
        'body': f"give {sender} {receiver} {message}"
    }
