import random

from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['hi'])
    async def hello(self, ctx):
        user = ctx.message.author
        await ctx.send(f"Hello There {user.mention}!")

    @commands.command()
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send("{}".format(msg))

    @commands.command()
    async def reply(self, ctx, *, question):
        responses = ["yes", "maybe", "no"]
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

    @commands.command(aliases=['8ball', 'test'])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Reply hazy, try again.",
                     "Ask again later.",
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Very doubtful."]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


def setup(bot):
    bot.add_cog(Fun(bot))
