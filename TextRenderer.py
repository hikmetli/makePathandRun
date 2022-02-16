from math import cos, radians, sin ,asin
import pygame,math
from Drawable import Drawable

class TextRenderer(Drawable):
    def __init__(self,surface : pygame,text, pos) -> None:
        super().__init__(surface, pos)
        self.textfont='freesansbold.ttf'
        self.textsize=20
        self.color=(155,155,155)
        self.text=text

    def typer(self):
        yazi=pygame.font.Font(self.textfont,self.textsize).render(self.text,True,self.color)
        self.surface.blit(yazi,self.pos)


