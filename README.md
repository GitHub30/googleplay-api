# Download apk

```bash
wget https://apks.deta.dev/com.pixel.gun3d.apk
wget https://apks.deta.dev/jp.co.mcdonalds.android.apk
wget https://apks.deta.dev/com.starbucks.jp.apk
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
