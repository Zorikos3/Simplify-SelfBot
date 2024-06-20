#IMPORTS: & INSTALLS - Open command prompt and write "pip install discord==1.7.3" and "pip install discord.py==1.7.3"
import discord
import time
from discord.ext import commands


token = "Your Discord Token" #Your Discord Token

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", self_bot=True, intents=intents) #Creating Client & Prefix


@client.event #Event Creation
async def on_ready():
    #Write Startup
    print("Simplify Status: Ready For Use.")
    print("-----------------------------")
    print("Command Prefix: ! | !cmds For Command List.")
    #sussy ahh prefix text


#Commands
@client.command() #First Command Creation
async def test(ctx):
    print("Test command was used.")
    await ctx.send("Test Command Was Used")
    message1 = await ctx.send("Delete Fast")
    await message1.delete()  
      
@client.command()
async def cmds(ctx):
    commands = client.commands
    command_list = [command.name for command in commands]
    commands_str = '\n'.join(command_list)
    await ctx.send(f"Available Commands:\n{commands_str}")
    
@client.command()
async def spam(ctx, message: str, count: int, delay: float):
     sentmessages = 0 
     for i in range(count):
        sentmessages += 1 
        time.sleep(delay) 
        await ctx.send(message)
        print(f"Message {message} Sent | {sentmessages}/{count}")
    
@client.command()
async def ms(ctx):
    ping = round(client.latency * 1000)
    await ctx.send(f"Current MS: {ping}ms")
    
@client.command()
async def pfp(ctx, user: discord.User): 
   avatar_url=user.avatar_url
   await ctx.send(avatar_url)
         
@client.command()
async def info(ctx, user: discord.User):
    user_id = user.id 
    username = user.name
    tag = user.discriminator
    created_at = user.created_at.strftime("%Y-%m-%d %H:%M:%S")
    response = f'User ID: {user_id}\nUsername: {username+"#"+tag}\nAccount Creation Date: {created_at}'
    await ctx.send(response)
    
@client.command()
async def react(ctx):
    thumbs_up = '\N{THUMBS UP SIGN}'
    await ctx.message.add_reaction(thumbs_up)
     
@client.command()
async def pingall(ctx):
    members = ctx.guild.members
    non_bot_members = [member for member in members if not member.bot]

    for i in range(0, len(non_bot_members), 10):
        member_chunk = non_bot_members[i:i+10]
        members_text = ' '.join(member.mention for member in member_chunk)
        await ctx.send(members_text)
        
@client.command()
async def bio(ctx):
    link = "https://www.boxxing.club"
    message = f"**Zor BioLink: {link}**"
    await ctx.send(message)
    
@client.command()
async def rizz(ctx):
    rizz_up_lines = [
        "Are you a parking ticket? cuz you've got FINE written all over you..",
        "sorry to bother you, but my phone must be broken because it doesn’t seem to have your number in it...",
        "I’m no cashier but you got a couple things on you I’d like to check out <3"
    ]
    if not hasattr(ctx.bot, 'rizz_index'):
        ctx.bot.rizz_index = 0
    rizz_up_line = rizz_up_lines[ctx.bot.rizz_index]
    ctx.bot.rizz_index = (ctx.bot.rizz_index + 1) % len(rizz_up_lines)
    await ctx.send(rizz_up_line)
    
client.run(token, bot=False) #Running sigma client and saying that bot isnt bot because we human
