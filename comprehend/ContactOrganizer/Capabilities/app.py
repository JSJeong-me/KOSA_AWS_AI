# -*- coding: utf-8 -*-

from chalice import Chalice
from chalicelib import storage_service
from chalicelib import recognition_service
from chalicelib import extraction_service
from chalicelib import contact_store

import base64
import json


#####
# 챌리스 애플리케이션 설정
#####
app = Chalice(app_name='Capabilities')
app.debug = True

#####
# 서비스 초기화
#####
storage_location = 'contact-organizer'
storage_service = storage_service.StorageService(storage_location)
recognition_service = recognition_service.RecognitionService(storage_location)
extraction_service = extraction_service.ExtractionService()
store_location = 'Contacts'
contact_store = contact_store.ContactStore(store_location)


#####
# RESTful 엔드포인트
#####
@app.route('/images', methods = ['POST'], cors = True)
def upload_image():
    """파일 업로드를 준비하고 스토리지 서비스에 파일 업로드"""
    request_data = json.loads(app.current_request.raw_body)
    file_name = request_data['filename']
    file_bytes = base64.b64decode(request_data['filebytes'])

    file_info = storage_service.upload_file(file_bytes, file_name)

    return file_info


@app.route('/images/{image_id}/extract-info', methods = ['POST'], cors = True)
def extract_image_info(image_id):
    """특정 이미지에서 텍스트를 탐지하고 해당 텍스트에서 연락처 정보를 추출"""
    MIN_CONFIDENCE = 70.0

    text_lines = recognition_service.detect_text(image_id)

    contact_lines = []
    for line in text_lines:
        # check confidence
        if float(line['confidence']) >= MIN_CONFIDENCE:
            contact_lines.append(line['text'])

    contact_string = '   '.join(contact_lines)
    contact_info = extraction_service.extract_contact_info(contact_string)

    return contact_info


@app.route('/contacts', methods = ['POST'], cors = True)
def save_contact():
    """연락처 정보를 연락처 저장 서비스에 저장"""
    request_data = json.loads(app.current_request.raw_body)

    contact = contact_store.save_contact(request_data)

    return contact


@app.route('/contacts', methods = ['GET'], cors = True)
def get_all_contacts():
    """연락처 저장 서비스에 저장된 모든 연락처를 읽어 옴"""
    contacts = contact_store.get_all_contacts()

    return contacts

