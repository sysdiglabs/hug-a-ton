def command_donate(params, body):
    if not validate_params(params):
        return {
            'statusCode': 200,
            'headers': {'Content-type': 'application/json'},
            'body': f"Usage: {body['command'][0]} donate <num_hugs> <charity_link>"
        }

    user_id = body["user_id"][0]
    user_name = body["user_name"][0]
    num_hugs = params[0]
    charity_link = params[1]

    return {
        'statusCode': 200,
        'headers': {'Content-type': 'application/json'},
        'body': f"<@{user_id}|{user_name}> has donated {num_hugs} hugs to {charity_link}"
    }


def validate_params(params):
    return len(params) == 2
