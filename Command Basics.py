from types import ModuleType
import discord
import random
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(command_prefix = "!", help_command=None)


def is_me(ctx):
    return ctx.author.id == 367740611538845696

def starts_with_a(msg):
    msg.content.startswith("a") or msg.content.startswith == "!purge"



@bot.command()
async def ping(ctx):
    await ctx.send("Pong!") 

@bot.command()
async def coinflip(ctx):
    num = random.randint(1,2)

    if num == 1:
        await ctx.send("Heads!")
    if num == 2:
        await ctx.send("Tails!")

@bot.command()
async def rps(ctx, hand):
    hands =["✌️","✋","👊"]
    bothand = random.choice(hands)
    await ctx.send(bothand)
    if hands == bothand:
        await ctx.send("DRAW!")
    elif hand == "✌️":
        if bothand == "👊":
            await ctx.send("I won!")
        if bothand == "✋":
            await ctx.send("You won!")
    elif hand == "✋":
        if bothand == "👊":
            await ctx.send("You won!")
        if bothand == "✌️":
            await ctx.send("I won!")
    elif hand == "👊":
        if bothand == "✋":
            await ctx.send("I won!")
        if bothand == "✌️":
            await ctx.send("You won!")


@bot.command(aliases = ["about"])
async def help(ctx):
    MyEmbed = discord.Embed(title = "Commands", description = "Commands to use for Kebab Bot", color = discord.Colour.dark_magenta())
    MyEmbed.set_thumbnail(url = "https://i.ytimg.com/vi/HfFx5UvzSxc/maxresdefault.jpg")
    MyEmbed.add_field(name = "!ping", value = "Says pong to you!", inline=False)
    MyEmbed.add_field(name = "!coinflip", value = "Play coinflip!", inline=False)
    MyEmbed.add_field(name = "!rps", value = "Play rock scissors paper!", inline=False)
    await ctx.send(embed = MyEmbed)


@bot.group()
async def edit(ctx):
    pass

@edit.command()
@commands.has_role("Shogun 将軍")
async def servername(ctx,*, input):
    await ctx.guild.edit(name = input)

@edit.command()
@commands.has_role("Shogun 将軍")
async def createtextchannel(ctx,*, input):
    await ctx.guild.create_text_channel(name = input)

@edit.command()
@commands.has_role("Shogun 将軍")
async def createvoicechannel(ctx,*, input):
    await ctx.guild.create_voice_channel(name = input)

@edit.command()
@commands.has_role("Shogun 将軍")
async def createrole(ctx,*, input):
    await ctx.guild.create_role(name = input)

@bot.command()
@commands.has_role("Shogun 将軍")
async def kick(ctx, member : discord.Member, *, reason = None):
    await ctx.guild.kick(member, reason = reason)

@bot.command()
@commands.has_role("Shogun 将軍")
async def ban(ctx, member : discord.Member, *, reason = None):
    await ctx.guild.ban(member, reason = reason)

@bot.command()
@commands.has_role("Shogun 将軍")
async def unban(ctx,*,input):
    name, discriminator = input.split("#")
    banned_members = await ctx.guild.bans()
    for bannedmember in banned_members:
        username = bannedmember.user.name
        disc = bannedmember.user.discriminator
        if name == username and discriminator == disc:
            await ctx.guild.unban(bannedmember.user)


#Error Handlers
@kick.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You dont have the necessary roles for this command")

@ban.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You dont have the necessary roles for this command")

@unban.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You dont have the necessary roles for this command")




#@commands.check(is_me)   #wheter check if your id match with author
#@commands.has_role("TEST ROLE")
#@commands.has_permissions(manage_messages = True)
@bot.command()
async def purge(ctx, amount, day = None, month : int = None, year : int = datetime.now().year):
    if amount == "/":
        if day == None or month == None:
            return
        else:
            await ctx.channel.purge(after = datetime(year, month, day)) #only deletes massages starts with a check = starts_with_a
    else:
        await ctx.channel.purge(limit = int(amount)+1)



@purge.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await  ctx.send("You have to specify either a date or number")
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("You can only have a slash or a number as the first input")




@bot.command()
async def mute(ctx, user : discord.Member):
    await user.edit(mute = True)

@bot.command()
async def unmute(ctx, user : discord.Member):
    await user.edit(mute = False)

@bot.command()
async def deafen(ctx, user : discord.Member):
    await user.edit(deafen = True)

@bot.command()
async def undeafen(ctx, user : discord.Member):
    await user.edit(deafen = False)

@bot.command()
async def voicekick(ctx, user = discord.Member):
    await user.edit(voice_channel = None)


@bot.command()
async def reload(ctx):
    bot.reload_extension("Cogs")

bot.load_extension("Cogs")
bot.run("TOKEN")