from chalice import Chalice
from chalicelib import storage_service
from chalicelib import recognition_service

import random


#####
# 챌리스 애플리케이션 설정
#####
app = Chalice(app_name='Capabilities')
app.debug = True


#####
# 서비스 초기화
#####
storage_location = 'contents.junho.her'
storage_service = storage_service.StorageService(storage_location)
recognition_service = recognition_service.RecognitionService(storage_service)


@app.route('/demo-object-detection', cors = True)
def demo_object_detection():
    """randomly selects one image to demo object detection"""
    files = storage_service.list_files()
    images = [file for file in files if file['file_name'].endswith(".jpeg")]
    image = random.choice(images)

    objects = recognition_service.detect_objects(image['file_name'])

    return {
        "imageName": image['file_name'],
        "imageUrl": image['url'],
        "objects": objects
    }


