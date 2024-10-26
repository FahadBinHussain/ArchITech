import discord
import re
import random

# Assuming your existing functions are defined here, including archiveLink

# Your bot's token
TOKEN = 'your_token_here'

# The channel ID you want to monitor for links
LINK_CHANNEL_ID = 123456789012345678

# Initialize the Discord client
client = discord.Client()

def archiveLink(url):
    domains = [
        'archive.today', 'archive.is', 'archive.fo',
        'archive.li', 'archive.md', 'archive.ph', 'archive.vn'
    ]
    domain = random.choice(domains)
    return f'https://{domain}?run=1&url={url}'

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Do not let the bot reply to itself
    if message.author == client.user:
        return

    # Check if the message is in the specified channel and contains a URL
    if message.channel.id == LINK_CHANNEL_ID:
        urls = re.findall(r'(https?://\S+)', message.content)
        if urls:
            for url in urls:
                # Generate the archive link for each URL found
                archive_url = archiveLink(url)
                # Send the archive link in the same channel
                await message.channel.send(archive_url)

# Start the bot
client.run(TOKEN)
