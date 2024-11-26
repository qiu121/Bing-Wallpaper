import time
import requests
import json

from config import DINGTALK_WEBHOOK_URL, DINGTALK_SIGNING_KEY
from dingtalk.signature import calculate_signature


def send_to_dingtalk(image_url: str, title: str, description: str) -> dict:
    timestamp = str(round(time.time() * 1000))
    headers = {"Content-Type": "application/json"}
    sign = calculate_signature(timestamp, DINGTALK_SIGNING_KEY)

    params = {
        "timestamp": timestamp,
        "sign": sign,
    }
    content = {
        "msgtype": "markdown",
        "markdown": {
            "title": f'🔖 {title}',
            "text": f"### 🔖 {title}\n\n![壁纸]({image_url})\n\n> 📝 {description}"
        }
    }
    response = requests.post(DINGTALK_WEBHOOK_URL, data=json.dumps(content), headers=headers, params=params)
    print(f'Request URL: {response.request.url}')
    print(f'Request Method: {response.request.method}')
    print(json.dumps(response.json(), ensure_ascii=False, indent=2))  # 打印标准 JSON 格式
    return response.json()
