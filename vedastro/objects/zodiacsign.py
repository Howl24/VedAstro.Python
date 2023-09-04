import VedAstro.Library as library

from vedastro.objects import ZodiacName
from vedastro.objects.angle import Angle


class ZodiacSign():

    def __init__(self, sign_name: ZodiacName, degrees_in_sign: Angle):
        self.zodiac_name = sign_name
        self.degrees_in_sign = degrees_in_sign
    #
    # def get_sign_name(self):
    #     return library.ZodiacSign.GetSignName()
    #
    # def get_degrees_in_sign(self):
    #     return library.ZodiacSign.GetDegreesInSign()
    #
    #
