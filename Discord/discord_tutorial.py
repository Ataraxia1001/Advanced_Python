import discord
import os
import requests
import json
import random

from keep_alive import keep_alive


from replit import db
db = {} # replit database

intents = discord.Intents().all()
client = discord.Client(intents=intents)

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person!"
]


if "responding" not in db.keys():
    db["responding"] = True


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


def update_encoragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]


def delete_encouragement(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements


# async: These functions are able to pause their execution while waiting for an operation to complete, 
# allowing other operations to run during this waiting period.
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) # 0 is client
    
    
@client.event
async def on_message(message): 
    if message.author == client.user:
        return

    msg = message.content
    
    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote) # await: send or receive data over network. "wait for this operation to complete, but while waiting, let other operations run if they need to." 
        
    if db["responding"]:    
        options = starter_encouragements
        if "encouragements" in db.keys():
            options = options + db["encouragements"]
        
        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options)) 
    
    if msg.startswith("$new"):
        encouraging_message = msg.split("$new ", 1)[1]  # 1: split into 2 parts
        update_encoragements(encouraging_message)
        await message.channel.send("New encouraging message added.") 
        
    if msg.startswith("$del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("$del", 1)[1])
            delete_encouragement(index)
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)
        
    if msg.startswith("$list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)    
    
    if msg.startswith("$responding"):  
        value = msg.split("$responding ", 1)[1]
        
        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is off.")
            
keep_alive()
client.run(os.getenv('TOKEN'))