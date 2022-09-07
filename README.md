# Download apk

```bash
wget https://apks.deta.dev/com.pixel.gun3d.apk
```

# Development

```bash
#deta new --project apk
deta visor enable

echo 'email=??????@gmail.com
password=??????????' > .env
deta update -e .env

# When changing requirements.txt or gpapi
deta deploy purge-dependencies
deta deploy
```
