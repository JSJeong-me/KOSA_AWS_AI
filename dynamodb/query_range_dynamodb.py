import boto3
from boto3.dynamodb.conditions import Key

ID = ''
ID_KEY = ''

tableName = 'users'

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1',aws_access_key_id=ID, aws_secret_access_key=ID_KEY)

table = dynamodb.Table(tableName)

middleAges = table.query(
    ProjectionExpression="last_name, first_name, age, id",
    KeyConditionExpression=
        Key('last_name').eq('Johnson') & Key('age').between(30,40)
)
print(middleAges['Items'])
