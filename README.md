# Tell Telegram
A simple command line utility to send messages via a telegram bot.

## Usage

```
$ telltg
usage: 
telltg "Hello world"
longrunning_program && telltg -o "My batch job" "Done"
echo "Hello world" | telltg

Configuration. choose one of the following options:
- Config file:
    - create a telltg.conf.json file in
        - ~/.telltg.conf.json
        - /etc/telltg.conf.json
    - copy and customize this config:
        {"key":"bot123:abc","ids":["1234", "456"]}
- ENVIRONMENTAL VARIABLE
    - set the following environmental variables
    - TELLTG_BOT_KEY
    - TELLTG_CHAT_IDS (as comma separated values)

A CLI Telegram message sender

positional arguments:
  message               The message you want to send

optional arguments:
  -h, --help            show this help message and exit
  --object OBJECT, -o OBJECT
                        Message object
  --hostname, -n        Include hostname
  --id [ID [ID ...]], -i [ID [ID ...]]
                        Send to specific chat_id
```

## Configuration

### Bot setup
First a bot and a chat_id are needed:
* create a bot via the [BotFather](https://telegram.me/botfather)
* take note of the bot's `token` provided by the botfather
* add the bot to your contacts and sent it a message
* Use the `getUpdates` API method to retrive your `chat_id`
  * YOu can do that by point your browser at `https://api.telegram.org/bot{token}/getUpdates` and look for an `id` element inside a `chat` element

### Installation

Run the following command: `$ pip install telltg`

### Config file
Write the config file with the syntax sppecified below in one of the following locations:

* `~/.telltg.conf.json`
* `/etc/telltg.conf.json`


```
{
  "key":"mykey",
  "ids":[
    "myid1"
  ]
}
```
