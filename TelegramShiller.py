from telethon import TelegramClient, functions, sync, events
from Message import fetch_text, fetch_list
import time

# Telegram bot that automatically sends messages to a list of telegram groups, within a given time interval
# Retrieve api_id and hash from my.telegram.org and insert within quotation marks.
# @author GG
# @version 1.0

if __name__ == '__main__':
    api_id = ''
    api_hash = ''
    client = TelegramClient('Shiller9000', api_id, api_hash)
    channel_list = fetch_list()
    message = fetch_text()

client.start()

for var in channel_list:
    time.sleep(10)
    result = client(functions.channels.JoinChannelRequest(
        channel=var
    ))

i = 0

while True:

    destination_channel_username = channel_list[i]
    entity = client.get_entity(destination_channel_username)
    client.send_message(entity, message)

    i = i + 1
    time.sleep(20)

    if i == len(channel_list):
        print("Last index reached, 10 second sleep.")
        i = 0
        time.sleep(1800)

client.run_until_disconnected()
