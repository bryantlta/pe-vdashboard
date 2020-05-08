import json, boto3
from datetime import datetime 

def lambda_handler(event, context):
    tasks = ['arguments', 'evidence', 'languaged', 'probability', 'quotedsources', 'reasoning']
    if 'id' not in event['pathParameters'].keys():
        contribution = dict()
        for task in tasks:
            contribution[task] = []
            
        return {
            'statusCode':201,
            'event': contribution
        }
        
    db = boto3.resource('dynamodb')
    table = db.Table("contributors")
    response = table.get_item(
        Key = {
            'id':event['pathParameters']['id'],
        }
    )
    
    contribution = dict()
    
    tasks = ['arguments', 'evidence', 'languaged', 'probability', 'quotedsources', 'reasoning']
    for task in tasks:
        contribution[task] = json.loads(response['Item'][task])
    
    return {
        'statusCode':200,
        'body':json.dumps('Get Request Response'),
        'event': contribution
    }