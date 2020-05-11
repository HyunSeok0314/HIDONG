import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("완료")
    game = discord.Game("'!도움말'로 명령어 확인")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    id = message.author.id
    channel = message.channel



    if message.content.startswith("!도움말"):
        await message.channel.send(message.author.mention+"```css\n동이루봇 사용법\n#1. '동이루'를 붙어 봇을 사용한다\n#2. '동이루 안녕'등 명령어들이 있다(점점 추가 함)\n#3. '!문의'로 문의\n#4. '!관리자 [정보/소환]으로 관리자의 정보를 확인할 수 있다'\n...```")
        
    elif message.content.startswith("!문의"):
        atr = message.guild.get_member(653172394499768322)
        atr1 = message.guild.get_member(369371525146476546)
        msg = message.content[4:]
        if msg == "":
            await message.channel.send(message.author.mention + "```css\n문의 내용을 적어주세요.(+문의 [내용])\n```")
        else:
            await atr1.send(message.author.mention + " : " + msg)
            await atr.send(message.author.mention + " : " + msg)
            await message.channel.send(message.author.mention + "```css\n정상적으로 문의를 보냈습니다.\n```")

    elif message.content.startswith("!관리자"):
        atr = message.guild.get_member(369371525146476546)
        msg = message.content[5:]
        if msg == "소환":
            await atr.send(message.author.mention + "님이 동이루방에서 당신을 부릅니다")
            await message.channel.send(message.author.mention + "```css\n정상적으로 메세지를 보냈습니다.\n(다소 시간이 걸릴 수 있음.)\n```")
        elif msg == "정보":
            await message.channel.send(message.author.mention + "```css\n키 : 182\n외모 : 씹상타치\n(ex: 공 유)\n전번 : 01056551737\n[추가중...]\n```")
        else:
            await message.channel.send(message.author.mention + "```css\n내용을 적어주세요.(+관리자 [정보/소환])\n```")



    elif message.content.startswith("동이루 안녕"):
        await message.channel.send("안녕하세용")
    elif message.content.startswith("동이루 뭐해"):
        await message.channel.send("뭐할지 고민중이에용>3<")
    elif message.content.startswith("동이루 엄마"):
        await message.channel.send("선은 지킵시다 ^^7")
    elif message.content.startswith("동이루 바보"):
        await message.channel.send("미안해용 ㅠㅠ")
    elif message.content.startswith("동이루 병신"):
        await message.channel.send("선은 지킵시다 ^^7")
    elif message.content.startswith("동이루 ㅂㅅ"):
        await message.channel.send("선은 지킵시다 ^^7")
    elif message.content.startswith("동이루 시발"):
        await message.channel.send("선은 지킵시다 ^^7")
    elif message.content.startswith("동이루 ㅅㅂ"):
        await message.channel.send("선은 지킵시다 ^^7")
    elif message.content.startswith("동이루 씨발"):
        await message.channel.send("선은 지킵시다 ^^7")
    elif message.content.startswith("동이루 넌 누구야"):
        await message.channel.send("저는 모두의 친구입니당 ^^!")
    elif message.content.startswith("동이루 잘가"):
        await message.channel.send("내일 또 봐용")
    elif message.content.startswith("동이루"):
        await message.channel.send("넹^-^")





access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
















