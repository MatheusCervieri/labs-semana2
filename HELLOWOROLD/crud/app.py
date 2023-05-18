import json

items = {}

def lambda_handler(event, context):
    httpMethod = event['httpMethod']

    if httpMethod == 'GET':
        if 'pathParameters' in event and event['pathParameters'] and 'id' in event['pathParameters']:
            id = event['pathParameters']['id']
            if id in items:
                return {
                    'statusCode': 200,
                    'body': json.dumps(items[id]),
                    'headers': {
                        'Access-Control-Allow-Origin': '*',  # Use '*' to allow any origin or replace '*' with your specific origin
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
                    },
                }
            else:
                return {
                    'statusCode': 404,
                    'body': 'Item not found',
                    'headers': {
                        'Access-Control-Allow-Origin': '*',  # Use '*' to allow any origin or replace '*' with your specific origin
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
                    },
                }
        else:
            return {
                'statusCode': 200,
                'body': json.dumps(items),
                'headers': {
                    'Access-Control-Allow-Origin': '*',  # Use '*' to allow any origin or replace '*' with your specific origin
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
                },
            }

    elif httpMethod == 'POST':
        item = json.loads(event['body'])
        id = str(len(items) + 1)
        items[id] = item
        return {
            'statusCode': 201,
            'body': json.dumps({'id': id}),
            'headers': {
                'Access-Control-Allow-Origin': '*',  # Use '*' to allow any origin or replace '*' with your specific origin
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
            },
        }

    elif httpMethod == 'PUT':
        if 'pathParameters' in event and event['pathParameters'] and 'id' in event['pathParameters']:
            id = event['pathParameters']['id']
            if id in items:
                items[id] = json.loads(event['body'])
                return {
                    'statusCode': 200,
                    'body': 'Item updated',
                    'headers': {
                        'Access-Control-Allow-Origin': '*',  # Use '*' to allow any origin or replace '*' with your specific origin
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
                    },
                }
            else:
                return {
                    'statusCode': 404,
                    'body': 'Item not found',
                    'headers': {
                        'Access-Control-Allow-Origin': '*',  # Use '*' to allow any origin or replace '*' with your specific origin
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
                    },
                }

    elif httpMethod == 'DELETE':
        if 'pathParameters' in event and event['pathParameters'] and 'id' in event['pathParameters']:
            id = event['pathParameters']['id']
            if id in items:
                del items[id]
                return {
                    'statusCode': 200,
                    'body': 'Item deleted',
                    'headers': {
                        'Access-Control-Allow-Origin': '*',  # Use '*' to allow any origin or replace '*' with your specific origin
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
                    },
                }
            else:
                return {
                    'statusCode': 404,
                    'body': 'Item not found',
                    'headers': {
                        'Access-Control-Allow-Origin': '*',  # Use '*' to allow any origin or replace '*' with your specific origin
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
                    },
                }

    else:
        return {
            'statusCode': 405,
            'body': 'Method not supported',
            'headers': {
                'Access-Control-Allow-Origin': '*',  # Use '*' to allow any origin or replace '*' with your specific origin
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
            },
        }
