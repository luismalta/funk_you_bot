import requests

async def xingamento(message):
    response = requests.get('http://xinga-me.appspot.com/api').json()['xingamento']
    await message.channel.send(response)