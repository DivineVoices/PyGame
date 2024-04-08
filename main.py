import pygame
import time

from Settings import *
from GameObject import *
from Map import *
from Menus import *

class Game:
    def __init__(self):
        self.running = True
        self.ui_hide_timer = 0
        self.prev_BlueFlow = 0
        self.prev_RedFlow = 0
        self.prev_WhiteFlow = 0

        self.ground = [
            StaticObject(self, -200, 200, 400, 100, "Ground"),
            StaticObject(self, 200, 100, 100, 200, "Wall"),
            StaticObject(self, 150, 0, 100, 50, "Platform"),
        ]

        self.map = Map(10, 1, 50, *[loadTile(path) for path in TILES])

        self.main_menu = Menu(self, 500, 500)

        self.leftPressed = False
        self.rightPressed = False
        self.up = False
        self.down = False
        self.tabPressed = False

        self.player = Player(self, 0, 0, 50, 75)
        self.camera = Camera(self, Vector2(0, 0), 5, self.player)
        self.clock = py.time.Clock()
        self.deltatime = 0

    def update(self):
        self.camera.update()

    def draw(self):
        pygame.font.init()
        my_font = pygame.font.SysFont('Resources/GEO_AI__.TTF', 64)
        self.map.blit(SCREEN, self.camera)

        if self.tabPressed:
            self.main_menu.blit(SCREEN)

        CardPosition = []
        
        if (self.BlueFlow != self.prev_BlueFlow or 
            self.RedFlow != self.prev_RedFlow or 
            self.WhiteFlow != self.prev_WhiteFlow):
            self.ui_hide_timer = time.time() 
            self.hide_ui = False
        else:
            if time.time() - self.ui_hide_timer >= 3:
                self.hide_ui = True
        self.prev_BlueFlow = self.BlueFlow
        self.prev_RedFlow = self.RedFlow
        self.prev_WhiteFlow = self.WhiteFlow
        for i in range(len(self.InvContents)):
            CardScale = self.CardScale[i]
            CardImage = None
            if self.InvContents[i] == 'Dash':
                CardImage = py.image.load("Resources/Godspeed_Soul_Card.webp")
            elif self.InvContents[i] == 'Jump+':
                CardImage = py.image.load("Resources/Elevate_Soul_Card.webp")
            elif self.InvContents[i] == 'Bomb':
                CardImage = py.image.load("Resources/Purify_Soul_Card.webp")
            
            if CardImage is not None:
                CardWidth = int(CardImage.get_width())
                CardHeight = int(CardImage.get_height() * CardScale)
                CardPosition.append((
                    ((WIDTH - (CardImage.get_width() * 3)) - ((CardImage.get_width() * -i) - 169) - CardImage.get_width()),
                    (HEIGHT + 100) - CardHeight
                ))

        for i, (content, scale) in enumerate(zip(self.InvContents, self.CardScale)):
            CardImage = None
            if content == 'Dash':
                CardImage = py.image.load("Resources/Godspeed_Soul_Card.webp")
            elif content == 'Jump+':
                CardImage = py.image.load("Resources/Elevate_Soul_Card.webp")
            elif content == 'Bomb':
                CardImage = py.image.load("Resources/Purify_Soul_Card.webp")

            if CardImage is not None:
                CardWidth = int(CardImage.get_width())
                CardHeight = int(CardImage.get_height() * scale)
                CardImage = py.transform.scale(CardImage, (CardWidth, CardHeight))
                CardRect = CardImage.get_rect(topleft=CardPosition[i])
                SCREEN.blit(CardImage, CardRect)

                

        ImageB = py.transform.scale(py.image.load("Resources/collectible_fleur.png"), (64, 64))
        tracks = [self.BlueFlow, self.RedFlow, self.WhiteFlow]
        colors = [(51, 96, 163), (173, 56, 45), (242, 246, 252)]
        if self.hide_ui == False:
            for i, (track, color) in enumerate(zip(tracks, colors)):
                track_text = my_font.render(str(track), True, color)
                SCREEN.blit(ImageB, (64, 12 + i * 64))
                SCREEN.blit(track_text, (24, 24 + i * 64))

        py.display.flip()

    def inv(self):
        self.BlueFlow = 0
        self.WhiteFlow = 0
        self.RedFlow = 0
        self.InvContents = []
        self.CardScale = [0, 0, 0]

    def run(self):
        selected_card = 0 
        self.inv()
        while self.running:
            SCREEN.fill(SKY)
            self.deltatime = self.clock.get_time() / 1000
            self.clock.tick(60)
            self.update()
            self.draw()
           
            if self.leftPressed:
                self.player.transform.position.moveX(-10)
            if self.rightPressed:
                self.player.transform.position.moveX(10)
            if self.up:
                self.player.transform.position.moveY(-10)
            if self.down:
                self.player.transform.position.moveY(10)
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False
                if event.type == py.KEYUP:
                    if event.key == py.K_q:
                        self.leftPressed = False
                    if event.key == py.K_d:
                        self.rightPressed = False
                    if event.key == py.K_z:
                        self.up = False
                    if event.key == py.K_s:
                        self.down = False
                    if event.key == py.K_b:
                        self.BlueFlow += 1
                    if event.key == py.K_r:
                        self.RedFlow += 1
                    if event.key == py.K_w:
                        self.WhiteFlow += 1
                    if event.key == py.K_i:
                        if len(self.InvContents) >= 3:
                            self.InvContents.pop(0)
                        self.InvContents.append("Dash")
                    if event.key == py.K_o:
                        if len(self.InvContents) >= 3:
                            self.InvContents.pop(0)
                        self.InvContents.append("Jump+")
                    if event.key == py.K_p:
                        if len(self.InvContents) >= 3:
                            self.InvContents.pop(0)
                        self.InvContents.append("Bomb")
                    if event.key == py.K_1:
                        selected_card = 0
                    if event.key == py.K_2:
                        selected_card = 1
                    if event.key == py.K_3:
                        selected_card = 2

                if event.type == py.KEYDOWN:
                    if event.key == py.K_q:
                        self.leftPressed = True
                    if event.key == py.K_d:
                        self.rightPressed = True
                    if event.key == py.K_z:
                        self.up = True
                    if event.key == py.K_s:
                        self.down = True
                    if event.key == py.K_SPACE:
                        self.player.jump()
                    if event.key == py.K_TAB:
                        if self.tabPressed:
                            self.tabPressed = False
                        else:
                            self.tabPressed = True

            self.CardScale = [0.5, 0.5, 0.5]
            self.CardScale[selected_card] = 1

            


g = Game()
g.run()
