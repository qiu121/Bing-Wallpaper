from datetime import datetime, timezone

from wallpaper import get_bing_wallpaper
from feishu import get_feishu_token, send_to_feishu
from dingtalk import send_to_dingtalk
from wecom import send_to_wecome


def main():
    # 获取当前时间，并设置为本地时区
    current_time = datetime.now(timezone.utc).astimezone()
    # 格式化为 年-月-日 时:分:秒 时区格式
    print(current_time.strftime('%Y-%m-%d %H:%M:%S %Z %z'))

    wallpaper_url, wallpaper_description, wallpaper_title = get_bing_wallpaper()
    access_token = get_feishu_token()
    if wallpaper_url:
        print(f'🔖 {wallpaper_title}')
        print(f"📝 {wallpaper_description}")
        print(f"🔗 {wallpaper_url}")
        send_to_feishu(wallpaper_url, wallpaper_description, wallpaper_title, access_token)
        send_to_dingtalk(wallpaper_url, wallpaper_title, wallpaper_description)

        send_to_wecome(wallpaper_url, wallpaper_title, wallpaper_description)


if __name__ == "__main__":
    main()
