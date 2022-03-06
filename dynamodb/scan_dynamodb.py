import boto3

ID = ''
ID_KEY = ''

tableName = 'users'

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1',aws_access_key_id=ID, aws_secret_access_key=ID_KEY)

table = dynamodb.Table(tableName)

allUsers = table.scan()
print(allUsers)
