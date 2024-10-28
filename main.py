from datetime import datetime, timezone
from feushu_api import get_feishu_token,send_to_feishu
from bing_wallpaper import get_bing_wallpaper

def main():
    # 获取当前时间，并设置为本地时区
    current_time = datetime.now(timezone.utc).astimezone()
    # 格式化为 年-月-日 时:分:秒 时区格式
    print(current_time.strftime('%Y-%m-%d %H:%M:%S %Z %z'))

    wallpaper_url, wallpaper_description, wallpaper_title = get_bing_wallpaper()
    if wallpaper_url:
        access_token = get_feishu_token()
        print(f'🔖 {wallpaper_title}')
        print(f"📝 {wallpaper_description}")
        print(f"🔗 {wallpaper_url}")
        send_to_feishu(wallpaper_url, wallpaper_description, wallpaper_title, access_token)

if __name__ == "__main__":
    main()
