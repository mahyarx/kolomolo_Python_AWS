import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

# Custom encoder for Decimal
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            if obj % 1 == 0:
                return int(obj)
            else:
                return float(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    print("EVENT RECEIVED:")
    print(json.dumps(event))

    path_params = event.get('pathParameters')

    try:
        if path_params and 'user_id' in path_params:
            # Get one user
            user_id = path_params['user_id']
            response = table.get_item(Key={'user_id': user_id})
            item = response.get('Item')

            if not item:
                return {
                    'statusCode': 404,
                    'body': json.dumps({'message': 'User not found'})
                }

            return {
                'statusCode': 200,
                'body': json.dumps(item, cls=DecimalEncoder)
            }
        else:
            # List all user_ids
            scan_result = table.scan(ProjectionExpression="user_id")
            user_ids = [item['user_id'] for item in scan_result.get('Items', [])]

            return {
                'statusCode': 200,
                'body': json.dumps({"user_ids": user_ids})
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }