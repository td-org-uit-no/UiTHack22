import os
import pygame
from pygame import *
from collections import Counter


SCREEN_X = 4000
SCREEN_Y = 2000

BLACK = (0,0,0)
WHITE = (255,255,255)
BROWN =((100,40,0))
MARRON = ((115,0,0))
COFFE_BROWN =((200,190,140))

path =  "/home/hauk/uithack/UiTHack22/Crypto/tmpname_freqanalysis/UitHack-2022_freq"
string = "uithacktheempireattackendor"

class Pic():
    def __init__(self,path,string):
        self.screen = pygame.display.set_mode((SCREEN_X,SCREEN_Y),0,32)
        self.path =  path
        self.string = string

    def draw(self):
        self.screen.blit(self.screen, (0, 0))


    def count(self,string):

        print(len(string))
        return Counter(string)

    def gen_path(self,path,file):

        new_path = path + '/'+file
        return new_path 


    def append_path(self,path):

        imgs = []
        for file in os.listdir(path):
            imgs.append(self.gen_path(path,file))

        return imgs

    def map_imgs_to_letter(self,path,string):

        img_files = self.append_path(path)
        dic = {}
        for char in string:
            for img in img_files:
                if (img.endswith(char +'.png')):
                    dic.update({char:img})      
        return dic

    def append_img(self,path,string):

        img_dic = self.map_imgs_to_letter(path,string)
        list_of_imgs = []
        for char in string:
            if char in img_dic:
                pic = img_dic.get(char)
                list_of_imgs.append(pic)

        return list_of_imgs

    def load_imgs(self,path,string):

        mem_img = []
        tmp_img = self.append_img(path,string)
        for file in tmp_img:
            new_img = pygame.image.load(file)
            mem_img.append(new_img.convert_alpha())

        return mem_img
    
    def show_imgs(self,path,string):
        
        for i in range (len((self.append_img(path,string)))):
            img = self.load_imgs(path,string)
            self.screen.blit(img[i],(120*i,750))
        
def main():

    pygame.init()

    # Drawing the screeen where the action is supose to happen
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)

    pic = Pic(path,string)
   

    # Creating a clockSS
    clock = pygame.time.Clock()

    # The main game-loop
    while True:

        timepass = clock.tick(30)/1000

       # Fill the screen with black
        screen.fill(COFFE_BROWN)

        pic.show_imgs(path,string)

        screen.blit(screen, (0, 0))

        pygame.display.flip()

        pygame.display.update()

        event = pygame.event.poll()

        if event:
            if event.type == pygame.QUIT:
                print("THE GAME QUITED")
                exit()
      



if __name__ == "__main__":

    main()
