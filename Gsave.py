import discord


async def Gsaveon(message):
    await message.delete()
    await message.channel.send(f"{message.author.mention}, 이런 싹바가지 없는놈! 교리에 손을 대다니!")
    await message.author.edit(nick="교리에 손을 댄 싹바가지 없는 놈")