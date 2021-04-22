# BoraBoraBot
Wenn ihr es kaum erwarten könnt einen weiteren von BoraBoras Anwesenheitstests zu schreiben, dann ist dieser Bot genau richtig für euch.

Verpasst keinen Anwesenheitstest, indem ihr euch von der zarten Stimme BoraBoras auf Discord erinnern lasst, dass es mal wieder Zeit ist sich den schönen Seiten des Lebens zuzuwenden.

# Installation

Benutzt diesen [Link](https://discord.com/api/oauth2/authorize?client_id=834381041644208170&permissions=3147776&scope=bot) um den Bot auf einem Server eurer Wahl zu installieren.

# Deploy Backend
Eventuell wollt ihr das Backend des Bots selbst deployen. Dafür könnt ihr das Skript borabora.py benutzen, müsst aber zunächst einen Bot im [Discord Developer Portal](https://discord.com/developers/docs/intro) erstellen. Dieser braucht die Rechte zum schreiben, betreten eines Channels und sprechen im Channel.

# Usage
```
usage: boraborabot.py [-h] [--discord DISCORD] [--name NAME] [--passwd PASSWD] [--test] [--quiet]
                      [--noText] [--audio AUDIO]

Verpasst keinen Anwesenheitstest, indem ihr euch von der zarten Stimme BoraBoras auf Discord erinnern
lasst, dass es mal wieder Zeit ist sich den schönen Seiten des Lebens zuzuwenden.

optional arguments:
  -h, --help         show this help message and exit
  --discord DISCORD  Enables Discord Bot. Needs Discord token.
  --name NAME        Name to log in to Moodle like <name>@lehre.dhbw.mosbach.de.
  --passwd PASSWD    Password for Moodle.
  --test             Test the bot.
  --quiet            Deactivates the voice of BoraBora.
  --noText           Deactivates writing of BoraBora.
  --audio AUDIO      A folder with mp3 files to play from.
  ```
