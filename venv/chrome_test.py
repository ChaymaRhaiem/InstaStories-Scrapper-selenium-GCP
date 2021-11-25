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
import json


import re
from urllib.request import urlopen

import glob
from google.cloud import storage
from google.oauth2 import service_account

from google.cloud import vision

import pandas as pd
from selenium.webdriver.chrome.options import Options
import argparse

"""try:
    my_username = sys.argv[1]
    my_password = sys.argv[2]
    mode = sys.argv[3]
    target_username = sys.argv[4]
    dest_bucket=sys.argv[5]
    chrome_test.login(my_username,my_password,target_username,dest_bucket)
except:
    print("")
"""
options = Options()
options.headless = True

#sys.argv['mode'], default="both"


service = Service("C:\Instagram_stories_scrapper\chrome web driver\chromedriver_win32/chromedriver.exe")
drive = webdriver.Chrome(service=service, options=options)


#single target_user stories scrapping
#add midnight time for scrapping
target_username = "//"

my_username = "//"
my_password = "//"

images = []
videos = []
list=[]

with open('file.json') as source:
    info = json.load(source)

storage_credentials = service_account.Credentials.from_service_account_info(info)
project_id = 'project-101-321021'
client = storage.Client(project=project_id, credentials=storage_credentials)

# Explicitly use service account credentials by specifying the private key
# Retrieve an existing bucket
dest_bucket = client.get_bucket('insta_stories0')
directory_path = "dir"
gcs_path = "//"

def img_path(dest_bucket,list):
    blobs = client.list_blobs(dest_bucket)

    for blob in blobs:
        path = blob.name.split('/',3)
        list.append(path[3])
    print(list)


def detect_logos_uri(uri):
    with open('file.json') as source:
        info = json.load(source)

    storage_credentials = service_account.Credentials.from_service_account_info(info)
    """Detects logos in the file located in Google Cloud Storage or on the Web.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient(credentials=storage_credentials)
    image = vision.Image()
    image.source.image_uri = uri

    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    print('Logos:')

    for logo in logos:
        print(logo.description)
    """if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
"""

def list_blobs(dest_bucket):

    blobs = client.list_blobs(dest_bucket)

    for blob in blobs:
        print(blob.name)


def upload_directory_to_gcs(directory_path, dest_bucket, gcs_path):
    for local_file in directory_path:
       rel_paths = glob.glob(directory_path + '/**', recursive=True)
       for local_file in rel_paths:
           remote_path = f'{gcs_path}/{"/".join(local_file.split(os.sep)[1:])}'
           if os.path.isfile(local_file):
               blob = dest_bucket.blob(remote_path)
               blob.upload_from_filename(local_file)
    return



















def scrapeStories(traget_username):
    images = []
    print("Scraping stories from " + '"' + target_username + '".' )
    getStories(target_username ,images)
    save_to_computer(images,target_username)

    print("Downloaded " + str(len(images)) + " images from " + '"' + target_username + '".')




def getStories(target_username,images):
    print('test3')
    story_page = "https://www.instagram.com/stories" + "/" + target_username + "/"
    drive.get(story_page)

    print('starting story viewing')
    sleep(1)
    #react-root > section > div.qF0y9.Igw0E.rBNOH.YBx95.vwCYk > div > section > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.NUiEW > div > div > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.dQ9Hi > button#
    drive.find_element_by_css_selector("#react-root > section > div.qF0y9.Igw0E.rBNOH.YBx95.vwCYk > div > section > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.NUiEW > div > div > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.dQ9Hi > button").click()
    print('story viewing')
    sleep(1)
    while drive.current_url == story_page:

        Resources = drive.execute_script("return window.performance.getEntriesByType('resource');")
        sleep(2.5)
    # click loads all resources
        print(Resources)
        for resource in Resources:
            if 'jpg' in resource['name'] :
                if 'jpg' in resource['name'] and resource['decodedBodySize'] > 9900:
                    if resource['name'] not in images:
                        images.append(resource['name'])
                        print('story found')
                        print(images)
            if 'mp4' in resource['name'] and resource['initiatorType'] != 'imageset':
                if resource['name'] not in images:
                    videos.append(resource['name'])
        sleep(1)
        drive.find_element_by_css_selector("#react-root > section > div.qF0y9.Igw0E.rBNOH.YBx95.vwCYk > div > section > div > button.FhutL").click()
        sleep(1)

        print(images)
        print(str(len(images)) + "images found.")














def login(my_username,my_password,target_username,dest_bucket):
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
     scrapeStories(target_username)



img_path(dest_bucket,list)

def detect_blobs(dest_bucket,list):
     blobs = client.list_blobs(dest_bucket)
     for i in range(len(list)):
             uri = "gs://uri" + target_username +"/"+ list[i]
             sleep(1)
             detect_logos_uri(uri)

def endMe():
    drive.close()

def save_to_computer(images,target_username):
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y")
    folder_location = 'dir'
    newpath = folder_location + "/" + target_username
    print(newpath)
    if not os.path.exists(newpath):
            os.makedirs(newpath)
            # Download files into folder
    print(images)
    try:
        for i in range(len(images)):
            print('aaaa')
            f_name = images[i].split('/')[-1].split('?', 1)[0]
            f_path_file =  newpath + "/" + dt_string +  "_" + f_name
            #img_data = requests.get(images[i]).content
            #print(img_data)



            with requests.get(images[i], stream=True) as r:
                  with open( f_path_file, "wb") as f:
                                for chunk in r.iter_content(chunk_size=8192):
                                    if chunk:
                                        f.write(chunk)
                                        f.flush()
    except Exception as e:
        print(e)
    endMe()


#if mode != "download":
def download(mode="download"):
    login(my_username,my_password,target_username,dest_bucket)
    upload_directory_to_gcs(directory_path, dest_bucket, gcs_path)

def computer_vision(mode="detect"):
    detect_blobs(dest_bucket,list)

def scrapeInsta(mode="default"):
    login(my_username, my_password, target_username, dest_bucket)
    upload_directory_to_gcs(directory_path, dest_bucket, gcs_path)
    detect_blobs(dest_bucket,list)


####TO DO  dossier dataframe bucket directories named with day  .csv - backend selenium   no time stamp  -
#DASH - >  HTML website

