import json
       
        
HELP_MESSAGE = \
{
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":wave: *Welcome to Hug-a-ton*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Use this command to share love & appreciation with your coworkers"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Give a hug*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Somebody helped you out? Have you seen an awesome contribution? Just sent a hug to a coworker with:```/hug @john.doe [message]```"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "An anonimous message will be posted to #-hugs_ with your message tagging the _hugee_"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Check your balance*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Wanna know the hugs you have available to give or the hugs you've received? Use:```/hug balance```"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "You'll get a private messsage with your balance"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Pay it forward*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Got enough hugs from your cowokers? Share the love outside Sysdig with:```/hug donate [quantity] [charity_link]```"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "A message will be post to #-hugs_ with about the donation and HR will reach out to proceed with the donation."
			}
		}
	]
}


def command_help():
    return {
        'statusCode': 200,
        'headers': {'Content-type': 'application/json'},
        'body': json.dumps(HELP_MESSAGE)
    }
