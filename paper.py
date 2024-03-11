import nextcord
from nextcord.ext import commands
import random
from nextcord import slash_command,Interaction,SlashOption
from nextcord.abc import GuildChannel
intens = nextcord.Intents.all()
intens.members=True
client = commands.Bot(command_prefix="!", intents=intens,case_insensitive=False)
#list
choices=["paper","rock","scissors"]

@client.event
async def on_ready():
   print("""bot is ready
            ____________________""")
@client.event
async def on_member_join(member):
     print(f"{member} is joined")










@client.slash_command(name="roshambo_rock", description="You chose rock", guild_ids=[1206906212889919518])
async def roshambo_rock(interaction: Interaction):
    computer_choice = random.choice(choices)

    if computer_choice == "paper":
        await interaction.response.send_message(" paper, you lost!")
    elif computer_choice == "rock":
        await interaction.response.send_message(" rock, it's a tie. Try again!")
    elif computer_choice == "scissors":
        await interaction.response.send_message("scissors, you win!")



@client.slash_command(name="roshambo_paper",description="u 'll chose paper ",guild_ids=[1206906212889919518])
async def roshambo_paper(interaction:Interaction):
     computer_choice = random.choice(choices)
     if computer_choice =="paper":  
        await interaction.response.send_message("paper,it is tied,try again")
     elif computer_choice =="rock":
         await interaction.response.send_message("rock,u win!!!!")
     elif computer_choice =="scissors" :
         await interaction.response.send_message("scissors,oh u lost!") 


@client.slash_command(name="roshambo_scissors",description="u 'll chose scissors ",guild_ids=[1206906212889919518])
async def roshambo_scissors(interaction:Interaction,):
     computer_choice = random.choice(choices)
     if computer_choice =="paper":  
        await interaction.response.send_message(f"parer ,u win!")
     elif computer_choice =="rock":
         await interaction.response.send_message(f"rock,u lost!!!")
     elif computer_choice =="scissors" :
         await interaction.response.send_message(f"scissors,it is tie") 









client.run("MTIxNjg2NDA4MDU0ODA3MzYzMw.G1vQkU.-jR7WotQHQ5LChY9K5Ojn01x9EpllYVKYYWRd0")
