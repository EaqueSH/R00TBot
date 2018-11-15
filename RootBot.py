import discord
import asyncio
from discord.ext.commands import Bot


TOKEN = "XXXXXXXXXXXXXXXXXXX"

client = Bot(command_prefix=["../"])
client.remove_command("help")



def ChallOne(message):
    if message == "EaqueStackTheBest":
        return ":white_check_mark: Succesfully Thx for use my bot bro ;)"
    else:
        return ":x: incorrect reply"

@client.event
async def on_ready():
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print("link invitation: https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8".format(client.user.id))
    print("Dev by : EaqueStacks")


@client.command(aliases=["help"])
async def helper():
    embed = discord.Embed(title="what you can a do :white_check_mark: :", colour=discord.Colour(0x4435e9), url="https://metaxploit.tk")

    embed.set_thumbnail(url=client.user.avatar_url)
    embed.set_author(name="Username: {}".format(client.user.name), url="https://metaxploit.tk", icon_url="{}".format(client.user.avatar_url))
    embed.set_footer(text="Bot Create by EaqueStack", icon_url="https://cdn.discordapp.com/attachments/512659588101701636/512670657415479299/5348ce43a934b029a4204ccb55d02d50.jpg")

    embed.add_field(name="Easy chall :grinning:", value="`1- ../chall1Details`\n`2- ../chall2`")
    embed.add_field(name="Medium chall :grimacing:", value="`3- ../chall3`\n`4- ../chall4`")
    embed.add_field(name="Hot chall :rage:", value="`5- ../chall5`\n`6- ../chall6`")

    await client.say(embed=embed)


@client.command(aliases=["chall1Details"])
async def chOne():
    embed = discord.Embed(title="Welcome to Challenge 1 this name is MD5Decrypt", colour=discord.Colour(0x4435e9), url="https://metaxploit.tk")

    embed.set_thumbnail(url=client.user.avatar_url)
    embed.set_author(name="Username: {}".format(client.user.name), url="https://metaxploit.tk", icon_url="{}".format(client.user.avatar_url))
    embed.set_footer(text="Bot Create by EaqueStack", icon_url="https://cdn.discordapp.com/attachments/512659588101701636/512670657415479299/5348ce43a934b029a4204ccb55d02d50.jpg")

    embed.add_field(name="what are the rules of the chall:thinking:", value="```Michel your brother gives you his computer the only condition: You do not have the right to touch the text file called \"pswd.txt\". You are curious and mean so you open the text file and you see a password \"2e142fdb4ac84a7e9ff9ba56626c252cc6abdfb641c9477559ac6731f77f1124\". You test the password everywhere however it does not work. Try to find the password good luck :)```")
    embed.add_field(name="Command: ", value="`../chall1 + <reply>`")
    await client.say(embed=embed)
    


@client.command(aliases=["chall1"])
async def challmd5(*args):
    await client.say(ChallOne(*args))



	





client.run(TOKEN)
