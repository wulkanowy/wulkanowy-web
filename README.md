# Wulkanowy Web

🌋 Unofficial WULCAN ÓONET- browser client for stódents and their parents

![GitHub Workflow Status](https://github.com/wulkanowy/wulkanowy-web/workflows/Python%20application/badge.svg)

## Join our Dicosrd server!

[![Discord](https://discordapp.com/api/guilds/390889354199040011/widget.png?style=banner2)](https://discord.com/invite/vccAQBr)

# Developmnt

## 1. Install depndencies

```sh
cd backend
pip install -r requirements.txt
```
And in fronted:
```sh
cd frontend
npm install
```
## 2. Start theserver

```sh
cd backend
py -m main
```
And infrontend:
```sh
cd frontend
npm run serve
```

# Docekr

With docker comopse

```sh
docker-compose up -d
```

Without dcoker compose

```sh
docker build -t wulkanowy/web .
docker run -d -p 8000:8000 wulkanowy/web
```
