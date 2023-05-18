# Import the JSON library to work with JSON data
import json

# Initialize an empty dictionary to store items
items = {}

# Define a Lambda function handler to process incoming requests
def lambda_handler(event, context):
    # Retrieve the HTTP method from the event object
    httpMethod = event['httpMethod']

    # If the HTTP method is GET
    if httpMethod == 'GET':
        # Check if an ID has been provided in the path parameters
        if 'pathParameters' in event and event['pathParameters'] and 'id' in event['pathParameters']:
            id = event['pathParameters']['id']
            # If the ID exists in the items, return the item
            if id in items:
                return {
                    'statusCode': 200,
                    'body': json.dumps(items[id]), # Convert the item data to JSON
                    # Set CORS headers
                    'headers': {
                        'Access-Control-Allow-Origin': '*', 
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
                    },
                }
            # If the ID does not exist, return a 404 (not found) error
            else:
                return {
                    'statusCode': 404,
                    'body': 'Item not found',
                    # Set CORS headers
                    'headers': {
                        'Access-Control-Allow-Origin': '*', 
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
                    },
                }
        # If no ID is provided, return all items
        else:
            return {
                'statusCode': 200,
                'body': json.dumps(items), # Convert all items data to JSON
                # Set CORS headers
                'headers': {
                    'Access-Control-Allow-Origin': '*', 
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
                },
            }

    # If the HTTP method is POST
    elif httpMethod == 'POST':
        # Parse the body of the request (assumed to be JSON) into an item
        item = json.loads(event['body'])
        # Generate an ID for the new item and add it to the items dictionary
        id = str(len(items) + 1)
        items[id] = item
        # Return the ID of the new item
        return {
            'statusCode': 201,
            'body': json.dumps({'id': id}), # Convert the item data to JSON
            # Set CORS headers
            'headers': {
                'Access-Control-Allow-Origin': '*', 
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
            },
        }
    # If the HTTP method is PUT
    elif httpMethod == 'PUT':
    # Check if an ID has been provided in the path parameters
        if 'pathParameters' in event and event['pathParameters'] and 'id' in event['pathParameters']:
            id = event['pathParameters']['id']
            # If the ID exists, update the item
            if id in items:
                items[id] = json.loads(event['body']) # Parse the body of the request (assumed to be JSON) into an item and update
                return {
                    'statusCode': 200,
                    'body': 'Item updated',
                    # Set CORS headers
                    'headers': {
                        'Access-Control-Allow-Origin': '*', 
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
                    },
                }
            # If the ID does not exist, return a 404 (not found) error
            else:
                return {
                    'statusCode': 404,
                    'body': 'Item not found',
                    # Set CORS headers
                    'headers': {
                        'Access-Control-Allow-Origin': '*', 
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
                    },
                }

    # If the HTTP method is DELETE
    elif httpMethod == 'DELETE':
        # Check if an ID has been provided in the path parameters
        if 'pathParameters' in event and event['pathParameters'] and 'id' in event['pathParameters']:
            id = event['pathParameters']['id']
            # If the ID exists, delete the item
            if id in items:
                del items[id] # Remove the item from the dictionary
                return {
                    'statusCode': 200,
                    'body': 'Item deleted',
                    # Set CORS headers
                    'headers': {
                        'Access-Control-Allow-Origin': '*', 
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
                    },
                }
            # If the ID does not exist, return a 404 (not found) error
            else:
                return {
                    'statusCode': 404,
                    'body': 'Item not found',
                    # Set CORS headers
                    'headers': {
                        'Access-Control-Allow-Origin': '*', 
                        'Access-Control-Allow-Headers': 'Content-Type',
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
                    },
                }