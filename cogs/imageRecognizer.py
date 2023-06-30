from io import BytesIO
from discord.ext import commands
import requests
from PIL import Image
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
from tensorflow.keras import models

TARGET_RESOLUTION = 64


class imageRecognizer(commands.Cog):
    def init(self, client):
        self.client = client

    @commands.command()
    async def imageReader(self, ctx):

        print("test")

        url = ctx.message.attachments[0]
        img_data = requests.get(url)
        pilImage = Image.open(BytesIO(img_data.content))
        pilImage.resize((TARGET_RESOLUTION, TARGET_RESOLUTION), Image.ANTIALIAS)

        if os.path.exists('./NeuralNetwork/Dog_Classifier.model'):
            print("test2")
            model = models.load_model('./NeuralNetwork/Dog_Classifier.model')
            model.summary()

            prediction = model.predict(np.array([str(pilImage)]) / 255)
            index = np.argmax(prediction)

            print(index)


async def setup(client):
    await client.add_cog(imageRecognizer(client))