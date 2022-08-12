from discord_webhook import DiscordWebhook, DiscordEmbed
import discord
from discord.ext import commands
import time



bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help


@bot.command()
async def hablar(ctx,   keko, *, mensaje):
    await ctx.message.delete()
    await ctx.send("...", delete_after=0)
    time.sleep(3)
    
    webhook = DiscordWebhook(url=''#obtener un webhook,
                         username=f"{keko}" ,content=f"{mensaje}", avatar_url=f"https://www.habbo.es/habbo-imaging/avatarimage?user={keko}&action=none&direction=2&head_direction=2&gesture=std&size=l")
    response = webhook.execute()
@bot.event
async def on_ready():
    print("BOT listo!")
bot.run("")

