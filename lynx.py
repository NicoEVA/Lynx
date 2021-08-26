import discord
from discord.ext import commands
import random as rnd
client = commands.Bot(command_prefix="!")


mlemdatabase = ["https://s2.best-wallpaper.net/wallpaper/iphone/1906/Wildcat-lynx-tongue-snow_iphone_750x1334.jpg",
"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F88%2Fd7%2F7b%2F88d77b79d5f741f49bebfdb021bbb874.jpg&f=1&nofb=1",
"https://render.fineartamerica.com/images/images-profile-flow/400/images/artworkimages/mediumlarge/3/lynx-tongue-tobias-luxberg.jpg",
"https://i.pinimg.com/originals/cd/bb/55/cdbb55f267253bf2932ea256be144928.jpg",
"https://i.pinimg.com/474x/7c/5e/f2/7c5ef2b9b81dc305a178ade5a7cb251d--lynx-wallpapers.jpg",
"https://img.welt.de/img/debatte/kolumnen/Fuhrs-Woche/mobile152189306/9342504287-ci102l-w1024/Luchse.jpg"]

filter1 = ["Lynx","lynx"]

filter2 = ["cool","nice","like","awesome","thank you", "Thank you"]
tired   = ["slow","tired","crisis"]
annoyed = ["done", "pissed", "annoyed","temper"]
yawn    = ["yawn","morning"]  
mlems   = ["mlem","tongue","clean"]
talkreq = ["speak", "talk", "talking", "Talk"]
Talk    = ["Mrrrrep", "Meow", "Prrrt", "Brrr", "Mow" , "Mew"]
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    for word in filter1:
        if word in message.content:
            for word2 in filter2:
                if word2 in message.content:
                    await message.channel.send("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flive.staticflickr.com%2F2511%2F3996846238_488bd07358_z.jpg&f=1&nofb=1")
            await client.process_commands(message)
            for word3 in tired:
                if word3 in message.content:
                    await message.channel.send('https://photorator.com/photos/images/sleepy-lynx--22818.jpg')
            await client.process_commands(message)
            for word4 in annoyed:
                if word4 in message.content:
                    await message.channel.send('https://i.imgur.com/HaaotHr.jpg')
            await client.process_commands(message)
            for word5 in yawn:
                if word5 in message.content:
                    await message.channel.send('https://i.pinimg.com/originals/c5/3b/0b/c53b0b122940dbb3648c8a993c801758.jpg')
            await client.process_commands(message)
            for word6 in mlems:
                if word6 in message.content:
                    await message.channel.send(str(mlemdatabase[rnd.randint(0,len(mlemdatabase)-1)]))
            await client.process_commands(message)        
            for word7 in talkreq:
                if word7 in message.content:
                    await message.channel.send(str([Talk[rnd.randint(0,len(Talk)-1)] for i in range(4)]).strip(",[]"))
                    await message.channel.send("I mean... what did you expect, huh?")
            await client.process_commands(message)
    await client.process_commands(message)




@client.command()
async def kf(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send("{} says:".format(ctx.message.author.mention))
    await ctx.send("<a:kittyflap:874338917279727696>")

@client.command()
async def kfb(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send("{} says:".format(ctx.message.author.mention))
    await ctx.send("<a:kittyflapback:839434951342686209>")

@client.command()
async def s1(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send("{} says:".format(ctx.message.author.mention))
    await ctx.send("<a:kittystageone:861687693997637662>")

@client.command()
async def s2(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send("{} says:".format(ctx.message.author.mention))
    await ctx.send("<a:kittstagetwo:861687693913227294>")

@client.command()
async def s3(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send("{} says:".format(ctx.message.author.mention))
    await ctx.send("<a:kittstagethree:861687693977452554>")



client.run('ODUwMzg4Njk1MTM5ODc2OTA0.YLpAMA.o9GiTuSbWAeDm4y2-SyZDhNaW6M')

   
    