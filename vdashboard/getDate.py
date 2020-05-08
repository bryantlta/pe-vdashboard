import json, boto3
from datetime import datetime 

def lambda_handler(event, context):
    event_date = event['pathParameters']['date']
    db = boto3.resource("dynamodb")
    table = db.Table("totalcontributions")
    
    try:
        response = table.get_item(
            Key = {
                'date': event_date
            }
        )
        
        return {
            "statusCode":200,
            "event": response['Item']
        }
    except: 
        return {
            "statusCode":201,
            "event": {
                "contributioncount":0,
                "date": event_date
            }
        }