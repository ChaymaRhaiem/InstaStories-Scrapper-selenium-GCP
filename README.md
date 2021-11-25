# InstaStories-Scrapper---selenium-


<h1 align="center">Instagram Stories Scraper </h1>
<p align="center">
      <img src="https://img.shields.io/badge/built%20with-Selenium-yellow.svg" />
    </a>
    	<img src="https://img.shields.io/badge/built%20with-Python3-red.svg" />
    </a>
  </p>
<p>
  <p>A tool that <b>scrapes</b> Instagram stories implemented in Python 3 using the Selenium module.<p>
  <p> Uploads captured stories to GCP </p>
  <p> Uses Cloud Vision API to detect the logos in each image </p>
</p>



## Quick Start 🚀

- **You need to have Python 3.6 or above installed**

  - `python3 --version`

On Windows you might have to use `python` without the version (`3`) suffix.



- **Install REQUIREMENTS**

  - `python3 -m pip install -r requirements.txt`


# Selenium_python  :heavy_check_mark:

## What is Selenium ? 
#### Selenium is an open-source testing tool, which means it can be downloaded from the internet without spending anything. Selenium is a functional testing tool and also compatible with non-functional testing tools as well.
<br>

## Selenium WebDriver
Selenium WebDriver is a web framework that permits you to execute cross-browser tests. This tool is used for automating web-based application testing to verify that it performs expectedly.
Selenium WebDriver allows you to choose a programming language of your choice to create test scripts. As discussed earlier, it is an advancement over Selenium RC to overcome a few limitations. Selenium WebDriver is not capable of handling window components, but this drawback can be overcome by using tools like Sikuli, Auto IT, etc. <br>
[Getting Started with Selenium WebDriver for Automation Testing](https://www.browserstack.com/guide/selenium-webdriver-tutorial)


## Links :link:
* [Selenium](https://www.selenium.dev/)
* [Selenium Python](https://pypi.org/project/selenium/) :snake:
* [Docs](https://www.selenium.dev/selenium/docs/api/py/api.html)
* [Selenium Github](https://github.com/SeleniumHQ/Selenium)
<br>

## Downloads
* [ChromeDriver - WebDriver](https://chromedriver.chromium.org/)
* [Python](https://www.python.org/downloads/)
* [PyCharm](https://www.jetbrains.com/pycharm/download/)
<br>

## Getting Started with Selenium
```
pip install selenium
```
```
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"<LOCATION OF CHROMEDRIVER >")
```

Python Client for Google Cloud Vision
=====================================

|GA| |pypi| |versions| 

The `Google Cloud Vision`_  API enables developers to
understand the content of an image by encapsulating powerful machine
learning models in an easy to use REST API. It quickly classifies images
into thousands of categories (e.g., "sailboat", "lion", "Eiffel Tower"),
detects individual objects and faces within images, and finds and reads
printed words contained within images. You can build metadata on your
image catalog, moderate offensive content, or enable new marketing
scenarios through image sentiment analysis. Analyze images uploaded
in the request or integrate with your image storage on Google Cloud
Storage.

- `Client Library Documentation`_
- `Product Documentation`_

.. |GA| image:: https://img.shields.io/badge/support-GA-gold.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#general-availability
.. |pypi| image:: https://img.shields.io/pypi/v/google-cloud-vision.svg
   :target: https://pypi.org/project/google-cloud-vision/
.. |versions| image:: https://img.shields.io/pypi/pyversions/google-cloud-vision.svg
   :target: https://pypi.org/project/google-cloud-vision/
.. _Vision: https://cloud.google.com/vision/

.. _Google Cloud Vision: https://cloud.google.com/vision/
.. _Client Library Documentation: https://cloud.google.com/python/docs/reference/vision/latest
.. _Product Documentation: https://cloud.google.com/vision/reference/rest/


Quick Start
-----------

In order to use this library, you first need to go through the following steps:

1. `Select or create a Cloud Platform project.`_
2. `Enable billing for your project.`_
3. `Enable the Google Cloud Vision API.`_
4. `Setup Authentication.`_

.. _Select or create a Cloud Platform project.: https://console.cloud.google.com/project
.. _Enable billing for your project.: https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project
.. _Enable the Google Cloud Vision API.:  https://cloud.google.com/vision
.. _Setup Authentication.: https://googleapis.dev/python/google-api-core/latest/auth.html




Example Usage
~~~~~~~~~~~~~

.. code-block:: python

   from google.cloud import vision

   client = vision.ImageAnnotatorClient()
   response = client.annotate_image({
     'image': {'source': {'image_uri': 'gs://my-test-bucket/image.jpg'}},
     'features': [{'type_': vision.Feature.Type.FACE_DETECTION}]
   })

Known Limitations
~~~~~~~~~~~~~~~~~



  [TYPECHECK]
  
  generated-members=<<REGULAR EXPRESSION>>

Substitute a regular expression of your choosing that matches all lines for which you want to
disable this error check. For example, if you choose a convention of naming your
``ImageAnnotatorClient`` variables ``image_annotator_client``, then your regex could be
``image_annotator_client.*`` or something similar.

      
##Common Errors:
Certain images were not downloaded (currently working on it)
 

