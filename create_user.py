import json
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        first_name = body.get('first_name')
        age = body.get('age')

        if not first_name or not age:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'first_name and age are required'})
            }

        user_id = str(uuid.uuid4())
        item = {
            'user_id': user_id,
            'first_name': first_name,
            'age': int(age)
        }
        table.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': json.dumps({'user_id': user_id})
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }