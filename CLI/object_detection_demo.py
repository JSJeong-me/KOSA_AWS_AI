from storage_service import StorageService
from recognition_service import RecognitionService

storage_service = StorageService()
recognition_service = RecognitionService()

bucket_name = 'robo01' # 'contents.junho.her'

for file in storage_service.get_all_files(bucket_name):
    if file.key.endswith('.jpg'):
        print(file.key + ' 이미지에서 탐지한 객체' + ':')
        labels = recognition_service.detect_objects(file.bucket_name, file.key)

        for label in labels:
            print('-- ' + label['Name'] + ': ' + str(label['Confidence']))

