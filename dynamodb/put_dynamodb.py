import boto3

ID = ''
ID_KEY = ''

tableName = 'users'

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1',aws_access_key_id=ID, aws_secret_access_key=ID_KEY)

table = dynamodb.Table(tableName)

item1 = table.put_item(
    Item={
        'last_name': 'Johnson',
        'first_name': 'Benjamin',
        'age': 28,
        'id': 49387266
        }
    )
print(item1)

item2 = table.put_item(
    Item={
        'last_name': 'Jones',
        'first_name': 'Mary',
        'age': 42,
        'id': 49387267
        }
    )
print(item2)

item3 = table.put_item(
    Item={
        'last_name': 'Johnson',
        'first_name': 'Joe',
        'age': 33,
        'id': 49387268
        }
    )
print(item3)
