# KickBot for Telegram
Bot helps to get rid of no-names and individuals in chat

[Try the my bot](https://t.me/sofiarolbot)

Installation
------------
```shell
# Clone the repository
$ git clone https://github.com/onilyxe/KickBot.git

# Change the working directory to KickBot
$ cd KickBot
```

Configuring
------------
**Open the `config.json` configuration file in a text editor and change the values to your own:**
```ini
{
    "TOKEN": "0000000000:0000000000000000000000000000000000"
}
```
* `TOKEN` is token for your Telegram bot. You can get it here: [BotFather](https://t.me/BotFather)

Running
------------
Using Python
```shell
# Install requirements
$ python3 -m pip install -r requirements.txt

# Run script
$ python3 KickBot.py
```