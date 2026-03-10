#import module
import pygame
#start module
pygame.mixer.init()
#load music
pygame.mixer.music.load(r"Estudying\Python\World 1\music.mp3")
#play music
pygame.mixer.music.play()
#while play
while pygame.mixer.music.get_busy():
  pygame.time.wait(100)
  