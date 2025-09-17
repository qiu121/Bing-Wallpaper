import json
import requests
from config import SLACK_WEBHOOK_URL

def send_to_slack_compact(image_url: str, title: str, description: str) -> dict:
    headers = {"Content-Type": "application/json"}

    content = {
        "blocks": [
            # 标题
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*🔖 {title}*"
                }
            },
            # 图片
            {
                "type": "image",
                "image_url": image_url,
                "alt_text": description
            },
            # 描述（紧贴图片）
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"> 📝 {description}"
                    }
                ]
            }
        ]
    }

    response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(content), headers=headers)

    print(f"Request URL: {response.request.url}")
    print(f"Request Method: {response.request.method}")
    print(f"Response: {response.status_code} {response.text}")

    return {"status": response.status_code, "text": response.text}
