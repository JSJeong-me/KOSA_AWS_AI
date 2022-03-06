import boto3

ID = ''
ID_KEY = ''

tableName = 'users'

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1',aws_access_key_id=ID, aws_secret_access_key=ID_KEY)

table = dynamodb.Table(tableName)

table = dynamodb.create_table(
    TableName=tableName,
    KeySchema=[
        {
            'AttributeName': 'last_name',
            'KeyType': 'HASH' 
        },
        {
            'AttributeName': 'age',
            'KeyType': 'RANGE' 
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'age',
            'AttributeType': 'N' 
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)


