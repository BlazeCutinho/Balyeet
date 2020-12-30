import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title="Balyeet's Help Center",
            description="An Automatic Help Command",
            colour=discord.Colour.blue()
        )

        embed.set_footer(text="I'm Smart")
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/699819594478518392/786056321237254144/Blaze.jpg')
        embed.add_field(name='Help',
                        value="Fun:\n\n "
                              ".8ball (A Mystery Game with an 8Ball!)\n "
                              ".hello (Hi!)\n "
                              ".reply (Yes or No?)\n "
                              ".say (Say Anything..)\n "
                              ".ping (Pong! [Latency])\n "
                              "\n\n "
                              ""
                              "Moderation:\n\n "
                              ".ban (Ban a user!)\n "
                              ".clear (Clear the chat! - [Specify the amount!])\n "
                              ".kick (Kick a user!)\n "
                              ".mute (Mute a user! - [Remember to create a 'MUTED' role!])\n "
                              ".unban (Unban a user!)\n "
                              ".unmute (Unmute a user!)\n"
                              "\n ",
                        inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.remove_command("help")
    bot.add_cog(Help(bot))
