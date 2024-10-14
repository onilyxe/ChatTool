# ЧатТул фор тг
Блін я не пам'ятаю його функціонал

[Мій бот](https://t.me/BudanovKVBot)

Встановлення
------------
```shell
# Клонуй
$ git clone https://github.com/onilyxe/chattool.git

# Заходь
$ cd chattool
```

Конфігування
------------
**Відкрий `config.json` файл у текстовому редакторі та зміни значення на свої:**
```ini
{
    "TOKEN": "0000000000:0000000000000000000000000000000000",
    "ADMINS": [
        000000000,
        000000001
    ],
    "CHAT_TITLE": "міністерство канабісу"
}
```
* `TOKEN` це токен твого бота. Отримати його можна тут: [BotFather](https://t.me/BotFather)
* `ADMINS` id адмінів для адмін команд: [BotFather](https://t.me/BotFather)
* `CHAT_TITLE` назва чату для /topic: [BotFather](https://t.me/BotFather)

Пихтіти працювати
------------
Юзай пітон (не свій)
```shell
# Встанови залежності
$ python3 -m pip install -r requirements.txt

# Ран скріпт
$ python3 chattool.py
```