import requests
import json
from typing import Optional, Tuple
from config import BING_API, BING_URL

def get_bing_wallpaper() -> Tuple[Optional[str], Optional[str], Optional[str]]:
    response = requests.get(BING_API)
    data = response.json()
    print(json.dumps(data, ensure_ascii=False, indent=2))  # 打印标准 JSON 格式

    if data and 'images' in data:
        image_info = data['images'][0]
        image_url = BING_URL + image_info['url']
        image_description = image_info.get('copyright', 'Bing Daily Wallpaper')
        image_title = image_info.get('title', '🔖今日必应壁纸')
        return image_url, image_description, image_title
    print('No wallpaper found')
    return None, None, None
