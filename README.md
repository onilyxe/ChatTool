# Chattool для telegram

[Спробуй мого бота](https://t.me/BudanovKVBot)

Встановлення
------------
```shell
$ git clone https://github.com/onilyxe/chattool.git

$ cd chattool
```

Налаштування    
------------
**Відкрий `config.json` у текстовому редакторі та зміни значення на свої:**
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
* `ADMINS` id адмінів для адмін команд
* `CHAT_TITLE` назва чату для /topic

Запуск
------------
Юзай python
```shell
# Встанови залежності
$ python3 -m pip install -r requirements.txt

# Запусти скріпт
$ python3 chattool.py
```