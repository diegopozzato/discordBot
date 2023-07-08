from io import BytesIO
from discord.ext import commands
import requests
import cv2 as cv
import numpy as np
import os
from tensorflow.keras import models

TARGET_RESOLUTION = 64

class imageRecognizer(commands.Cog):
    def init(self, client):
        self.client = client

    @commands.command()
    async def imageReader(self, ctx):

        if os.path.exists('./NeuralNetwork/DogVsCat_Classificator.model'):
            model = models.load_model('./NeuralNetwork/DogVsCat_Classificator.model')

            try:
                
                url = ctx.message.attachments[0]
                resp = requests.get(url, stream=True).raw
                image = np.asarray(bytearray(resp.read()), dtype="uint8")
                image = cv.imdecode(image, cv.IMREAD_COLOR)
                img = cv.resize(image, (64, 64))

                prediction = model.predict(np.array([img]) / 255)
                index = np.argmax(prediction)

                if index == 1:
                    await ctx.reply("DOGGO")
                else:
                    await ctx.reply("CATTO")

            except:
                await ctx.reply("IMAGE ERROR! make sure you attached an image")





async def setup(client):
    await client.add_cog(imageRecognizer(client))