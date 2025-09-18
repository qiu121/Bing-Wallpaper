# Bing-Wallpaper 🖼️✨

[![Release Version](https://img.shields.io/github/v/release/qiu121/Bing-Wallpaper?label=version)](https://github.com/qiu121/Bing-Wallpaper/releases)
[![License](https://img.shields.io/github/license/qiu121/Bing-Wallpaper)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/qiu121/Bing-Wallpaper?style=social)](https://github.com/qiu121/Bing-Wallpaper/stargazers)

![Python](https://img.shields.io/badge/python-3.12%2B-3776AB?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/deploy-Docker-2496ED?logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?logo=githubactions&logoColor=white)
![GitLab CI](https://img.shields.io/badge/CI-GitLab-C51F1F?logo=gitlab&logoColor=white)

![Feishu](https://img.shields.io/badge/support-Feishu-2C8DF4?logo=bytedance&logoColor=white)
![DingTalk](https://img.shields.io/badge/support-DingTalk-007FFF?logo=alibabacloud&logoColor=white)
![WeCom](https://img.shields.io/badge/support-WeCom-1AAD19?logo=wechat&logoColor=white)
![Slack](https://img.shields.io/badge/support-Slack-4A154B?logo=slack&logoColor=white)

> 🚀 Get daily **Bing wallpapers** and push them to your chat platforms via webhooks — extensible to more providers.

---

## 📖 目录

- [🌟 功能简介](#-功能简介)  
- [⚡ 快速开始](#-快速开始)  
  - [📦 环境要求](#-环境要求)  
  - [⬇️ 安装](#-安装)  
  - [⚙️ 配置](#-配置)  
  - [▶️ 运行](#-运行)  
- [🛠️ 部署方式](#️-部署方式)  
  - [🐳 Docker](#-docker)  
  - [🤖 CI / GitHub Actions / GitLab CI](#-ci--github-actions--gitlab-ci)  
- [💬 支持的平台 / 通知渠道](#-支持的平台--通知渠道)  
- [📂 项目结构](#-项目结构)  
- [🔧 配置详解 (环境变量)](#-配置详解-环境变量)  
- [🤝 贡献指南](#-贡献指南)  
- [📜 许可证](#-许可证)  
- [🙏 致谢](#-致谢)

---

## 🌟 功能简介

`Bing-Wallpaper` 是一个自动获取必应每日壁纸（Bing Daily Wallpaper），并通过可配置的 webhook 推送到你的聊天平台（如飞书 / 钉钉 / 企业微信 / Slack 等），支持扩展更多推送适配器。

支持定时运行，自动下载壁纸并推送（含图片与描述），也可按需触发。

---

## ⚡ 快速开始

### 📦 环境要求

- **Python 3.12+**  
- 目标通知平台的机器人 Webhook 或 Token



### ⬇️ 安装

> **推荐使用 [`uv`](https://docs.astral.sh/uv/getting-started/)** 来创建隔离的虚拟环境并安装依赖

**使用 `uv`**

```bash
# 创建全新虚拟环境
uv venv --python 3.12 --seed .venv

# 激活虚拟环境
# Linux / macOS (bash / zsh)
source .venv/bin/activate

# Windows - PowerShell
.venv\Scripts\Activate.ps1

# Windows - cmd.exe
.venv\Scripts\activate.bat

# 在虚拟环境中安装依赖（如果 uv pip 已可用）
uv pip install -r requirements.txt

```


**使用传统方法（venv + pip）**

```bash
python3.12 -m venv .venv

# 激活虚拟环境
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\Activate.ps1 # Windows PowerShell
.venv\Scripts\activate.bat # Windows cmd

# 安装依赖
pip install -r requirements.txt
```

> 说明：使用 `python3.12 -m venv` 可以保证虚拟环境与指定解释器绑定（推荐在多 Python 版本机器上显式指定 `python3.12`）。

### ⚙️ 配置

使用 `.env` 或配置文件设置各平台的 Webhook/Token、Bing API 等。详见下方“配置详解（环境变量）”。

### ▶️ 运行

```bash
python main.py
```

可通过命令行参数选择只推送到某个平台或全部推送（请参考项目中的 CLI/入口实现）。

---

## 🛠️ 部署方式

### 🐳 Docker

构建镜像并运行：

```bash
docker build -t bing-wallpaper .

docker run -d --name bing-wallpaper --env-file .env bing-wallpaper
```

> 说明：确保 `.env` 中填写了你的 webhook 等敏感配置，且不要把 `.env` 提交到公共仓库。

### 🤖 CI / GitHub Actions / GitLab CI

仓库支持通过 CI/CD 运行或定时触发：

- **GitHub Actions**：可在 `.github/workflows/` 中添加 workflow，并使用 GitHub 的 scheduled triggers（cron）来定时运行。  
- **GitLab CI**：**注意**：GitLab 的 pipeline schedule（定时触发）需要在 GitLab 的 Web UI 中配置（`CI/CD → Schedules`），不能仅通过 `.gitlab-ci.yml` 在仓库内声明 cron。请在项目设置中创建 Schedule 并指向目标分支/变量。 

---

## 💬 支持的平台 / 通知渠道

| 渠道 | 类型 | 备注 |
|-----|------|------|
| 🪁 飞书（Feishu） | 自定义机器人 / App | 支持文本 + 图片（支持 AppId/Secret 签名等） |
| 🐬 钉钉（Dingtalk） | Webhook 机器人 | 支持文本 + 图片（支持签名） |
| 💼 企业微信（WeCom） | Webhook / Agent | 支持群聊或个人 |
| 🎨 Slack | Incoming Webhook | 支持文本 + 图片 |

---

## 📂 项目结构

```
Bing-Wallpaper/
├── .github/                # CI / Actions
├── config/                 # 配置文件
├── feishu/                 # 飞书推送模块
├── dingtalk/               # 钉钉推送模块
├── wecom/                  # 企业微信推送模块
├── slack/                  # Slack 推送模块
├── wallpaper/              # 获取壁纸
├── main.py                 # 主入口
├── requirements.txt        # 依赖
└── Dockerfile              # Docker 支持
```

---

## 🔧 配置详解 - 环境变量

请在 `.env` 或 CI Secret 中添加以下变量,下面列出完整变量清单：

```
FEISHU_APP_ID=
FEISHU_APP_SECRET=
FEISHU_WEBHOOK_URL=
FEISHU_SIGNING_KEY=

DINGTALK_WEBHOOK_URL=
DINGTALK_SIGNING_KEY=

WECOM_WEBHOOK_URL=

SLACK_WEBHOOK_URL=
```

**说明与使用建议**

- `FEISHU_APP_ID` / `FEISHU_APP_SECRET`：用于通过飞书开放平台获取 access_token（若你使用 App 授权方式）
- `FEISHU_WEBHOOK_URL` / `FEISHU_SIGNING_KEY`：用于自定义机器人推送（Webhook + 签名）  
- `DINGTALK_WEBHOOK_URL` / `DINGTALK_SIGNING_KEY`：用于钉钉机器人推送（签名可防止未授权调用）。
-  `WECOM_WEBHOOK_URL`：企业微信机器人
- `SLACK_WEBHOOK_URL`：Slack Incoming Webhook 地址

> 建议：把这些敏感变量放到 CI 的 secret 管理（GitHub Secrets / GitLab CI Variables / Docker Secrets）或使用环境管理器，不要把 `.env` 提交到仓库。

---

## 🤝 贡献指南

欢迎贡献代码 / 提交 Issue / Pull Request！

- 提交 PR 前请确保代码风格一致。  
- 新增功能请附带必要的文档或配置说明。  
- 如涉及敏感凭证，请使用 GitHub Secrets 或 CI 的安全变量，不要提交到仓库。

---

## 📜 许可证

本项目采用 **MIT License**，详见 [LICENSE](LICENSE) 文件。

---

## 🙏 致谢

- 📷 必应（Bing）的每日壁纸 API  
- 🔔 Slack, Feishu, Dingtalk, WeCom 提供的机器人推送接口  
- 💡 本项目所有贡献者
