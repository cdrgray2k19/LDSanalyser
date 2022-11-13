from LDS import *
import pygame as pg
import sys


WIDTH = 1400
HEIGHT = 800
TITLE = 'LDS GUI'

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

class textBox:

    def __init__(self, x, y, msg):
        self.x = x
        self.y = y
        self.msg = msg


        self.font = pg.font.Font('freesansbold.ttf', 20)
        self.text = self.font.render(self.msg, True, (0,0,0))
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.x+self.textRect.width/2, self.y+self.textRect.height/2)

    def display(self):
        screen.blit(self.text, self.textRect)

fieldNames = ["Daily Mean Temperature (0900-0900) (°C)", "Daily Total Rainfall (0900-0900) (mm)" ,"Daily Total Sunshine (0000-2400) (hrs)","Daily Mean Windspeed (0000-2400) (kn)","Daily Maximum Gust (0000-2400) (kn)","Daily Maximum Relative Humidity %","Daily Mean Total Cloud (oktas)","Daily Mean Visibility (Dm)","Daily Mean Pressure (hPa)","Daily Mean Wind Direction (o)","Daily Max Gust Corresponding Direction (o)"]

options = []
xPos = 100
yPos = 100
for i in range(0, len(fieldNames)):
    new = textBox(xPos,yPos + (50*i),str(i) + "  -  " +fieldNames[i])
    options.append(new)

inp = ""
input_active = True

font = pg.font.Font('freesansbold.ttf', 20)
text = font.render(inp, True, (0,0,255), (0,255,0))
textRect = text.get_rect()
textRect.center = (100, HEIGHT*0.9)

enterMsg = textBox(100, HEIGHT*0.9 - 50, "Enter Field Index:")

inputMsgMap = {"0": 1, "1": 2, "2": 3, "3": 4, "4": 6, "5": 7, "6": 8, "7": 9, "8": 10, "9": 11, "10": 13}

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse = pg.mouse.get_pos()
            if box.x <= mouse[0] <= box.x+box.width and box.y <= mouse[1] <= box.y+box.height:
                input_active = True
            else:
                input_active = False

        elif event.type == pg.KEYDOWN and input_active:
            if event.key == pg.K_RETURN:
                try:
                    collumn = inputMsgMap[inp]
                    plot(collumn, placesMap, data, ignoredVal, length, increments[collumn])
                except:
                    pass
                inp = ""
            elif event.key == pg.K_BACKSPACE:
                inp =  inp[:-1]
            else:
                inp += event.unicode

    
    
    screen.fill((255, 255, 255))
    for msg in options:
        msg.display()
    enterMsg.display()



    text = text = font.render(inp, True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (100 + textRect.width/2, HEIGHT*0.9+textRect.height/2)
    color = (0,0,0)
    if input_active:
        color = (0,255,0)
    box = pg.draw.rect(screen, color, (textRect.centerx-textRect.width/2-10, textRect.centery-textRect.height/2-10, max(textRect.width+20, 200), textRect.height+20), 2)
    screen.blit(text, textRect)

    pg.display.update()


pg.quit()
sys.exit()