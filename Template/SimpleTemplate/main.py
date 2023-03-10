from discord import * # Import la librairie discord.py

intents = Intents.default() #Creer une variable "intents" qui contient les intents par défault de discord
intents.message_content = True #Configure l'intent message_content à True
intents.members = True #Configure l'intent members à True

client = Client(intents=intents) # Définie le Client/Bot avec ses intents
tree = app_commands.CommandTree(client) #Sur la base du client/bot créer une variable tree contenant les commandes slash.

# Commandes ;

@app_commands.command(description="Votre Description")
async def nom(interaction : Interaction): # On définie la commande avec "async def" puis on lui donne un nom (/nom) et on lui donne entre () une interaction qui est une Interaction de discord.
	#Code à éxécuter lors de le commande /nom
	await interaction.response.send_message("Message") # await signifie ici intéragir avec discord puis interaction qu'on reprend de la définition puis response pour répondre à l'intéraction de la commande puis send_message pour envoyer un message.

tree.add_command(nom) # Sur la variable tree, ajoute une commande slash avec la fonction add_command(NOM DE LA COMMANDE).

@client.event # Spécifie un événement qui créer une action
async def on_ready(): #Les noms des fonctions pour les evenement ont des nom précis
	await tree.sync() # Synchronise les commandes slash avec discord quand le bot est pret
	print(f"Le bot : {client.user} est connectés.")

with open("token.json", "r") as file: # Ouvre le fichier token.json
	import json 
	token = json.load(file) #  Grace a la librairie json import le token et le stocke dans une variable

client.run(token) # Allume le bot grace au token