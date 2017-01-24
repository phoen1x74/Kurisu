import discord
from discord.ext import commands
from sys import argv

class Memes:
    """
    Meme commands
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    async def _meme(self, ctx, msg):
        author = ctx.message.author
        if ctx.message.channel.name[0:5] == "help-" or (self.bot.nomemes_role in author.roles):
            await self.bot.delete_message(ctx.message)
            try:
                await self.bot.send_message(author, "Meme commands are disabled in this channel, or your priviledges have been revoked.")
            except discord.errors.Forbidden:
                await self.bot.say(author.mention + " Meme commands are disabled in this channel, or your priviledges have been revoked.")
        else:
            await self.bot.say(ctx.message.author.display_name + ": " + msg)

    # list memes
    @commands.command(name="listmemes", pass_context=True)
    async def _listmemes(self, ctx):
        """List meme commands."""
        # this feels wrong...
        funcs = dir(self)
        msg = "```\n"
        for func in funcs:
            if func != "bot" and func[0] != "_":
                msg += func + "\n"
        msg += "```"
        await self._meme(ctx, msg)

    # 3dshacks memes
    @commands.command(pass_context=True, hidden=True)
    async def phoenix(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://media.giphy.com/media/Lt20BESX85xoQ/giphy.gif")

    @commands.command(pass_context=True, hidden=True)
    async def serrara(self, ctx):
        """Memes."""
        await self._meme(ctx, "https://media.giphy.com/media/DWHy12Gy3W19K/giphy.gif")

    @commands.command(pass_context=True, hidden=True)
    async def s_99(self, ctx):
        """Memes."""
        await self._meme(ctx, "**ALL HAIL BRITANNIA!**")

    @commands.command(pass_context=True, hidden=True)
    async def pixl(self, ctx):
        """Memes."""
        await self._meme(ctx, "```all heil creamsicle```")

    @commands.command(pass_context=True, hidden=True)
    async def banned(self, ctx):
        """Memes."""
        await self._meme(ctx, "https://cdn.discordapp.com/attachments/270629800383741954/272416630565240832/ISmLp.gif")

    @commands.command(pass_context=True, hidden=True)
    async def megumi(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/GMRp1dj.jpg")

    @commands.command(pass_context=True, hidden=True)
    async def inori(self, ctx):
        """Memes."""
        await self._meme(ctx, "https://i.imgur.com/WLncIsi.gif")

    @commands.command(pass_context=True, hidden=True)
    async def inori2(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/V0uu99A.jpg")

    @commands.command(pass_context=True, hidden=True)
    async def inori3(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/so8thgu.gifv")
        
    @commands.command(pass_context=True, hidden=True)
    async def kina(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/8Mm5ZvB.jpg")

    @commands.command(pass_context=True, hidden=True)
    async def r34(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/sjQZKBF.gif")

    @commands.command(pass_context=True, hidden=True)
    async def lenny(self, ctx):
        """Memes."""
        await self._meme(ctx, "( ͡° ͜ʖ ͡°)")

    @commands.command(pass_context=True, hidden=True)
    async def rip(self, ctx):
        """Memes."""
        await self._meme(ctx, "Press F to pay respects.")

    @commands.command(pass_context=True, hidden=True)
    async def permabrocked(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/ARsOh3p.jpg")

    @commands.command(pass_context=True, hidden=True)
    async def knp(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/EsJ191C.png")

    @commands.command(pass_context=True, hidden=True)
    async def xarec(self, ctx):
        """Memes."""
        await self._meme(ctx, "https://i.imgur.com/wRVuidH.gif")

    @commands.command(pass_context=True, hidden=True)
    async def clap(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/UYbIZYs.gifv")

    @commands.command(pass_context=True, hidden=True)
    async def ayyy(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/bgvuHAd.png")

    @commands.command(pass_context=True, hidden=True)
    async def hazel(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/vpu8bX3.png")

    @commands.command(pass_context=True, hidden=True)
    async def love(self, ctx):
        """Memes."""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(ctx.message.author, "You know I'll always love you, even if we can't tell anyone.")

    # Cute commands :3
    @commands.command(pass_context=True, hidden=True)
    async def headpat(self, ctx):
        """Cute"""
        await self._meme(ctx, "http://i.imgur.com/7V6gIIW.jpg")

# Load the extension
def setup(bot):
    bot.add_cog(Memes(bot))
