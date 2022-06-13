import json
import re
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('subscriptions')

def lambda_handler(event, context):

    try:
        email=event['queryStringParameters']['email']

        # Check if email has format (regex)
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            res={'res':'Email syntax is wrong', 'error':'error'}
        else:
            try:
                table.put_item(
                    Item={
                        'email':email
                    },
                    ConditionExpression="attribute_not_exists(email)"
                )
                res={'res': 'User has been subscribed'}
            except:
                res={'res': 'User was already subscribed', 'error':'error'}

        return {
            'statusCode': 200,
            'body': json.dumps(res)
        }
    except:
        return {
            'statusCode': 500,
            'body': json.dumps({'res':'Request failed', 'error':'error'})
        }