import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('subscriptions')

def lambda_handler(event, context):

    print(table.creation_date_time)

    print(event)
    return {
        'statusCode': 200,
    }