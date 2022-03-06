import boto3
from boto3.dynamodb.conditions import Key

ID = ''
ID_KEY = ''


tableName = 'users'

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1',aws_access_key_id=ID,aws_secret_access_key=ID_KEY)

table = dynamodb.Table(tableName)

goodbyeJohnson = table.delete_item(
    Key={
        'last_name': 'Johnson',
        'age': 33
    }
)
