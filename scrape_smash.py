from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

# Function for scraping moveset data for one Smash character
def scrape_me_your_moves(url):

    PATH = '/Users/jameslee/Desktop/Data_Science/chromedriver'
    driver = webdriver.Chrome(PATH)
    driver.get(url)
    def character_name(url):
        return url.split('/')[3].strip('.php').capitalize()


    time.sleep(1)
    # this line makes sure that the page is properly loaded first before we start crawling the webpage
    
    moves = driver.find_elements_by_class_name('movecontainer')

    def check_exists(class_name):
        try:
            move.find_element_by_class_name(class_name)
        except NoSuchElementException:
            return False
        return True
    move_list = []
    for move in moves:      
        if check_exists('movename')== False:
            movename = 'NA'
        else:
            movename = move.find_element_by_class_name('movename').text # move name
        if check_exists('basedamage') == False:
            basedamage = "NA"
        else:
            basedamage = move.find_element_by_class_name('basedamage').text # base damage
        
        if check_exists('startup')== False:
            startup = 'NA'
        else:
            startup = move.find_element_by_class_name('startup').text # startup frames
        if check_exists('advantage')== False:
            advantage = 'NA'
        else:    
            advantage = move.find_element_by_class_name('advantage').text # on shield
        if check_exists('activeframes')== False:
            active_frames = 'NA'
        else:
            active_frames = move.find_element_by_class_name('activeframes').text # active on -
        if check_exists('startup')== False:
            total_frames = 'NA'
        else:
            total_frames = move.find_element_by_class_name('totalframes').text # total frames
        if check_exists('landinglag')== False:
            landing_lag = 'NA'
        else:
            landing_lag = move.find_element_by_class_name('landinglag').text # landing lag
        if check_exists('shieldlag')== False:
            shield_lag = 'NA'
        else:
            shield_lag = move.find_element_by_class_name('shieldlag').text # shield lag
        if check_exists('shieldstun')== False:
            shield_stun = 'NA'
        else:
            shield_stun = move.find_element_by_class_name('shieldstun').text # shield stun
        if check_exists('notes')== False:    
            notes = 'NA'
        else:
            notes = move.find_element_by_class_name('notes').text # additional notes for the specific move
        metric_list = {
            'character_name': character_name(url),
            'movename': movename,
            'basedamage': basedamage,
            'startup': startup,
            'advantage': advantage,
            'active_frames': active_frames,
            'total_frames': total_frames,
            'landing_lag':landing_lag,
            'shield_lag':shield_lag,
            'shield_stun':shield_stun,
            'notes':notes
        }

        move_list.append(metric_list)

    data = pd.DataFrame(move_list)
    

    driver.quit()

    return data


