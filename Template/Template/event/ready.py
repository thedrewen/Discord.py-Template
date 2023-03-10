""" Importations """
from discord import *


""" Code """
class ready_def:
    def ready(client, tree):
        @client.event
        async def on_ready():
            print(f'Le bot {client.user} est connecté !')
            await tree.sync()