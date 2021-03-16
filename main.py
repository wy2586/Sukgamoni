import discord
from class_cmd import Command, Commands
import Gsave

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    global unron, suk, morningsuk
    print(client.user.id)
    game = discord.Game("石을 맞이하라")
    await client.change_presence(status=discord.Status.online, activity=game)
    unron = 0
    suk = 0
    morningsuk = 0
    embed = discord.Embed(title="石가모니 기상", description="너희들의 신 石가모니가 시작되었다",
                          color=0x62c1cc)
    embed.set_image(url="https://images-ext-1.discordapp.net/external/HSo-_A26Gpv9mJ7Nw1BojY-Pc7SgWCCjlTBPf_7XKzc/%3Fscode%3Dmtistory2%26fname%3Dhttps%253A%252F%252Ft1.daumcdn.net%252Fcfile%252Ftistory%252F9944E3455C924E9E2D/https/img1.daumcdn.net/thumb/R800x0/")
    await client.get_channel(637624439777001494).send(embed=embed)


@client.event
async def on_message(message):
    global unron, suk, morningsuk
    if message.author.bot:
        return None

    for cmd in Commands:
        await cmd.checkAndRun(message)

    if unron == 1:
        await message.delete()
    else:
        pass

    if suk == 1:
        if message.content.startswith("석멘") or message.content.startswith("/석멘"):
            pass
        else:
            await message.delete()
    else:
        pass

    if morningsuk == 0:
        if message.content.startswith("석모닝"):
            morningsuk = 1
            await message.channel.send(f"{message.author.mention}, 즐거운 아침인사!")
        else:
            pass
    else:
        pass

    if str(message.channel) == "石교-교리":
        await message.delete()
        await message.channel.send(f"{message.author.mention}, 이런 싹바가지 없는놈! 교리에 손을 대다니!")
        await message.author.edit(nick="교리에 손을 댄 싹바가지 없는 놈")
    else:
        pass


@Command("/언론탄압")
async def cmd_언론탄압(message):
    global unron
    sel = message.content.split(" ")[1]
    if str(sel) == "시작":
        unron = 1
        await message.channel.send(f"{message.author.mention}, 언론탄압이 시부럴 시작됐어!")
    elif str(sel) == "종료":
        unron = 0
        await message.channel.send(f"{message.author.mention}, 언론탄압이 시부럴 끝났어!")


@Command("/석전해주기")
async def cmd_석전해주기(message):
    d = message.content[7:]
    await message.delete()
    await message.channel.send(d)


@Command("/석멘타임")
async def cmd_석멘타임(message):
    global suk
    sel = message.content.split(" ")[1]
    if str(sel) == "시작":
        suk = 1
        await message.channel.send(f"{message.author.mention}, 석멘타임! 이제 말할때는 석멘 [내용]으로 해야해!")
    elif str(sel) == "종료":
        suk = 0
        await message.channel.send(f"{message.author.mention}, 석멘타임이 종료되었다")


client.run("ODAwOTcxMDgyNzU5Nzk4ODE1.YAZ4cw.bRqRX1WJOUXCVGIovojKUgiZ0Os")