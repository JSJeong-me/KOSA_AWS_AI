import boto3
from boto3.dynamodb.conditions import Key

ID = ''
ID_KEY = ''

tableName = 'users'

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1',aws_access_key_id=ID, aws_secret_access_key=ID_KEY)

table = dynamodb.Table(tableName)

#Get all users with last name of Johnson
johnsons = table.scan(
    FilterExpression=Key('last_name').eq("Johnson")
)
print(johnsons)

#Get all users over the age of 30
overThirty = table.scan(
    FilterExpression=Key('age').gt(30)
)
print(overThirty['Items'])
