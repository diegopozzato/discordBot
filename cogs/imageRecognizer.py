from io import BytesIO
from discord.ext import commands
import requests
from PIL import Image

TARGET_RESOLUTION = 64


class imageRecognizer(commands.Cog):
    def init(self, client):
        self.client = client

    @commands.command()
    async def imageReader(self, ctx):
        url = ctx.message.attachments[0]
        img_data = requests.get(url)
        pilImage = Image.open(BytesIO(img_data.content))
        pilImage.resize((TARGET_RESOLUTION, TARGET_RESOLUTION), Image.ANTIALIAS)


async def setup(client):
    await client.add_cog(imageRecognizer(client))