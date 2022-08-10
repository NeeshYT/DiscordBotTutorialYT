import discord
from ka import keep_alive
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "!")
client.remove_command("help")

@client.event
async def on_ready():
    print(f"{client.user} is ready")

@client.command()
async def test(ctx):
    await ctx.send("Hi!")

@client.command()
async def help(ctx):
    em = discord.Embed(title="help")
    for cmd in client.walk_commands():
        des = cmd.description
        if not des or des == None or des == "":
            des = "No description provided"
        if cmd.signature is None:
            cmd.signature = ""
        em.add_field(name = f"`{cmd.name}{cmd.signature}`", value = des)
    await ctx.send(embed = em)

@client.command(description = "test")
async def embed(ctx):
    em = discord.Embed(
        title = "EMbed Title",
        description = "Embed Description",
        color = discord.Colour.red()
    )
    em.add_field(
        name = "Field Name",
        value = "Field Value"
    )
    em.add_field(
        name = "Field Name",
        value = "Field Value",
        inline = True
    )
    em.set_author(
        name = "Author Name",
        icon_url = ctx.author.avatar_url
    )
    em.set_footer(
        text = "Footer Text",
        icon_url = ctx.author.avatar_url
    )
    await ctx.send(embed = em)
    
for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        try:
            client.load_extension(f"cogs.{file[:-3]}")
        except Exception as e:
            print(e)
        
keep_alive()
client.run("MTAwMzAzNTkzOTIzNDM5NDEzMg.GzPmce.23EFu7j6JuYaVukF4M44UwzgSPr8cc-aINYv6E")

