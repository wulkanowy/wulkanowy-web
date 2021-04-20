# Wulkanowy Web

🌋 Unofficial VULCAN UONET+ browser client for students and their parents

![GitHub Workflow Status](https://github.com/wulkanowy/wulkanowy-web/workflows/Python%20application/badge.svg)

## Join our Discord server!

[![Discord](https://i.imgur.com/3ljTQWy.png)](https://discord.gg/5qsEujZMdp)

# Development

## 1. Install dependencies

```sh
pip install -r requirements.txt
npm install
```

## 2. Make migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

## 3. Start the server

```sh
python manage.py runserver
npm run dev
```

# Docker

With docker compose

```sh
docker-compose up -d
```

Without docker compose

```sh
docker build -t wulkanowy/web .
docker run -d -p 8000:8000 wulkanowy/web
```