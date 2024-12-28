import json
import requests

from config import WECOME_WEBHOOK_URL


def send_to_wecome(image_url: str, title: str, description: str) -> dict:
    headers = {"Content-Type": "application/json"}
    # 企业微信的Markdown渲染不支持图片的嵌入;
    # 通过news消息类型生成卡片消息时，图片默认显示在标题下方，描述在最下方,这种消息格式是固定的!!!
    # https://developer.work.weixin.qq.com/document/path/91770#%E5%9B%BE%E6%96%87%E7%B1%BB%E5%9E%8B
    content = {
        "msgtype": "news",
        "news": {
            "articles": [{
                "title": f'🔖 {description}',
                # "title": f'🔖 {title}',
                # "description": f'📝 {description}',
                "url": image_url,
                "picurl": image_url,
            }]
        }
    }
    # content = {
    #     "msgtype": "markdown",
    #     "markdown": {
    #         "content": f"🔖 **{title}**\n\n"
    #                    f"![BingWallpaper]({image_url})\n\n"
    #                    f"> 📝 {description}"
    #     }
    # }

    response = requests.post(WECOME_WEBHOOK_URL, data=json.dumps(content), headers=headers)

    print(f'Request URL: {response.request.url}')
    print(f'Request Method: {response.request.method}')
    print(json.dumps(response.json(), ensure_ascii=False, indent=2))

    return response.json()
