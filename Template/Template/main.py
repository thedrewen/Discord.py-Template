""" Importations """
from discord import *
import json


""" Client & Intents """
intents = Intents.default()
intents.message_content = True
intents.members = True

client = Client(intents=intents)
tree = app_commands.CommandTree(client)


""" Commandes """
from commandes.test import test_def # Import la commande test
test_def.commande(client, tree)


""" Events """
from event.ready import ready_def
ready_def.ready(client, tree)


""" Run """
with open('data/token.json', 'r') as file:
    token = json.load(file)
client.run(token)