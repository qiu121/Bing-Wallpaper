import requests
import json
import os
import time
import hashlib
import base64
import hmac
from requests_toolbelt.multipart.encoder import MultipartEncoder
from typing import Optional, Tuple

# 环境变量获取
FEISHU_APP_ID = os.getenv('FEISHU_APP_ID')
FEISHU_APP_SECRET = os.getenv('FEISHU_APP_SECRET')
FEISHU_WEBHOOK_URL = os.getenv('FEISHU_WEBHOOK_URL')
FEISHU_SIGNING_KEY = os.getenv('FEISHU_SIGNING_KEY')  # 签名密钥

BING_URL = 'https://bing.com'
BING_API = f'{BING_URL}/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'


def get_bing_wallpaper() -> Tuple[Optional[str], Optional[str], Optional[str]]:
    response = requests.get(BING_API)
    data = response.json()
    if data and 'images' in data:
        image_info = data['images'][0]
        image_url = BING_URL + image_info['url']
        image_description = image_info.get('copyright', 'Bing Daily Wallpaper')
        image_title = image_info.get('title', '🔖今日必应壁纸')
        return image_url, image_description, image_title
    print('No wallpaper found')
    return None, None, None


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


def calculate_signature(timestamp: str, secret: str) -> str:
    # 计算签名字符串：timestamp + "\n" + 密钥
    to_sign = f'{timestamp}\n{secret}'
    hmac_code = hmac.new(to_sign.encode('utf-8'), digestmod=hashlib.sha256).digest()
    # 对结果进行base64处理
    return base64.b64encode(hmac_code).decode('utf-8')


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
    return response.json()


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


def main():
    wallpaper_url, wallpaper_description, wallpaper_title = get_bing_wallpaper()
    if wallpaper_url:
        access_token = get_feishu_token()
        send_to_feishu(wallpaper_url, wallpaper_description, wallpaper_title, access_token)


if __name__ == "__main__":
    main()
