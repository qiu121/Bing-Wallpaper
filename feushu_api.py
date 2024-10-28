import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
from typing import Optional
from config import FEISHU_APP_ID, FEISHU_APP_SECRET, FEISHU_WEBHOOK_URL, FEISHU_SIGNING_KEY
from utils import calculate_signature
import time

def get_feishu_token() -> str:
    token_url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({
        "app_id": FEISHU_APP_ID,
        "app_secret": FEISHU_APP_SECRET
    })
    response = requests.post(token_url, headers=headers, data=data)
    result = response.json()
    return result.get('tenant_access_token', '')


def upload_image(image_url: str, access_token: str) -> Optional[str]:
    url = "https://open.feishu.cn/open-apis/im/v1/images"
    image_data = requests.get(image_url).content
    form = {'image_type': 'message', 'image': ('image.jpg', image_data)}
    multi_form = MultipartEncoder(fields=form)
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': multi_form.content_type
    }
    response = requests.post(url, headers=headers, data=multi_form)
    image_key = response.json().get('data', {}).get('image_key')
    return image_key


def send_to_feishu(image_url: str, image_description: str, image_title: str, access_token: str) -> dict:
    # 获取当前时间戳
    timestamp = str(int(time.time()))
    # 计算签名
    sign = calculate_signature(timestamp, FEISHU_SIGNING_KEY)

    headers = {'Content-Type': 'application/json'}
    image_key = upload_image(image_url, access_token)
    data = {
        "timestamp": f'{timestamp}',
        "sign": f'{sign}',
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": f'🔖{image_title}',
                    "content": [
                        [
                            {
                                "tag": "img",
                                "image_key": image_key
                            },
                            {
                                "tag": "text",
                                "text": f"📝{image_description}"
                            },
                        ]
                    ]
                }
            }
        }
    }
    response = requests.post(FEISHU_WEBHOOK_URL, headers=headers, data=json.dumps(data))
    print(f'Request URL: {response.request.url}')
    print(f'Request Method: {response.request.method}')
    print(json.dumps(response.json(), ensure_ascii=False, indent=2))  # 打印标准 JSON 格式
    return response.json()
