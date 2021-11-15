from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from io import BytesIO
from datetime import datetime
import subprocess
import requests
import urllib.request

from pathlib import Path
from os.path import basename
import shutil
import sys, os

import urlparse3




service = Service("C:\Instagram_stories_scrapper\chrome web driver\chromedriver_win32/chromedriver.exe")
drive = webdriver.Chrome(service=service)


#single target_user stories scrapping
#add scrapping schedule
target_username = "//"

my_username = "//"
my_password = "//"




def scrapeStories(traget_username):

    print("Scraping stories from " + '"' + target_username + '".' )
    images= []
    getStories(target_username ,images)
    print('stories gotten')
    save_to_computer(images,target_username)

    print("Downloaded " + str(len(images)) + " images from " + '"' + target_username + '".')




def getStories(target_username,images):
    print('test3')
    story_page = "https://www.instagram.com/stories" + "/" + target_username + "/"
    drive.get(story_page)

    print('starting story viewing')
    sleep(1)
    drive.find_element_by_css_selector('#react-root > section > div.qF0y9.Igw0E.rBNOH.YBx95.vwCYk > div > section > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.NUiEW > div > div > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.dQ9Hi > button').click()
    print('story viewing')
    sleep(1)
    while drive.current_url == story_page:

        Resources = drive.execute_script("return window.performance.getEntriesByType('resource');")
        sleep(5)
    # click loads all resources
        for resource in Resources:
            if 'jpg' in resource['name'] :
                   if resource['name'] not in images and resource['decodedBodySize'] > 9000 :
                      print('story found')
                      images.append(resource['name'])
                      print(resource['name'])
                      sleep(1)
        drive.find_element_by_css_selector("#react-root > section > div.qF0y9.Igw0E.rBNOH.YBx95.vwCYk > div > section > div > button.FhutL").click()
        print("looploop")
        sleep(1)
        print(images)
    # upload_to_bucket(images,target_username) #split('_')

    #drive.find_element_by_xpath("/html/body/span/section/div/div/section/div[2]/button[2]/div").click()













def login(my_username,my_password,target_username):
     drive.get("https://www.instagram.com/accounts/login/")
     sleep(3)
     username = drive.find_element_by_name('username')
     username.send_keys(my_username)
     password = drive.find_element_by_name('password')
     password.send_keys(my_password)
     button_login = drive.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button')
     button_login.click()
     sleep(5)
     print('test1')
     not_now = drive.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
     not_now.click()
     print('test2')
     sleep(1)
     notificationnotnow = drive.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
     notificationnotnow.click()

     sleep(1)
   #TO DO: ADD LOOP FOR USER ACCOUNTS AND ROUTINE
     scrapeStories(target_username)

def create_file_path(target_username):
    year = datetime.datetime.now().strftime("%y")
    month = datetime.datetime.now().strftime("%M")
    day = datetime.datetime.now().strftime("%d")
    file_path = f"/target_username/{year}/{month}"
    return file_path





def save_to_computer(images,target_username):
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y")


    folder_location = 'C:/Users/Lenovo/Pictures'
    newpath = folder_location + "\\" + target_username

    sleep(3)


    if not os.path.exists(newpath):
        os.makedirs(newpath)
        # Download files into folder
    try:
        for i in range(len(images)):

            filename = os.path.basename(urlparse(images[i]).path)
            filename_jpg = os.path.splitext(filename)[0] + '.jpg'

            #f_name = images[0].split('/')[-1].split('?', 1)[0]
            #f_path_file = "./" + target_username + "/" + f_name
            my_file = Path(filename_jpg)
            if my_file.is_file():
                print("File exsists...")
                continue
            else:
                # print(f_name)
                with requests.get(images[i], stream=True) as r:
                    r.raise_for_status()
                    with open(f_path_file, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
    except Exception as e:
        print(e)






    #f_path = target_username + "_" + dt_string + "_" + "story" + file_name

def endme():
    driver.close()




login(my_username,my_password,target_username)



####TO DO  dossier dataframe bucket directories named with day  .csv - backend selenium   no time stamp  -
