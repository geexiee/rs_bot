from random import randint
import pyautogui as pag
import sys
import cv2
import Main as m

mb = m.MiningBot()
rock_coordinates = {'o1':(858, 543, 895, 567), 'o2':(859, 484, 897, 515), 'o3':(914, 481, 948, 517), 'o4':(1024,4347,1058,4537)}
rock_pixel_colour = {'o1':(57,30,20), 'o2':(54,27,19), 'o3':(54,27,19), 'o4':(57,30,20)}
rock_pixel_coordinates = {'o1':(899,581), 'o2':(905,540), 'o3':(945,531), 'o4':(1055,476)}
rock_images = ['o1.jpg', 'o2.jpg', 'o3.jpg']
empty_rock_images = ['e1.jpg', 'e2.jpg', 'e3.jpg']
ore_coordinate = (1830, 1103)
ore_colour = (47,25,15)

newss = pag.screenshot(region=(0,0,1920,1200))

def test_find_o1():
    assert mb.check_ore_exists('o1') == True

def test_find_o2():
    assert mb.check_ore_exists('o2') == True

def test_find_o3():
    assert mb.check_ore_exists('o3') == True

def test_find_o4():
    assert mb.check_ore_exists('o4') == True

def test_full_inv():
    assert mb.check_full_inv() == True
