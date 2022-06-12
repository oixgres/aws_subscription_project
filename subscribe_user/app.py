import json
from urllib import response
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('subscriptions')

def lambda_handler(event, context):

    # Check if the user is already subscribed
    email = table.get_item(
        Key={
            'email': event['email']
        }
    )

    # If the user is already subscribed, finish
    if email:
        res='User are already subscribed'
    # Else, subscribe the user
    else:
        table.put_item(
            Item={
                'email': event['email']
            }
        )
        res = 'User subscribed'

    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }