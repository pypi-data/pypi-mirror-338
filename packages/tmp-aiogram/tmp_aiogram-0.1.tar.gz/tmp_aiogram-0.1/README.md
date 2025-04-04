# tmp-aiogram

`tmp-aiogram` — bu Python bilan yozilgan Aiogram botini yaratishga yordam beruvchi paket. Ushbu paket Docker, `.gitignore`, va boshqa konfiguratsiyalarni o'z ichiga oladi, bu esa botni oson sozlash va ishlatish imkonini beradi.

## Loyiha strukturasini yaratish

Loyiha yaratish uchun quyidagi fayl va papkalar tuzilmasi bo'ladi:

``` bash

tmp-aiogram/
├── handlers/
│   ├── __init__.py
│   └── start.py
├── utils/
│   ├── __init__.py
│   ├── texts.py
│   ├── buttons.py
│   └── env.py
├── services/
│   ├── __init__.py
│   └── services.py
├── state/
│   ├── __init__.py
│   └── state.py
├── .env
├── .env.example
├── dockerfile
├── docker-compose.yml
├── .gitignore
├── bot.py
├── loader.py
├── README.md
└── requirements.txt
```



## O'rnatish

1. **Paketni o'rnatish:**

   Avvalo, `tmp-aiogram` paketini o'rnating:

   ```bash
    pip install tmp-aiogram

    ```

## Yangi template yaratish

``` bash
    tmp project_name
```


