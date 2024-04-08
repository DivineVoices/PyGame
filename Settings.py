import pygame as py

py.init()
py.font.init()
py.mixer.init()

# CONSTANT
WIDTH, HEIGHT = 800, 600
TITLE = "JEU VACHEMENT COOL"
GRAVITY = 9.8
RESOLUTION = 50
TILERESOLUTION = 16

# SET THE VALUES
SCREEN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption(TITLE)

# Fonts
Fonts = {
	"arial": py.font.Font("./Resources/arial.ttf", 12),
	"Grand arial": py.font.Font("./Resources/arial.ttf", 25),
}

CardImg = [
	py.transform.scale(py.image.load("Resources/Godspeed_Soul_Card.webp"), (100, 200)),
	py.transform.scale(py.image.load("Resources/Elevate_Soul_Card.webp"), (100, 200)),
	py.transform.scale(py.image.load("Resources/Purify_Soul_Card.webp"), (100, 200)),
]

Flower = py.transform.scale(py.image.load("Resources/collectible_fleur.png"), (64, 64))

Textures = [
	None,
	py.transform.smoothscale(py.image.load("Resources/Base pack/Tiles/box.png"), (RESOLUTION, RESOLUTION)),
	py.transform.smoothscale(py.image.load("Resources/Base pack/Tiles/castle.png"), (RESOLUTION, RESOLUTION)),
]

TILES = [
	"Tile/tile.tile",
	"Tile/tile2.tile",
	"Tile/tile3.tile",
	"Tile/tile4.tile"
]

# Color Palette
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
SKY = (130, 200, 255)
CYAN = (0, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)


