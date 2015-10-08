# Tell Telegram
A simple command line utility to send messages via a telegram bot.

## Usage

Telltg can be used with just one positional argument, the text:
`telltg "hello world"`

It can be used with `stdin`. As an example:
`cat MYFILE | telltg`

An optional argument `-d` (domain) is used to specify the "source" of the message.
This is useful to disambiguate which source/machine originated the message.

Optional `chat_id`(s) can be passed via the command line as well using the `-i flag`.

## Configuration

### Bot setup
First a bot and a chat_id are needed:
* create a bot via the [BotFather](https://telegram.me/botfather)
* take note of the bot's `token` provided by the botfather
* add the bot to your contacts and sent it a message
* Use the `getUpdates` API method to retrive your `chat_id`
  * YOu can do that by point your browser at `https://api.telegram.org/bot{token}/getUpdates` and look for an `id` element inside a `chat` element

### Installation

Run the following command: `pip install git+https://github.com/simonacca/TellTg/`

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
