from random import randint
import pyautogui as pag
import sys
import cv2

rock_coordinates = {'o1':(858, 543, 895, 567), 'o2':(859, 484, 897, 515), 'o3':(914, 481, 948, 517), 'o4':(1024,4347,1058,4537)}
rock_pixel_colour = {'o1':(57,30,20), 'o2':(54,27,19), 'o3':(54,27,19), 'o4':(57,30,20)}
rock_pixel_coordinates = {'o1':(899,581), 'o2':(905,540), 'o3':(945,531), 'o4':(1055,476)}
rock_images = ['o1.jpg', 'o2.jpg', 'o3.jpg']
empty_rock_images = ['e1.jpg', 'e2.jpg', 'e3.jpg']
ore_coordinate = (1830, 1103)
ore_colour = (47,25,15)

class MiningBot():
    def __init__(self):
        pass

    def mine_stuff(self):
        for img in rock_images:
            surroundings_img = pag.screenshot('surroundings.png', region=(0,0,1920,1200)) # adjust region so that it covers only the rs env
            if pag.locate(img, surroundings_img, confidence = 0.85) != None: # if we can find the rock with ore in it
                self.clickonrock(img)
                while True:
                    if self.check_ore_exists(img) == False: # if the ore has been mined either by me or someone else
                        break
            else:
                continue

    # returns true if the inventory is full
    def check_full_inv(self):
        if self.get_pixel_colours(1830, 1103) == ore_colour: 
           return True
        return False

        #chatbox_img = pag.screenshot('chatbox.png', region=(1,1000,512,126)) 
        #if pag.locate('full_inv_message.jpg', chatbox_img, confidence = 0.8) != None:
       #     return True
       # return False


    # returns random x y coordinates within a box
    def get_random_coordinates(self, x_lower, y_lower, x_upper, y_upper):
        x = randint(x_lower, x_upper)
        y = randint(y_lower, y_upper)
        return x, y

    # returns true if the specified ore is in the rock
    def check_ore_exists(self, ore_name):      # ore_name should be a string of form 'on' where n is an integer 1-4
        x,y = rock_pixel_coordinates[ore_name]
        if self.get_pixel_colours(x, y) == rock_pixel_colour[ore_name]:
            return True
        return False 

    # returns the rgb colours of a specified pixel
    def get_pixel_colours(self, x, y):
        pag.moveTo(x, y)
        return pag.pixel(x,y)

    # teleports the mouse to a random coordinate within a specified ore's box and clicks on it
    def clickonrock(self, ore_image_name):
        orename = ore_image_name.strip('.jpg')
        x_lower, y_lower, x_upper, y_upper = rock_coordinates[orename]
        print(rock_coordinates[orename])
        x, y = self.get_random_coordinates(x_lower, y_lower, x_upper, y_upper)
        print(x,y)
        pag.click(x,y)
        '''
        #TODO       
        move mouse to x,y in human fashion
        click on xy
        '''


'''
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pag.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
'''

'''
    def rock_empty(self, img):
        haystack = pag.screenshot('haystack.png', region=(0,0,1920,1200))
        empty_ore_img = empty_rock_images[img]
        res = pag.locate(empty_ore_img, haystack, confidence = 0.8)
        if res == None:
            print('couldnt find empty rock')
            return False
        print('found empty rock')
        return True
'''

'''
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pag.position()
        r,g,b = pag.pixel(x,y)
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pxlclr = 'R: ' + str(r) + 'G: ' + str(g) + 'B: ' + str(b)
        print(positionStr, end='')
        print(pxlclr, end = '')
        print('\b' * (len(positionStr)+len(pxlclr)), end='', flush=True)
except KeyboardInterrupt:
    print('\n')


def get_pixel_colours(x, y):
    pag.moveTo(x, y)
    pos_str = 'X: ' + str(x) + ' Y: ' + str(y)
    r,g,b = pag.pixel(x,y)
    pxlclr = 'R: ' + str(r) + ' G: ' + str(g) + ' B: ' + str(b)
    print(pos_str)
    print(pxlclr)
'''