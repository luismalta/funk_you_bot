async def connect_user_voice(message):
        canal = message.author.voice.channel
        await canal.connect()

async def disconnect_user_voice(message):
        canal = message.author.voice.channel
        await canal.disconnet()