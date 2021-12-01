def command_donate(params, body):
    return {
        'statusCode': 200,
        'headers': {'Content-type': 'application/json'},
        'body': "20 hubs donated"
    }
