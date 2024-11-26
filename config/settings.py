import os

# 环境变量配置
FEISHU_APP_ID = os.getenv('FEISHU_APP_ID', '')
FEISHU_APP_SECRET = os.getenv('FEISHU_APP_SECRET', '')
FEISHU_WEBHOOK_URL = os.getenv('FEISHU_WEBHOOK_URL', '')
FEISHU_SIGNING_KEY = os.getenv('FEISHU_SIGNING_KEY', '')

DINGTALK_WEBHOOK_URL = os.getenv('FEISHU_WEBHOOK_URL', '')
DINGTALK_SIGNING_KEY = os.getenv('FEISHU_SIGNING_KEY', '')

BING_URL = 'https://bing.com'
BING_API = f'{BING_URL}/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
