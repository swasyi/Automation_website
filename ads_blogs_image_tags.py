import tkinter as tk
from tkinter import ttk, messagebox
import os
import re
import concurrent.futures
import threading
import pyperclip
import requests
import pyautogui
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.options import ArgOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import ast
from selenium.webdriver.support.ui import Select
import traceback


def get_driver():
    brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    chrome_options = Options()
    chrome_options.binary_location = brave_path
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# def load_page_and_zoom(driver, url, zoom='40%'):
#     driver.get(url)
#     driver.execute_script(f"document.body.style.zoom='{zoom}'")
#


def getadsonline(Title,Description,Target_url):
    driver = get_driver()
    driver.get("https://getadsonline.com/index.php?view=post&cityid=536&lang=en&catid=3&subcatid=18&shortcutregion=0")
    time.sleep(5)

    titlebox=driver.find_element(By.ID,'adtitle')
    titlebox.send_keys(Title)

    time.sleep(3)

    location = driver.find_element(By.NAME, 'area')
    location.send_keys("Rani Bagh, Delhi")
    time.sleep(3)

    desc_box=driver.find_element(By.ID,'wmd-input')
    desc_box.send_keys(Description+"  "+Target_url)
    time.sleep(3)

    email_box=driver.find_element(By.ID,'email')
    email_box.send_keys("koushal.obluhc@gmail.com")
    time.sleep(3)

    radio_buttons = driver.find_elements(By.NAME, "showemail")
    radio_buttons[2].click()
    time.sleep(2)

    # Scroll up by 200 pixels
    driver.execute_script("window.scrollBy(0, 300);")

    # Find the checkbox using its name attribute
    checkbox1 = driver.find_element(By.NAME, 'othercontactok')

    checkbox1.click()
    time.sleep(3)

    # Find the checkbox using its name attribute
    checkbox2 = driver.find_element(By.NAME, 'agree')
    checkbox2.click()
    time.sleep(3)

    driver.execute_script("window.scrollBy(0, 300);")


    post_now_button = driver.find_element(By.XPATH, '//button[text()="Post Now"]')
    post_now_button.click()

    input("END?")

def postthreads(Title,Description,Target_url):
    driver = get_driver()
    driver.get("https://posthereads.com/index.php?view=post&cityid=536&lang=en&catid=3&subcatid=18&shortcutregion=0")
    time.sleep(5)

    titlebox=driver.find_element(By.ID,'adtitle')
    titlebox.send_keys(Title)

    time.sleep(3)

    location = driver.find_element(By.NAME, 'area')
    location.send_keys("Rani Bagh, Delhi")
    time.sleep(3)

    desc_box=driver.find_element(By.ID,'wmd-input')
    desc_box.send_keys(Description+"  "+Target_url)
    time.sleep(3)

    email_box=driver.find_element(By.ID,'email')
    email_box.send_keys("koushal.obluhc@gmail.com")
    time.sleep(3)

    radio_buttons = driver.find_elements(By.NAME, "showemail")
    radio_buttons[2].click()
    time.sleep(2)

    # Scroll up by 200 pixels
    driver.execute_script("window.scrollBy(0, 300);")

    # Find the checkbox using its name attribute
    checkbox1 = driver.find_element(By.NAME, 'othercontactok')
    checkbox1.click()
    time.sleep(3)

    # Find the checkbox using its name attribute
    checkbox2 = driver.find_element(By.NAME, 'agree')
    checkbox2.click()
    time.sleep(3)

    # Scroll up by 200 pixels
    driver.execute_script("window.scrollBy(0, 300);")

    post_now_button = driver.find_element(By.XPATH, '//button[text()="Post Now"]')
    post_now_button.click()

    input("END?")

def postherefree(Title,Description,Target_url):
    driver = get_driver()
    driver.get("https://postherefree.com/index.php?view=post&cityid=536&lang=en&catid=3&subcatid=18&shortcutregion=0")
    time.sleep(5)

    titlebox=driver.find_element(By.ID,'adtitle')
    titlebox.send_keys(Title)

    time.sleep(3)

    location = driver.find_element(By.NAME, 'area')
    location.send_keys("Rani Bagh, Delhi")
    time.sleep(3)

    desc_box=driver.find_element(By.ID,'wmd-input')
    desc_box.send_keys(Description+"  "+Target_url)
    time.sleep(3)

    email_box=driver.find_element(By.ID,'email')
    email_box.send_keys("koushal.obluhc@gmail.com")
    time.sleep(6)

    radio_buttons = driver.find_elements(By.NAME, "showemail")
    radio_buttons[2].click()
    time.sleep(2)

    # Scroll up by 200 pixels
    driver.execute_script("window.scrollBy(0, 300);")

    # Find the checkbox using its name attribute
    checkbox1 = driver.find_element(By.NAME, 'othercontactok')
    checkbox1.click()
    time.sleep(3)
    # Find the checkbox using its name attribute
    checkbox2 = driver.find_element(By.NAME, 'agree')
    checkbox2.click()
    time.sleep(3)

    # Scroll up by 200 pixels
    driver.execute_script("window.scrollBy(0, 300);")
    post_now_button = driver.find_element(By.XPATH, '//button[text()="Post Now"]')
    post_now_button.click()

    input("END?")

def ursads(Title,Description,Target_url):
    driver = get_driver()
    driver.get("https://ursads.com/index.php?view=post&cityid=536&lang=en&catid=3&subcatid=18&shortcutregion=0")
    time.sleep(5)

    titlebox=driver.find_element(By.ID,'adtitle')
    titlebox.send_keys(Title)

    time.sleep(3)

    location = driver.find_element(By.NAME, 'area')
    location.send_keys("Rani Bagh, Delhi")
    time.sleep(3)

    desc_box=driver.find_element(By.ID,'wmd-input')
    desc_box.send_keys(Description+"  "+Target_url)
    time.sleep(3)

    email_box=driver.find_element(By.ID,'email')
    email_box.send_keys("koushal.obluhc@gmail.com")
    time.sleep(3)

    radio_buttons = driver.find_elements(By.NAME, "showemail")
    radio_buttons[2].click()
    time.sleep(2)

    # Scroll up by 200 pixels
    driver.execute_script("window.scrollBy(0, 300);")
    # Find the checkbox using its name attribute
    checkbox1 = driver.find_element(By.NAME, 'othercontactok')
    checkbox1.click()
    time.sleep(3)

    # Find the checkbox using its name attribute
    checkbox2 = driver.find_element(By.NAME, 'agree')
    checkbox2.click()
    time.sleep(3)

    # Scroll up by 200 pixels
    driver.execute_script("window.scrollBy(0, 300);")
    post_now_button = driver.find_element(By.XPATH, '//button[text()="Post Now"]')
    post_now_button.click()

    input("END?")

def adshoo(Title,Description,Target_url):
    driver = get_driver()
    driver.get("https://www.adshoo.com/index.php?view=post&cityid=75&lang=en&catid=3&subcatid=18&shortcutregion=0")
    time.sleep(5)

    titlebox=driver.find_element(By.ID,'adtitle')
    titlebox.send_keys(Title)

    time.sleep(3)

    location = driver.find_element(By.NAME, 'area')
    location.send_keys("Rani Bagh, Delhi")
    time.sleep(3)

    desc_box=driver.find_element(By.ID,'wmd-input')
    desc_box.send_keys(Description+"  "+Target_url)
    time.sleep(3)

    email_box=driver.find_element(By.ID,'email')
    email_box.send_keys("koushal.obluhc@gmail.com")
    time.sleep(3)

    radio_buttons = driver.find_elements(By.NAME, "showemail")
    radio_buttons[2].click()
    time.sleep(2)

    # Scroll up by 200 pixels
    driver.execute_script("window.scrollBy(0, 300);")
    # Find the checkbox using its name attribute
    checkbox1 = driver.find_element(By.NAME, 'othercontactok')
    checkbox1.click()
    time.sleep(3)

    # Find the checkbox using its name attribute
    checkbox2 = driver.find_element(By.NAME, 'agree')
    checkbox2.click()
    time.sleep(3)

    # Scroll up by 200 pixels
    driver.execute_script("window.scrollBy(0, 300);")
    post_now_button = driver.find_element(By.XPATH, '//button[text()="Post Now"]')
    post_now_button.click()

    input("END?")

def letspostfree(Title,Description,Target_url):
    driver = get_driver()
    driver.get("https://letspostfree.com/index.php?view=post&cityid=536&lang=en&catid=3&subcatid=18&shortcutregion=0")
    time.sleep(5)

    titlebox=driver.find_element(By.ID,'adtitle')
    titlebox.send_keys(Title)

    time.sleep(3)

    location = driver.find_element(By.NAME, 'area')
    location.send_keys("Rani Bagh, Delhi")
    time.sleep(3)

    desc_box=driver.find_element(By.ID,'wmd-input')
    desc_box.send_keys(Description+"  "+Target_url)
    time.sleep(3)

    email_box=driver.find_element(By.ID,'email')
    email_box.send_keys("koushal.obluhc@gmail.com")
    time.sleep(3)

    radio_buttons = driver.find_elements(By.NAME, "showemail")
    radio_buttons[2].click()
    time.sleep(2)

    # Scroll up by 200 pixels
    driver.execute_script("window.scrollBy(0, 300);")
    # Find the checkbox using its name attribute
    checkbox1 = driver.find_element(By.NAME, 'othercontactok')
    checkbox1.click()
    time.sleep(3)

    # Find the checkbox using its name attribute
    checkbox2 = driver.find_element(By.NAME, 'agree')
    checkbox2.click()
    time.sleep(3)

    # Scroll up by 200 pixels
    driver.execute_script("window.scrollBy(0, 300);")
    post_now_button = driver.find_element(By.XPATH, '//button[text()="Post Now"]')
    post_now_button.click()

    input("END?")

def yookalo(Title,Description,Keyword,target_url):
    driver = get_driver()
    driver.get("https://posts.yookalo.com/list-an-ad-steps.php")
    # Optional: Wait for the page to load fully
    time.sleep(5)

    # Wait for the radio buttons to be present
    wait = WebDriverWait(driver, 10)
    radio_buttons = wait.until(EC.presence_of_all_elements_located((By.NAME, "typenow")))

    # Click the "Business" radio button (2nd one)
    radio_buttons[1].click()

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "Post a Classified Ad"
    classified_ad_link = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Post a Classified Ad")
    ))
    classified_ad_link.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "India"
    india_button = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "India")
    ))
    india_button.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "Email"
    by_email = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "By Email")
    ))
    by_email.click()

    time.sleep(3)

    health_label = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="56"]')))

    # Click on the label (which will check the radio button)
    health_label.click()

    time.sleep(5)
    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()


    time.sleep(3)

    # Wait for the input to be visible and interactable
    title_input = wait.until(EC.visibility_of_element_located((By.ID, "titleen_US")))

    # Send text to the input
    title_input.send_keys(Title)

    time.sleep(3)

    # Wait for the textarea to be visible
    description_area = wait.until(EC.visibility_of_element_located((By.ID, "descriptionen_US")))

    # Send text to the textarea
    description_area.send_keys(Description)

    time.sleep(3)

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    address_area = wait.until(EC.visibility_of_element_located((By.ID, "address")))
    address_area.send_keys("Rani Bagh Delhi")

    time.sleep(3)

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    # Wait for and click the "INR" currency radio button
    inr_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='inr']")))
    inr_label.click()

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    Name_area = wait.until(EC.visibility_of_element_located((By.ID, "contactName")))
    Name_area.send_keys("OBLU")

    email_area = wait.until(EC.visibility_of_element_located((By.ID, "contactEmail")))
    email_area.send_keys("koushal.obluhc@gmail.com")

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    company_name_area = wait.until(EC.visibility_of_element_located((By.ID, "bizorcompanyname")))
    company_name_area.send_keys("OBLU")

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    # Wait until the dropdown is present
    country_dropdown = wait.until(EC.presence_of_element_located((By.ID, "countryId")))

    # Wrap it in Select and choose India by value
    select = Select(country_dropdown)
    select.select_by_value("IN")

    time.sleep(3)

    region_dropdown= wait.until(EC.presence_of_element_located((By.ID, "regionId")))

    select=Select(region_dropdown)
    select.select_by_value('781499')

    time.sleep(3)

    city_dropdown=wait.until(EC.presence_of_element_located((By.ID, "cityId")))

    select=Select(city_dropdown)
    select.select_by_value('276454')


    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    phone_field=driver.find_element(By.ID, "meta_new-custom-field")
    phone_field.send_keys("9650447099")

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    website_url=driver.find_element(By.ID, "q1")
    website_url.send_keys(target_url)


    continue_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_link.click()

    time.sleep(3)

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)


    # Wait for and click the "Continue" button
    submit_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Submit")))
    submit_button.click()
    time.sleep(6)

    print("https://www.yookalo.com/item-success")

    input("ENd?")

def findmaster(Title,Description,keyword,target_url):
    driver = get_driver()
    driver.get("https://listings.findermaster.com/post-a-free-ad-process-type.php")

    time.sleep(5)

    # Wait for the radio buttons to be present
    wait = WebDriverWait(driver, 10)
    radio_buttons = wait.until(EC.presence_of_all_elements_located((By.NAME, "typenow")))

    # Click the "Business" radio button (2nd one)
    radio_buttons[1].click()

    time.sleep(2)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()

    # Step 3: On the next page, wait for and click "Post a Classified Ad"
    classified_ad_link = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Post a Classified Ad")
    ))
    classified_ad_link.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "India"
    india_button = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "India")
    ))
    india_button.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "Email"
    by_email = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "By Email")
    ))
    by_email.click()

    time.sleep(3)

    wait = WebDriverWait(driver, 10)
    health_label = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="56"]')))

    # Click on the label (which will check the radio button)
    health_label.click()

    time.sleep(3)
    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))

    # Click the button
    continue_button.click()

    time.sleep(5)

    # Wait for the input to be visible and interactable
    title_input = wait.until(EC.visibility_of_element_located((By.ID, "titleen_US")))

    # Send text to the input
    title_input.send_keys(Title)

    time.sleep(3)

    # Wait for the textarea to be visible
    description_area = wait.until(EC.visibility_of_element_located((By.ID, "descriptionen_US")))

    # Send text to the textarea
    description_area.send_keys(Description)

    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    address_area = wait.until(EC.visibility_of_element_located((By.ID, "address")))
    address_area.send_keys("Rani Bagh, Delhi")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    # Wait for the radio button with ID "INR" to be clickable
    wait = WebDriverWait(driver, 10)
    inr_radio_button = wait.until(EC.element_to_be_clickable((By.ID, "INR")))

    # Click the radio button
    inr_radio_button.click()

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    name_field=driver.find_element(By.ID,'contactName')
    name_field.send_keys("Oblu")
    time.sleep(3)

    email_field=driver.find_element(By.ID,'contactEmail')
    email_field.send_keys("koushal.obluhc@gmail.com")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    company_business_name=driver.find_element(By.ID,'companyorbusinessname')
    company_business_name.send_keys("OBLU")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)


    # Wait until the dropdown is present
    country_dropdown = wait.until(EC.presence_of_element_located((By.ID, "countryId")))

    # Wrap it in Select and choose India by value
    select = Select(country_dropdown)
    select.select_by_value("IN")

    time.sleep(3)

    region_dropdown= wait.until(EC.presence_of_element_located((By.ID, "regionId")))

    select=Select(region_dropdown)
    select.select_by_value('781499')

    time.sleep(3)

    city_dropdown=wait.until(EC.presence_of_element_located((By.ID, "cityId")))

    select=Select(city_dropdown)
    select.select_by_value('276454')
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    phone_number_field=driver.find_element(By.ID,'meta_new-custom-field')
    phone_number_field.send_keys("9650447099")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)


    webseite_url_field=driver.find_element(By.ID,'q1')
    webseite_url_field.send_keys(target_url)
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(3)

    # Wait for the "None" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    none_radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="None"]')))

    # Click the "None" radio button
    none_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    # Wait for the "None" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    daytime_radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="Daytime"]')))

    # Click the "None" radio button
    daytime_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for the "business_day" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    business_day_radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="1–2 business days"]')))


    business_day_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    wait = WebDriverWait(driver, 10)
    yes_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="Yes"]')))

    yes_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    keyword_field=driver.find_element(By.ID,'w1')
    keyword_field.send_keys(keyword)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    submit_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Submit")))
    submit_button.click()
    time.sleep(6)

    print("https://www.findermaster.com/item-success")


    input("END?")

def h1ad(Title,Description,Keyword):
    driver = get_driver()
    driver.get("https://postjourney.h1ad.com/post-a-classified-ad-process.php")

    time.sleep(5)

    # Wait for the radio buttons to be present
    wait = WebDriverWait(driver, 10)
    radio_buttons = wait.until(EC.presence_of_all_elements_located((By.NAME, "typenow")))

    # Click the "Business" radio button (2nd one)
    radio_buttons[1].click()

    time.sleep(2)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()

    # Step 3: On the next page, wait for and click "Post a Classified Ad"
    classified_ad_link = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Post a Classified Ad")
    ))
    classified_ad_link.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "India"
    india_button = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "India")
    ))
    india_button.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "Email"
    by_email = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "By Email")
    ))
    by_email.click()

    time.sleep(3)


    try:
        radio_button = wait.until(EC.element_to_be_clickable((By.ID, 'catId_5')))
        radio_button.click()
    except:
        # Fallback: use JS click
        radio_button = driver.find_element(By.ID, 'catId_5')
        driver.execute_script("arguments[0].click();", radio_button)


    time.sleep(3)
    continue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Continue"]')))
    continue_button.click()
    time.sleep(6)


    # Wait for the input to be visible and interactable
    title_input = wait.until(EC.visibility_of_element_located((By.ID, "titleen_US")))

    # Send text to the input
    title_input.send_keys(Title)

    time.sleep(3)

    # Wait for the textarea to be visible
    description_area = wait.until(EC.visibility_of_element_located((By.ID, "descriptionen_US")))

    # Send text to the textarea
    description_area.send_keys(Description)

    time.sleep(3)

    continue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Continue"]')))
    continue_button.click()
    time.sleep(6)

    address_area = wait.until(EC.visibility_of_element_located((By.ID, "address")))
    address_area.send_keys("My Address")
    time.sleep(3)

    continue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Continue"]')))
    continue_button.click()
    time.sleep(6)

    # Wait for the radio button with ID "INR" to be clickable
    wait = WebDriverWait(driver, 10)
    radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="INR"]')))

    # Click the "None" radio button
    radio_button.click()
    time.sleep(3)

    continue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Continue"]')))
    continue_button.click()
    time.sleep(6)

    name_field=driver.find_element(By.ID,'contactName')
    name_field.send_keys("Oblu")
    time.sleep(3)

    email_field=driver.find_element(By.ID,'contactEmail')
    email_field.send_keys("madderladder68@gmail.com")
    time.sleep(3)

    continue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Continue"]')))
    continue_button.click()
    time.sleep(6)

    company_business_name=driver.find_element(By.ID,'contactNumber')
    company_business_name.send_keys("OBLU")
    time.sleep(3)

    continue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Continue"]')))
    continue_button.click()
    time.sleep(6)

    # Wait until the dropdown is present
    country_dropdown = wait.until(EC.presence_of_element_located((By.ID, "countryId")))

    # Wrap it in Select and choose India by value
    select = Select(country_dropdown)
    select.select_by_value("IN")

    time.sleep(3)

    region_dropdown = wait.until(EC.presence_of_element_located((By.ID, "regionId")))

    select = Select(region_dropdown)
    select.select_by_value('781499')

    time.sleep(3)

    city_dropdown = wait.until(EC.presence_of_element_located((By.ID, "cityId")))

    select = Select(city_dropdown)
    select.select_by_value('276454')
    time.sleep(3)


    continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success")))
    continue_button.click()
    time.sleep(6)

    phone_number_field=driver.find_element(By.ID,'meta_new-custom-field')
    phone_number_field.send_keys("9650447099")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success")))
    continue_button.click()
    time.sleep(6)

    webseite_url_field=driver.find_element(By.ID,'q1')
    webseite_url_field.send_keys("https://obluhc.com/")
    time.sleep(3)
    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    # Wait for the "None" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    none_radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="None"]')))

    # Click the "None" radio button
    none_radio_button.click()
    time.sleep(3)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    # Wait for the "None" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    daytime_radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="Daytime"]')))

    # Click the "daytime" radio button
    daytime_radio_button.click()
    time.sleep(3)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)



    # Wait for the "business_day" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    business_day_radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="1–2 business days"]')))

    business_day_radio_button.click()
    time.sleep(3)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)


    wait = WebDriverWait(driver, 10)
    yes_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="Yes"]')))

    yes_radio_button.click()
    time.sleep(3)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    keyword_field=driver.find_element(By.ID,'keywords')
    keyword_field.send_keys(Keyword)
    time.sleep(3)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    input("End?")

def wallclassifieds(Title, Description, keyword,target_url):
    driver = get_driver()

    driver.get("https://itemlist.wallclassifieds.com/post-a-free-ad-process-type.php")

    time.sleep(5)

    # Wait for the radio buttons to be present
    wait = WebDriverWait(driver, 10)
    radio_buttons = wait.until(EC.presence_of_all_elements_located((By.NAME, "typenow")))

    # Click the "Business" radio button (2nd one)
    radio_buttons[1].click()

    time.sleep(2)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    # Step 3: On the next page, wait for and click "Post a Classified Ad"
    classified_ad_link = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Post a Classified Ad")
    ))
    classified_ad_link.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "India"
    india_button = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "India")
    ))
    india_button.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "Email"
    by_email = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "By Email")
    ))
    by_email.click()

    time.sleep(3)

    wait = WebDriverWait(driver, 10)
    health_label = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="56"]')))

    # Click on the label (which will check the radio button)
    health_label.click()

    time.sleep(3)
    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))

    # Click the button
    continue_button.click()

    time.sleep(5)

    # Wait for the input to be visible and interactable
    title_input = wait.until(EC.visibility_of_element_located((By.ID, "titleen_US")))

    # Send text to the input
    title_input.send_keys(Title)

    time.sleep(3)

    # Wait for the textarea to be visible
    description_area = wait.until(EC.visibility_of_element_located((By.ID, "descriptionen_US")))

    # Send text to the textarea
    description_area.send_keys(Description)

    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    address_area = wait.until(EC.visibility_of_element_located((By.ID, "address")))
    address_area.send_keys("Rani Bagh, Delhi")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    # Wait for the radio button with ID "INR" to be clickable
    wait = WebDriverWait(driver, 10)
    inr_radio_button = wait.until(EC.element_to_be_clickable((By.ID, "currency_INR")))

    # Click the radio button
    inr_radio_button.click()

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    name_field = driver.find_element(By.ID, 'contactName')
    name_field.send_keys("Oblu")
    time.sleep(3)

    email_field = driver.find_element(By.ID, 'contactEmail')
    email_field.send_keys("koushal.obluhc@gmail.com")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    company_business_name = driver.find_element(By.ID, 'bizorcompanyname')
    company_business_name.send_keys("OBLU")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    # Wait until the dropdown is present
    country_dropdown = wait.until(EC.presence_of_element_located((By.ID, "countryId")))

    # Wrap it in Select and choose India by value
    select = Select(country_dropdown)
    select.select_by_value("IN")

    time.sleep(3)

    region_dropdown = wait.until(EC.presence_of_element_located((By.ID, "regionId")))

    select = Select(region_dropdown)
    select.select_by_value('781499')

    time.sleep(3)

    city_dropdown = wait.until(EC.presence_of_element_located((By.ID, "cityId")))

    select = Select(city_dropdown)
    select.select_by_value('276454')
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    phone_number_field = driver.find_element(By.ID, 'meta_new-custom-field_1')
    phone_number_field.send_keys("9650447099")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    webseite_url_field = driver.find_element(By.ID, 'q1')
    webseite_url_field.send_keys(target_url)
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(3)

    # Wait for the "None" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    none_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="None"]')))

    # Click the "None" radio button
    none_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for the "None" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    daytime_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="Daytime"]')))

    # Click the "None" radio button
    daytime_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for the "business_day" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    business_day_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="1–2 business days"]')))

    business_day_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    wait = WebDriverWait(driver, 10)
    yes_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="Yes"]')))

    yes_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    keyword_field = driver.find_element(By.ID, 'k1')
    keyword_field.send_keys(keyword)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Find the element using the class name and click it
    button = driver.find_element(By.XPATH, '//a[@class="myButton"]')
    button.click()
    time.sleep(6)


    print("https://www.wallclassifieds.com/item-success")
    input("END?")
    return("https://www.wallclassifieds.com/item-success")

def classifiedfactors(Title, Description, keyword,target_url):
    driver = get_driver()

    driver.get("https://items.classifiedsfactor.com/post-a-classified-ad-type.php")

    time.sleep(5)

    # Wait for the radio buttons to be present
    wait = WebDriverWait(driver, 10)
    radio_buttons = wait.until(EC.presence_of_all_elements_located((By.NAME, "typenow")))

    # Click the "Business" radio button (2nd one)
    radio_buttons[1].click()

    time.sleep(2)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    # Step 3: On the next page, wait for and click "Post a Classified Ad"
    classified_ad_link = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Post a Classified Ad")
    ))
    classified_ad_link.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "India"
    india_button = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "India")
    ))
    india_button.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "Email"
    by_email = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "By Email")
    ))
    by_email.click()

    time.sleep(3)

    wait = WebDriverWait(driver, 10)
    health_label = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="22"]')))

    # Click on the label (which will check the radio button)
    health_label.click()

    time.sleep(3)
    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))

    # Click the button
    continue_button.click()

    time.sleep(5)

    # Wait for the input to be visible and interactable
    title_input = wait.until(EC.visibility_of_element_located((By.ID, "titleen_US")))

    # Send text to the input
    title_input.send_keys(Title)

    time.sleep(3)

    # Wait for the textarea to be visible
    description_area = wait.until(EC.visibility_of_element_located((By.ID, "descriptionen_US")))

    # Send text to the textarea
    description_area.send_keys(Description)

    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    address_area = wait.until(EC.visibility_of_element_located((By.ID, "address")))
    address_area.send_keys("Rani Bagh, Delhi")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)
    # Wait for the radio button with ID "INR" to be clickable
    wait = WebDriverWait(driver, 10)
    inr_radio_button = wait.until(EC.element_to_be_clickable((By.ID, "INR")))

    # Click the radio button
    inr_radio_button.click()

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    name_field = driver.find_element(By.ID, 'contactName')
    name_field.send_keys("Oblu")
    time.sleep(3)

    email_field = driver.find_element(By.ID, 'contactEmail')
    email_field.send_keys("koushal.obluhc@gmail.com")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    company_business_name = driver.find_element(By.ID, 'bizorcompanyname')
    company_business_name.send_keys("OBLU")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    # Wait until the dropdown is present
    country_dropdown = wait.until(EC.presence_of_element_located((By.ID, "countryId")))

    # Wrap it in Select and choose India by value
    select = Select(country_dropdown)
    select.select_by_value("IN")

    time.sleep(3)

    region_dropdown = wait.until(EC.presence_of_element_located((By.ID, "regionId")))

    select = Select(region_dropdown)
    select.select_by_value('781499')

    time.sleep(3)




    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    phone_number_field = driver.find_element(By.ID, 'meta_new-custom-field')
    phone_number_field.send_keys("9650447099")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    webseite_url_field = driver.find_element(By.ID, 'q1')
    webseite_url_field.send_keys(target_url)
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(3)

    # Wait for the "None" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    none_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="None"]')))

    # Click the "None" radio button
    none_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for the "None" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    daytime_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="Daytime (8 AM – 5 PM)"]')))

    # Click the "None" radio button
    daytime_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for the "business_day" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    business_day_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="1–2 business days"]')))

    business_day_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    wait = WebDriverWait(driver, 10)
    yes_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="Yes"]')))

    yes_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    keyword_field = driver.find_element(By.ID, 'keywords')
    keyword_field.send_keys(keyword)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Find the element using the class name and click it
    button = driver.find_element(By.XPATH, '//a[@class="myButton"]')
    button.click()
    time.sleep(6)



    print("https://www.classifiedsfactor.com/item-success")
    input("END?")
    return ("https://www.classifiedsfactor.com/item-success")



#IMAGES
def pinterest_upload(id,password,image_path,title,description,keyword,link):
    driver = get_driver()
    driver.get("https://www.pinterest.com/")
    time.sleep(3)

    search_box = driver.find_element(By.ID, "email")
    search_box.send_keys(id)
    time.sleep(3)

    password_box=driver.find_element(By.ID, "password")
    password_box.send_keys(password+Keys.ENTER)
    time.sleep(10)


    driver.get("https://in.pinterest.com/pin-creation-tool/")

    time.sleep(10)

    # Wait until the input is present and clickable
    wait = WebDriverWait(driver, 10)
    upload_input = wait.until(EC.presence_of_element_located((By.ID, "storyboard-upload-input")))




    # Upload the image
    upload_input.send_keys(image_path)

    time.sleep(3)
    #TITLE
    title_box=driver.find_element(By.ID,"storyboard-selector-title")
    title_box.send_keys(title)

    time.sleep(2)

    # Description
    # Wait until the Draft.js editor is visible
    wait = WebDriverWait(driver, 20)
    editor = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.public-DraftEditor-content[contenteditable='true']")
    ))

    # Click to focus (important for Draft.js editors)
    editor.click()

    # Send text
    editor.send_keys(description)

    time.sleep(3)
    # Link Upload
    link_box=driver.find_element(By.ID,"WebsiteField")
    link_box.send_keys(link)

    time.sleep(3)

    tags_box=driver.find_element(By.ID, "storyboard-selector-interest-tags")
    tags_box.send_keys(keyword)

    time.sleep(3)

    publish_button = driver.find_element(By.XPATH, "//div[text()='Publish']")
    publish_button.click()

    time.sleep(5)

    current_url = driver.current_url
    print("Current URL:", current_url)
    input("end?")



    # BOT PROTECTION
    # pinterest_upload("ladm5716@gmail.com","absolutemadlad",image_path,"3D Dental Printer | Precision Printing Solutions | Buy Now","Shop advanced 3D dental printers for high-precision models and appliances. Perfect for dental labs and clinics. Order today for fast delivery and support!","Printer 3D Dental","https://obluhc.com/collections/3d-printers")

def clipix_upload(id,password,image_path,title,description,link):
    driver = get_driver()

    driver.get("https://www.clipix.com/login")
    time.sleep(10)

    Email_Box=driver.find_element(By.ID,"Email")
    Email_Box.send_keys(id)

    time.sleep(2)

    Password_box=driver.find_element(By.ID,"Password")
    Password_box.send_keys(password+Keys.ENTER)

    time.sleep(5)

    driver.get("https://www.clipix.com/home")

    time.sleep(10)

    add_button=driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Add Content"]')
    add_button.click()

    time.sleep(2)

    wait = WebDriverWait(driver, 10)
    upload_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Upload a File"]')))
    upload_button.click()

    # Wait for the file input to be present
    file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]')))

    # Upload a file (can be absolute path to any file on your local system)
    file_input.send_keys(image_path)

    time.sleep(3)

    desc_box=driver.find_element(By.ID,'clipDescription-1')
    desc_box.send_keys(description+"  "+link)

    time.sleep(3)

    # Click the "Save to:" dropdown button
    save_to_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[.//span[contains(text(), "Save")]]')
    ))
    save_to_button.click()

    time.sleep(3)
    # Click the "Welcome to Clipix®" list item
    clipix_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[@id="1387645"]')
    ))
    clipix_button.click()

    time.sleep(3)

    # Click the "Save" button
    save_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[normalize-space()="Save"]')
    ))
    save_button.click()
    input("finished? ")

def imgbb(id,password,image_path,title,description,link):
    driver = get_driver()

    driver.get("https://imgbb.com/login")

    time.sleep(3)
    email_box=driver.find_element(By.ID,'login-subject')
    email_box.send_keys(id)

    time.sleep(3)
    password_box=driver.find_element(By.ID,'login-password')
    password_box.send_keys(password+Keys.ENTER)

    time.sleep(10)

    driver.get("https://imgbb.com/login")
    time.sleep(3)

    # Make the file input visible if it's hidden (optional but often necessary)
    driver.execute_script("document.getElementById('anywhere-upload-input').style.display = 'block';")

    # Locate the file input element
    file_input = driver.find_element(By.ID, "anywhere-upload-input")
    file_input.send_keys(image_path)

    time.sleep(3)

    # Wait until the edit button is clickable
    edit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.queue-item-button.edit[title='Edit']"))
    )

    # Click the button
    edit_button.click()

    time.sleep(3)

    title_box = driver.find_element(By.ID,'form-title')
    title_box.send_keys(title)

    time.sleep(3)

    description_box= driver.find_element(By.ID,'form-description')
    description_box.send_keys(description+link)

    time.sleep(3)
    # Wait until the submit button is clickable
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-input.default[data-action='submit']"))
    )

    # Click the submit button
    submit_button.click()

    time.sleep(3)

    # Locate the "Upload" button using its class name
    upload_button = driver.find_element(By.XPATH, "//button[@data-action='upload']")

    # Click the button
    upload_button.click()

    time.sleep(10)

    try:
        # Locate the "copy" button using XPath based on the data-action attribute
        copy_button = driver.find_element(By.XPATH, "//button[@data-action='copy']")

        # Click the button
        copy_button.click()
        print(pyperclip.paste())
    except:
        print("failed")
    input("end?")

def tumblr(id,password,image_path,title,description,keyword,link):
    driver = get_driver()

    driver.get("https://www.tumblr.com/login")

    # Wait until the email input is visible and interactable
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "email"))
    )

    # Clear any pre-filled text (optional)
    email_input.clear()

    # Send text to the input field
    email_input.send_keys(id)  # Replace with desired email

    time.sleep(5)

    # Wait until the password input is visible and interactable
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "password"))
    )

    # Clear any pre-filled text (optional)
    password_input.clear()

    # Send text to the password field
    password_input.send_keys(password+Keys.ENTER)  # Replace with your actual password

    time.sleep(10)

    driver.get("https://www.tumblr.com/new/photo")

    time.sleep(3)

    # Locate the hidden file input (assumes only one or use more specific selector)
    file_input = driver.find_element(By.CSS_SELECTOR, 'span.EvhBA input[type="file"]')
    file_input.send_keys(image_path)  # Replace with actual image paths

    time.sleep(3)


    # Wait for the contenteditable <p> to be visible
    editable_paragraph = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p[contenteditable='true']"))
    )

    # Click to focus
    editable_paragraph.click()

    # Send text to the contenteditable element
    editable_paragraph.send_keys(description+link)

    time.sleep(3)

    # Locate the textarea using its placeholder attribute
    textarea = driver.find_element(By.XPATH, "//textarea[@placeholder='#add tags']")

    # Send keys to the textarea
    textarea.send_keys(keyword)

    # Locate the "Post now" button using XPath based on the span text
    post_now_button = driver.find_element(By.XPATH, "//button[span[text()='Post now']]")

    # Click the button
    post_now_button.click()

    time.sleep(3)
    input("end?")


# BLOGS

def livepositively(id,password,title,description,link):
    driver = get_driver()
    driver.get("https://livepositively.com/login/")
    time.sleep(3)

    email_box=driver.find_element(By.ID,'email')
    email_box.send_keys(id)

    cont_button=driver.find_element(By.ID,'btn_submit')
    cont_button.click()

    time.sleep(3)

    password_box=driver.find_element(By.ID,'password')
    password_box.send_keys(password+Keys.ENTER)

    time.sleep(7)

    driver.get("https://livepositively.com/me/write.php")

    time.sleep(3)
    title_box=driver.find_element(By.ID,'titre')
    title_box.send_keys(title)

    time.sleep(3)

    # Locate the dropdown element by its ID
    dropdown_element = driver.find_element(By.ID,"categorie")
    dropdown = Select(dropdown_element)
    # Select the "Health" option by visible text
    dropdown.select_by_visible_text("Health")

    time.sleep(3)

    # Switch to the iframe
    iframe = driver.find_element(By.ID, "description_complet_ifr")
    driver.switch_to.frame(iframe)

    # Find the text area inside the iframe
    # In case of TinyMCE, this is typically inside the body or the div
    editor_area = driver.find_element(By.CSS_SELECTOR, "body")

    # Send text input to the editor
    editor_area.send_keys(description)

    # If you're done editing, switch back to the main content
    driver.switch_to.default_content()


    time.sleep(3)

    # Find the button using the aria-label or title (these are unique to this button)
    button = driver.find_element(By.XPATH, "//button[@aria-label='Insert/edit link']")

    # Click the button
    button.click()

    time.sleep(3)

    url_box= driver.find_element(By.XPATH, "//input[@type='url']")
    url_box.send_keys(link)

    time.sleep(3)

    # Find the "Save" button using the title attribute
    save_button = driver.find_element(By.XPATH, "//button[@title='Save']")



    # Click the "Save" button
    save_button.click()


    publish_button=driver.find_element(By.ID,'saveButton')
    publish_button.click()
    time.sleep(10)

    publish_button=driver.find_element(By.ID,'saveButton')
    publish_button.click()
    time.sleep(10)

    # Get the current URL
    current_url = driver.current_url
    print("Current URL:", current_url)

    input("end?")

# livepositively("madderladder68@gmail.com","absolutemadderl","Multi-Layer Aligner Sheet | Strength & Comfort | Buy Now","Explore top 3D printing companies in India. Compare services, get quotes, and choose the best fit for your needs. Start your 3D printing journey today!","https://obluhc.com/collections/3d-printers")

# livepositively("madderladder68@gmail.com","absolutemadderl","PET-C Aligner Sheet | Crystal Clear & Strong | Buy Now","Shop premium PET-C aligner sheets for high clarity, strength, and comfort. Perfect for precise orthodontic treatments. Order today for fast delivery!","https://obluhc.com/collections/aligner-sheets/products/erkodur-al-aligner-sheet")


def chatterchat(id,password,title,description,link):
    driver = get_driver()
    driver.get("https://www.chatterchat.com")

    time.sleep(3)

    email_box=driver.find_element(By.ID,'username')
    email_box.send_keys(id)
    time.sleep(3)
    password_box=driver.find_element(By.ID,'password')
    password_box.send_keys(password+Keys.ENTER)


    time.sleep(7)

    # Wait for the textarea to be visible
    textarea_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,"//textarea[@name='postText']"))
    )

    # Send text to the textarea
    textarea_element.send_keys(description+link+Keys.ENTER)
    textarea_element.click()
    time.sleep(3)

    post_button=driver.find_element(By.ID,'publisher-button')
    post_button.click()
    time.sleep(10)

    # Get the current URL
    current_url = driver.current_url
    print("Current URL:", current_url)
    print("https://chatterchat.com/madderladder")

    input("end?")

# chatterchat("madderladder","Absolutemadderladder1","PET-C Aligner Sheet | Crystal Clear & Strong | Buy Now","Shop premium PET-C aligner sheets for high clarity, strength, and comfort. Perfect for precise orthodontic treatments. Order today for fast delivery!","https://obluhc.com/collections/aligner-sheets/products/erkodur-al-aligner-sheet")


#CLASSIFIED Tags

def yookalo2(Title,Description,Keyword,target_url):
    driver = get_driver()
    driver.get("https://posts.yookalo.com/list-an-ad-steps.php")
    # Optional: Wait for the page to load fully
    time.sleep(15)

    driver.set_window_size(1920, 1080)
    # ---Step 2---
    wait = WebDriverWait(driver, 10)
    checkmark_xpath = "//label[contains(., 'Business')]/span[@class='checkmark']"
    checkmark = wait.until(EC.element_to_be_clickable((By.XPATH, checkmark_xpath)))
    checkmark.click()


    driver.find_element(By.CLASS_NAME, "myButton").click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "Post a Classified Ad"
    classified_ad_link = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Post a Classified Ad")
    ))
    classified_ad_link.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "India"
    india_button = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "India")
    ))
    india_button.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "Email"
    by_email = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "By Email")
    ))
    by_email.click()

    time.sleep(3)

    health_label = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="56"]')))

    # Click on the label (which will check the radio button)
    health_label.click()

    time.sleep(5)
    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()


    time.sleep(3)

    # Wait for the input to be visible and interactable
    title_input = wait.until(EC.visibility_of_element_located((By.ID, "titleen_US")))

    # Send text to the input
    title_input.send_keys(Title)

    time.sleep(3)

    # Wait for the textarea to be visible
    description_area = wait.until(EC.visibility_of_element_located((By.ID, "descriptionen_US")))

    # Send text to the textarea
    description_area.send_keys(Description)

    time.sleep(3)

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    address_area = wait.until(EC.visibility_of_element_located((By.ID, "address")))
    address_area.send_keys("Rani Bagh Delhi")

    time.sleep(3)

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    # Wait for and click the "INR" currency radio button
    inr_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='inr']")))
    inr_label.click()

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    Name_area = wait.until(EC.visibility_of_element_located((By.ID, "contactName")))
    Name_area.send_keys("OBLU")

    email_area = wait.until(EC.visibility_of_element_located((By.ID, "contactEmail")))
    email_area.send_keys("koushal.obluhc@gmail.com")

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    company_name_area = wait.until(EC.visibility_of_element_located((By.ID, "bizorcompanyname")))
    company_name_area.send_keys("OBLU")

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    # Wait until the dropdown is present
    country_dropdown = wait.until(EC.presence_of_element_located((By.ID, "countryId")))

    # Wrap it in Select and choose India by value
    select = Select(country_dropdown)
    select.select_by_value("IN")

    time.sleep(3)

    region_dropdown= wait.until(EC.presence_of_element_located((By.ID, "regionId")))

    select=Select(region_dropdown)
    select.select_by_value('781499')

    time.sleep(3)

    city_dropdown=wait.until(EC.presence_of_element_located((By.ID, "cityId")))

    select=Select(city_dropdown)
    select.select_by_value('276454')


    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    phone_field=driver.find_element(By.ID, "meta_new-custom-field")
    phone_field.send_keys("9650447099")

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    website_url=driver.find_element(By.ID, "q1")
    website_url.send_keys(target_url)


    continue_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_link.click()

    time.sleep(3)


    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)



    facebook_url=driver.find_element(By.ID, "q3")
    facebook_url.send_keys("https://www.facebook.com/obluhealthcare")

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)


    facebook_url=driver.find_element(By.ID, "q4")
    facebook_url.send_keys("https://www.instagram.com/oblu_healthcare/")


    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)


    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)

    #  Wait for and click the "Continue" button (submit)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(text(), 'Continue')]")
    ))
    submit_button.click()

    time.sleep(3)



    # Wait for and click the "Continue" button
    submit_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Submit")))
    submit_button.click()
    time.sleep(6)

    input("ENd?")

# yookalo("3D Printer for Dental | High-Precision Printing Solutions","Discover cutting-edge 3D printers for dental applications. Enhance your practice with high-precision, reliable, and cost-effective solutions for clear aligners, crowns, and more. Upgrade your dental technology today. Explore our range now!  https://obluhc.com/collections/3d-printers","3d printer for dental","https://obluhc.com/collections/3d-printers")
# #
# yookalo("PET-G Aligner Sheet | Clear, Strong & Safe | Buy Now","Explore high-quality PET-G aligner sheets designed for strength, transparency, and biocompatibility. Ideal for dental aligners. Order now for fast delivery!  https://obluhc.com/collections/aligner-sheets/products/erkodur-aligner-sheets","Pet G Aligner Sheet","https://obluhc.com/collections/aligner-sheets/products/erkodur-aligner-sheets")

def findmaster2(Title,Description,keyword,target_url):
    driver = get_driver()
    driver.get("https://listings.findermaster.com/post-a-free-ad-process-type.php")

    time.sleep(5)
    driver.set_window_size(1920, 1080)

    # Wait for the radio buttons to be present
    wait = WebDriverWait(driver, 10)
    radio_buttons = wait.until(EC.presence_of_all_elements_located((By.NAME, "typenow")))

    # Click the "Business" radio button (2nd one)
    radio_buttons[1].click()

    time.sleep(2)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()

    # Step 3: On the next page, wait for and click "Post a Classified Ad"
    classified_ad_link = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Post a Classified Ad")
    ))
    classified_ad_link.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "India"
    india_button = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "India")
    ))
    india_button.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "Email"
    by_email = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "By Email")
    ))
    by_email.click()

    time.sleep(3)

    wait = WebDriverWait(driver, 10)
    health_label = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="56"]')))

    # Click on the label (which will check the radio button)
    health_label.click()

    time.sleep(3)
    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))

    # Click the button
    continue_button.click()

    time.sleep(5)

    # Wait for the input to be visible and interactable
    title_input = wait.until(EC.visibility_of_element_located((By.ID, "titleen_US")))

    # Send text to the input
    title_input.send_keys(Title)

    time.sleep(3)

    # Wait for the textarea to be visible
    description_area = wait.until(EC.visibility_of_element_located((By.ID, "descriptionen_US")))

    # Send text to the textarea
    description_area.send_keys(Description)

    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    address_area = wait.until(EC.visibility_of_element_located((By.ID, "address")))
    address_area.send_keys("Rani Bagh, Delhi")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    # Wait for the radio button with ID "INR" to be clickable
    wait = WebDriverWait(driver, 10)
    inr_radio_button = wait.until(EC.element_to_be_clickable((By.ID, "INR")))

    # Click the radio button
    inr_radio_button.click()

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    name_field=driver.find_element(By.ID,'contactName')
    name_field.send_keys("Oblu")
    time.sleep(3)

    email_field=driver.find_element(By.ID,'contactEmail')
    email_field.send_keys("koushal.obluhc@gmail.com")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    company_business_name=driver.find_element(By.ID,'companyorbusinessname')
    company_business_name.send_keys("OBLU")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)


    # Wait until the dropdown is present
    country_dropdown = wait.until(EC.presence_of_element_located((By.ID, "countryId")))

    # Wrap it in Select and choose India by value
    select = Select(country_dropdown)
    select.select_by_value("IN")

    time.sleep(3)

    region_dropdown= wait.until(EC.presence_of_element_located((By.ID, "regionId")))

    select=Select(region_dropdown)
    select.select_by_value('781499')

    time.sleep(3)

    city_dropdown=wait.until(EC.presence_of_element_located((By.ID, "cityId")))

    select=Select(city_dropdown)
    select.select_by_value('276454')
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    phone_number_field=driver.find_element(By.ID,'meta_new-custom-field')
    phone_number_field.send_keys("9650447099")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)


    webseite_url_field=driver.find_element(By.ID,'q1')
    webseite_url_field.send_keys(target_url)
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(3)


    # Wait for the "None" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    none_radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="None"]')))

    # Click the "None" radio button
    none_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    # Wait for the "None" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    daytime_radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="Daytime"]')))

    # Click the "None" radio button
    daytime_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for the "business_day" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    business_day_radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="1–2 business days"]')))


    business_day_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    wait = WebDriverWait(driver, 10)
    yes_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="Yes"]')))

    yes_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    keyword_field=driver.find_element(By.ID,'w1')
    keyword_field.send_keys(keyword)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    facebook_url=driver.find_element(By.ID,'q3')
    facebook_url.send_keys("https://www.facebook.com/obluhealthcare")


    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)



    insta_url=driver.find_element(By.ID, "q4")
    insta_url.send_keys("https://www.instagram.com/oblu_healthcare/")
    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)



    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    linkdin_url=driver.find_element(By.ID,'lt1')
    linkdin_url.send_keys("https://in.linkedin.com/company/oblu-healthcare-llp")

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    submit_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Submit")))
    submit_button.click()
    time.sleep(6)




    input("END?")

#9650447099

# findmaster("Top Dental 3D Printers for Accurate & Efficient Dental Solutions","Explore the best dental 3D printers for precision and efficiency. Enhance your dental practice with cutting-edge technology that ensures accurate results. Discover more today and take your practice to the next level with our reliable 3D printers!  https://obluhc.com/collections/3d-printers","dental 3d printer","https://obluhc.com/collections/3d-printers")
# #
# findmaster("PET-G Aligner Sheet | Clear, Strong & Safe | Buy Now","Explore high-quality PET-G aligner sheets designed for strength, transparency, and biocompatibility. Ideal for dental aligners. Order now for fast delivery!  https://obluhc.com/collections/aligner-sheets/products/erkodur-aligner-sheets","Pet G Aligner Sheet","https://obluhc.com/collections/aligner-sheets/products/erkodur-aligner-sheets")
# #


def h1ad2(Title,Description,Keyword,target_url):
    driver=get_driver()
    driver.get("https://postjourney.h1ad.com/post-a-classified-ad-process.php")

    time.sleep(5)
    driver.set_window_size(1920, 1080)
    # Wait for the radio buttons to be present
    wait = WebDriverWait(driver, 10)
    radio_buttons = wait.until(EC.presence_of_all_elements_located((By.NAME, "typenow")))

    # Click the "Business" radio button (2nd one)
    radio_buttons[1].click()

    time.sleep(2)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "Post a Classified Ad"
    classified_ad_link = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Post a Classified Ad")
    ))
    classified_ad_link.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "India"
    india_button = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "India")
    ))
    india_button.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "Email"
    by_email = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "By Email")
    ))
    by_email.click()

    time.sleep(3)


    try:
        radio_button = wait.until(EC.element_to_be_clickable((By.ID, 'catId_5')))
        radio_button.click()
    except:
        # Fallback: use JS click
        radio_button = driver.find_element(By.ID, 'catId_5')
        driver.execute_script("arguments[0].click();", radio_button)


    time.sleep(3)
    continue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Continue"]')))
    continue_button.click()
    time.sleep(6)


    # Wait for the input to be visible and interactable
    title_input = wait.until(EC.visibility_of_element_located((By.ID, "titleen_US")))

    # Send text to the input
    title_input.send_keys(Title)

    time.sleep(3)

    # Wait for the textarea to be visible
    description_area = wait.until(EC.visibility_of_element_located((By.ID, "descriptionen_US")))

    # Send text to the textarea
    description_area.send_keys(Description)

    time.sleep(3)

    continue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Continue"]')))
    continue_button.click()
    time.sleep(6)

    address_area = wait.until(EC.visibility_of_element_located((By.ID, "address")))
    address_area.send_keys("Rani Bagh, Delhi")
    time.sleep(3)

    continue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Continue"]')))
    continue_button.click()
    time.sleep(6)

    # Wait for the radio button with ID "INR" to be clickable
    wait = WebDriverWait(driver, 10)
    radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="INR"]')))

    # Click the "None" radio button
    radio_button.click()
    time.sleep(3)

    continue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Continue"]')))
    continue_button.click()
    time.sleep(6)

    name_field=driver.find_element(By.ID,'contactName')
    name_field.send_keys("Oblu")
    time.sleep(3)

    email_field=driver.find_element(By.ID,'contactEmail')
    email_field.send_keys("koushal.obluhc@gmail.com")
    time.sleep(3)

    continue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Continue"]')))
    continue_button.click()
    time.sleep(6)

    company_business_name=driver.find_element(By.ID,'contactNumber')
    company_business_name.send_keys("OBLU")
    time.sleep(3)

    continue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Continue"]')))
    continue_button.click()
    time.sleep(6)

    # Wait until the dropdown is present
    country_dropdown = wait.until(EC.presence_of_element_located((By.ID, "countryId")))

    # Wrap it in Select and choose India by value
    select = Select(country_dropdown)
    select.select_by_value("IN")

    time.sleep(3)

    region_dropdown = wait.until(EC.presence_of_element_located((By.ID, "regionId")))

    select = Select(region_dropdown)
    select.select_by_value('781499')

    time.sleep(3)

    city_dropdown = wait.until(EC.presence_of_element_located((By.ID, "cityId")))

    select = Select(city_dropdown)
    select.select_by_value('276454')
    time.sleep(3)


    continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success")))
    continue_button.click()
    time.sleep(6)

    phone_number_field=driver.find_element(By.ID,'meta_new-custom-field')
    phone_number_field.send_keys("9650447099")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success")))
    continue_button.click()
    time.sleep(6)

    webseite_url_field=driver.find_element(By.ID,'q1')
    webseite_url_field.send_keys(target_url)
    time.sleep(3)
    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    # Wait for the "None" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    none_radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="None"]')))

    # Click the "None" radio button
    none_radio_button.click()
    time.sleep(3)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    # Wait for the "None" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    daytime_radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="Daytime"]')))

    # Click the "daytime" radio button
    daytime_radio_button.click()
    time.sleep(3)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)



    # Wait for the "business_day" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    business_day_radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="1–2 business days"]')))

    business_day_radio_button.click()
    time.sleep(3)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)


    wait = WebDriverWait(driver, 10)
    yes_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="Yes"]')))

    yes_radio_button.click()
    time.sleep(3)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    keyword_field=driver.find_element(By.ID,'keywords')
    keyword_field.send_keys(Keyword)
    time.sleep(3)


    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)


    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)


    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)


    facebook_url=driver.find_element(By.ID,'facebook_url')
    facebook_url.send_keys("https://www.facebook.com/obluhealthcare")

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)


    insta_url=driver.find_element(By.ID, "instagram_url")
    insta_url.send_keys("https://www.instagram.com/oblu_healthcare/")

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)


    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    continue_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Continue']")
    ))
    continue_link.click()
    time.sleep(6)

    # Find the element using the class name and click it
    button = driver.find_element(By.XPATH, '//a[@class="myButton"]')
    button.click()
    time.sleep(6)

    input("end?")
    return("https://www.h1ad.com/item-success")

# h1ad("Top Dental 3D Printers for Accurate & Efficient Dental Solutions","Explore the best dental 3D printers for precision and efficiency. Enhance your dental practice with cutting-edge technology that ensures accurate results. Discover more today and take your practice to the next level with our reliable 3D printers!  https://obluhc.com/collections/3d-printers","dental 3d printer","https://obluhc.com/collections/3d-printers")
#
# h1ad("Zendura Aligner Sheet | Trusted Strength & Clarity | Buy Now","Shop original Zendura aligner sheets for superior strength, crack resistance, and clear aesthetics. Ideal for premium orthodontic results. Order now! https://obluhc.com/collections/aligner-sheets ","Zendura Aligner Sheet","https://obluhc.com/collections/aligner-sheets")


def wallclassifieds2(Title, Description, keyword, target_url, wait=None):
    driver = get_driver()
    driver.get("https://itemlist.wallclassifieds.com/post-a-free-ad-process-type.php")

    time.sleep(5)
    driver.set_window_size(1920, 1080)

    checkmark_xpath = "//label[contains(., 'Business')]/span[@class='checkmark']"
    checkmark = wait.until(EC.element_to_be_clickable((By.XPATH, checkmark_xpath)))
    checkmark.click()

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "Post a Classified Ad"
    classified_ad_link = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Post a Classified Ad")
    ))
    classified_ad_link.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "India"
    india_button = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "India")
    ))
    india_button.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "Email"
    by_email = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "By Email")
    ))
    by_email.click()

    time.sleep(3)

    wait = WebDriverWait(driver, 10)
    health_label = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="56"]')))

    # Click on the label (which will check the radio button)
    health_label.click()

    time.sleep(3)
    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))

    # Click the button
    continue_button.click()

    time.sleep(5)

    # Wait for the input to be visible and interactable
    title_input = wait.until(EC.visibility_of_element_located((By.ID, "titleen_US")))

    # Send text to the input
    title_input.send_keys(Title)

    time.sleep(3)

    # Wait for the textarea to be visible
    description_area = wait.until(EC.visibility_of_element_located((By.ID, "descriptionen_US")))

    # Send text to the textarea
    description_area.send_keys(Description)

    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    address_area = wait.until(EC.visibility_of_element_located((By.ID, "address")))
    address_area.send_keys("Rani Bagh, Delhi")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    # Wait for the radio button with ID "INR" to be clickable
    wait = WebDriverWait(driver, 10)
    inr_radio_button = wait.until(EC.element_to_be_clickable((By.ID, "currency_INR")))

    # Click the radio button
    inr_radio_button.click()

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    name_field = driver.find_element(By.ID, 'contactName')
    name_field.send_keys("Oblu")
    time.sleep(3)

    email_field = driver.find_element(By.ID, 'contactEmail')
    email_field.send_keys("koushal.obluhc@gmail.com")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    company_business_name = driver.find_element(By.ID, 'bizorcompanyname')
    company_business_name.send_keys("OBLU")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    # Wait until the dropdown is present
    country_dropdown = wait.until(EC.presence_of_element_located((By.ID, "countryId")))

    # Wrap it in Select and choose India by value
    select = Select(country_dropdown)
    select.select_by_value("IN")

    time.sleep(3)

    region_dropdown = wait.until(EC.presence_of_element_located((By.ID, "regionId")))

    select = Select(region_dropdown)
    select.select_by_value('781499')

    time.sleep(3)

    city_dropdown = wait.until(EC.presence_of_element_located((By.ID, "cityId")))

    select = Select(city_dropdown)
    select.select_by_value('276454')
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    phone_number_field = driver.find_element(By.ID, 'meta_new-custom-field_1')
    phone_number_field.send_keys("9650447099")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    webseite_url_field = driver.find_element(By.ID, 'q1')
    webseite_url_field.send_keys(target_url)
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(3)

    # Wait for the "None" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    none_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="None"]')))

    # Click the "None" radio button
    none_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for the "None" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    daytime_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="Daytime"]')))

    # Click the "None" radio button
    daytime_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for the "business_day" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    business_day_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="1–2 business days"]')))

    business_day_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    wait = WebDriverWait(driver, 10)
    yes_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="Yes"]')))

    yes_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    keyword_field = driver.find_element(By.ID, 'k1')
    keyword_field.send_keys(keyword)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    facebook_url=driver.find_element(By.ID,'fb1')
    facebook_url.send_keys("https://www.facebook.com/obluhealthcare")


    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    insta_url=driver.find_element(By.ID, "ig1")
    insta_url.send_keys("https://www.instagram.com/oblu_healthcare/")

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    linkdin_url=driver.find_element(By.ID,'li1')
    linkdin_url.send_keys("https://in.linkedin.com/company/oblu-healthcare-llp")

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Find the element using the class name and click it
    button = driver.find_element(By.XPATH, '//a[@class="myButton"]')
    button.click()
    time.sleep(6)



    input("END?")
    return("https://www.wallclassifieds.com/item-success")


# wallclassifieds("Elegoo 3D Printers: Precision, Reliability, and Innovation","Discover Elegoo's high-quality 3D printers for precision and reliability in every print. Explore a range of advanced models designed for innovation and professional use. Upgrade your 3D printing experience today – Visit our store and find the perfect Elegoo printer for your needs! https://obluhc.com/products/elegoo-saturn-4-ultra-3d-printer","elegoo","https://obluhc.com/products/elegoo-saturn-4-ultra-3d-printer")
# #
# wallclassifieds("Zendura Aligner Sheet | Trusted Strength & Clarity | Buy Now","Shop original Zendura aligner sheets for superior strength, crack resistance, and clear aesthetics. Ideal for premium orthodontic results. Order now! https://obluhc.com/collections/aligner-sheets ","Zendura Aligner Sheet","https://obluhc.com/collections/aligner-sheets")


def classifiedfactors2(Title, Description, keyword,target_url):
    driver = get_driver()
    driver.get("https://items.classifiedsfactor.com/post-a-classified-ad-type.php")

    time.sleep(5)
    driver.set_window_size(1920, 1080)
# Step 2-----
    wait = WebDriverWait(driver, 10)
    checkmark_xpath = "//label[contains(., 'Business')]/span[@class='checkmark']"
    checkmark = wait.until(EC.element_to_be_clickable((By.XPATH, checkmark_xpath)))
    checkmark.click()

    wait = WebDriverWait(driver, 5)
    continue_link = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='myButton' and .//span[text()='Continue']]"))
    )
    continue_link.click()

    # Step 3: On the next page, wait for and click "Post a Classified Ad"
    wait = WebDriverWait(driver, 10)
    classified_ad_link = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Post a Classified Ad")
    ))
    classified_ad_link.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "India"
    wait = WebDriverWait(driver, 10)
    india_button = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "India")
    ))
    india_button.click()

    time.sleep(3)

    # Step 3: On the next page, wait for and click "Email"
    wait = WebDriverWait(driver, 10)
    by_email = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "By Email")
    ))
    by_email.click()

    time.sleep(3)

    wait = WebDriverWait(driver, 10)
    health_label = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="22"]')))

    # Click on the label (which will check the radio button)
    health_label.click()

    time.sleep(3)
    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))

    # Click the button
    continue_button.click()

    time.sleep(5)

    # Wait for the input to be visible and interactable
    title_input = wait.until(EC.visibility_of_element_located((By.ID, "titleen_US")))

    # Send text to the input
    title_input.send_keys(Title)

    time.sleep(3)

    # Wait for the textarea to be visible
    description_area = wait.until(EC.visibility_of_element_located((By.ID, "descriptionen_US")))

    # Send text to the textarea
    description_area.send_keys(Description)

    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    address_area = wait.until(EC.visibility_of_element_located((By.ID, "address")))
    address_area.send_keys("Rani Bagh, Delhi")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)
    # Wait for the radio button with ID "INR" to be clickable
    wait = WebDriverWait(driver, 10)
    inr_radio_button = wait.until(EC.element_to_be_clickable((By.ID, "INR")))

    # Click the radio button
    inr_radio_button.click()

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    name_field = driver.find_element(By.ID, 'contactName')
    name_field.send_keys("Oblu")
    time.sleep(3)

    email_field = driver.find_element(By.ID, 'contactEmail')
    email_field.send_keys("koushal.obluhc@gmail.com")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    company_business_name = driver.find_element(By.ID, 'bizorcompanyname')
    company_business_name.send_keys("OBLU")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    # Wait until the dropdown is present
    country_dropdown = wait.until(EC.presence_of_element_located((By.ID, "countryId")))

    # Wrap it in Select and choose India by value
    select = Select(country_dropdown)
    select.select_by_value("IN")

    time.sleep(3)

    region_dropdown = wait.until(EC.presence_of_element_located((By.ID, "regionId")))

    select = Select(region_dropdown)
    select.select_by_value('781499')

    time.sleep(3)




    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    phone_number_field = driver.find_element(By.ID, 'meta_new-custom-field')
    phone_number_field.send_keys("9650447099")
    time.sleep(3)

    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-center.upcase")))
    # Click the button
    continue_button.click()
    time.sleep(3)

    webseite_url_field = driver.find_element(By.ID, 'q1')
    webseite_url_field.send_keys(target_url)
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(3)

    # Wait for the "None" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    none_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="None"]')))

    # Click the "None" radio button
    none_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for the "None" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    daytime_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="Daytime (8 AM – 5 PM)"]')))

    # Click the "None" radio button
    daytime_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    # Wait for the "business_day" radio button to be clickable
    wait = WebDriverWait(driver, 10)
    business_day_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="1–2 business days"]')))

    business_day_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    wait = WebDriverWait(driver, 10)
    yes_radio_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @value="Yes"]')))

    yes_radio_button.click()
    time.sleep(3)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)

    keyword_field = driver.find_element(By.ID, 'keywords')
    keyword_field.send_keys(keyword)

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    facebook_url=driver.find_element(By.ID,'facebook_url')
    facebook_url.send_keys("https://www.facebook.com/obluhealthcare")

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    insta_url=driver.find_element(By.ID, "instagram_url")
    insta_url.send_keys("https://www.instagram.com/oblu_healthcare/")

    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    # Wait for and click the "Continue" button
    continue_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    continue_button.click()
    time.sleep(6)


    # Find the element using the class name and click it
    button = driver.find_element(By.XPATH, '//a[@class="myButton"]')
    button.click()
    time.sleep(6)




    input("END?")
    return ("https://www.classifiedsfactor.com/item-success")

# classifiedfactors("Elegoo 3D Printers: Precision, Reliability, and Innovation","Discover Elegoo's high-quality 3D printers for precision and reliability in every print. Explore a range of advanced models designed for innovation and professional use. Upgrade your 3D printing experience today – Visit our store and find the perfect Elegoo printer for your needs! https://obluhc.com/products/elegoo-saturn-4-ultra-3d-printer","elegoo","https://obluhc.com/products/elegoo-saturn-4-ultra-3d-printer")
#
# classifiedfactors("Erkodur AL Aligner Sheet | Durable & Clear | Buy Now","Get Erkodur AL aligner sheets for high durability and crystal-clear orthodontic aligners. Perfect for dental labs and clinics. Order today for fast delivery! https://obluhc.com/collections/aligner-sheets/products/erkodur-al-aligner-sheet","Erkodur AL Aligner Sheet","https://obluhc.com/collections/aligner-sheets/products/erkodur-al-aligner-sheet")
#

# yookaloo findmaster



# --- Function placeholder ---
def run_selected():
    selected = automation_choice.get()
    title = entry1.get()
    desc = entry2.get()
    link = entry3.get()
    keyword = entry4.get()

    if not selected:
        messagebox.showwarning("Input Error", "Please choose an automation")
        return
    if selected == "getadsonline":
        getadsonline(title, desc, link)

    elif selected == "postthreads":
        postthreads(title, desc, link)

    elif selected == "postherefree":
        postherefree(title, desc, link)

    elif selected == "ursads":
        ursads(title, desc, link)

    elif selected == "adshoo":
        adshoo(title, desc, link)

    elif selected == "letspostfree":
        letspostfree(title, desc, link)

    elif selected == "yookalo":
        yookalo(title, desc, keyword, link)

    elif selected == "findmaster":
        findmaster(title, desc, keyword, link)

    elif selected == "h1ad":
        h1ad(title, desc, keyword, link)

    elif selected == "wallclassifieds":
        wallclassifieds(title, desc, keyword, link)

    elif selected == "classifiedfactors":
        classifiedfactors(title, desc, keyword, link)

    # For demo
    messagebox.showinfo(
        "Running Automation",
        f"Automation: {selected}\n\nTitle: {title}\nDescription: {desc}\nLink: {link}"
    )

def run_second_selected():
    selected2 = automation_choice2.get()
    input_image_path = entry5.get()
    input_title = entry6.get()
    input_description=entry7.get()
    input_keyword=entry8.get()
    input_link=entry9.get()

    if not selected2:
        messagebox.showwarning("Input Error", "Please choose a second automation")
        return

    # --- Dummy mapping ---
    if selected2 == "pinterest":
        pinterest_upload('ladm5716@gmail.com','absolutemadlad1',input_image_path,input_title,input_description,input_keyword,input_link)

    if selected2 == "clipix":
        clipix_upload("ladm5716@gmail.com","absolutemadlad1",input_image_path,input_title,input_description,input_link)

    if selected2 == 'imgbb':
        imgbb("ladm5716@gmail.com","absolutemadlad1",input_image_path,input_title,input_description,input_link)


    if selected2 == 'tumblr':
        tumblr("ladm5716@gmail.com","absolutemadlad1",input_image_path,input_title,input_description,input_keyword,input_link)


    messagebox.showinfo(
        "Running Second Automation",
        f"Automation: {selected2}\n\nField1: {input_image_path}\nField2: {input_title}"
    )

def run_third_selected():
    selected3 = automation_choice3.get()
    TITLE = entry10.get()
    DESCRIPTION = entry11.get()
    LINK = entry12.get()

    if not selected3:
        messagebox.showwarning("Input Error", "Please choose a second automation")
        return

    # --- Dummy mapping ---
    if selected3 == "livepositively":
        livepositively('madderladder68@gmail.com','absolutemadderl',TITLE,DESCRIPTION,LINK)

    if selected3 == "chatterchat":
        chatterchat("madderladder","Absolutemadderladder1",TITLE,DESCRIPTION,LINK)


    messagebox.showinfo(
        "Running Third Automation",
        f"Automation: {selected3}\n\nTitle: {TITLE}\nDescription: {DESCRIPTION}\nLink: {LINK}"
    )

def run_fourth_selected():
    selected4 = automation_choice4.get()
    TITLE1 = entry13.get()
    DESCRIPTION1 = entry14.get()
    KEYWORD1 = entry15.get()
    LINK1 = entry16.get()

    if not selected4:
        messagebox.showwarning("Input Error", "Please choose a second automation")
        return

    # --- Dummy mapping ---
    if selected4 == "yookalo2":
        yookalo2(TITLE1,DESCRIPTION1,KEYWORD1,LINK1)

    if selected4 == "findmaster2":
        findmaster2(TITLE1,DESCRIPTION1,KEYWORD1,LINK1)

    if selected4 == "h1ad2":
        h1ad2( TITLE1, DESCRIPTION1, KEYWORD1, LINK1)

    if selected4 == "wallclassifieds2":
        wallclassifieds2( TITLE1, DESCRIPTION1, KEYWORD1, LINK1)

    if selected4 == "classifiedfactors2":
        classifiedfactors2( TITLE1, DESCRIPTION1, KEYWORD1, LINK1)


    messagebox.showinfo(
        "Running fourth Automation",
        f"Automation: {selected4}\n\nTitle: {TITLE1}\nDescription: {DESCRIPTION1}\nKeyword: {KEYWORD1}\nLink: {LINK1}"
    )


# --- UI Setup ---
import tkinter as tk
from tkinter import ttk



root = tk.Tk()
root.title("OBLU HC - Marketing Automation Tool")
root.state("zoomed")   # Full screen on Windows

# --- Styles ---
style = ttk.Style()
style.theme_use("clam")

style.configure("Header.TLabel", font=("Segoe UI", 20, "bold"), foreground="#00274D")
style.configure("Section.TLabelframe.Label", font=("Segoe UI", 14, "bold"), foreground="#003366")
style.configure("TLabel", font=("Segoe UI", 12))
style.configure("TEntry", font=("Segoe UI", 12))
style.configure("TButton", font=("Segoe UI", 12, "bold"), padding=8)

# --- Header Bar ---
header_frame = tk.Frame(root, bg="#00274D", height=70)
header_frame.pack(fill="x")

header_label = tk.Label(
    header_frame,
    text="OBLU HC - Marketing Automation Tool",
    font=("Segoe UI", 20, "bold"),
    fg="white",
    bg="#00274D"
)
header_label.pack(pady=15)

# --- Main Content ---
main_frame = ttk.Frame(root, padding=30)
main_frame.pack(fill="both", expand=True)

# Use grid container for side-by-side layout
forms_frame = ttk.Frame(main_frame)
forms_frame.pack(fill="both", expand=True)


# ===============================
# First Automation Section (LEFT)
# ===============================
form_section = ttk.LabelFrame(forms_frame, text="Automation Classified Ads", padding=20, style="Section.TLabelframe")
form_section.grid(row=0, column=0, padx=20, pady=20, sticky="n")

# Dropdown
ttk.Label(form_section, text="Choose Automation:").grid(row=0, column=0, sticky="w", pady=10, padx=10)
automation_choice = ttk.Combobox(
    form_section,
    values=["getadsonline", "postthreads", "postherefree","ursads","adshoo", "letspostfree","yookalo","findmaster","h1ad","wallclassifieds","classifiedfactors"],
    state="readonly", width=40
)
automation_choice.grid(row=0, column=1, pady=10, padx=10)

# Input fields
ttk.Label(form_section, text="Enter Title:").grid(row=1, column=0, sticky="w", pady=10, padx=10)
entry1 = ttk.Entry(form_section, width=42)
entry1.grid(row=1, column=1, pady=10, padx=10)

ttk.Label(form_section, text="Enter Description:").grid(row=2, column=0, sticky="w", pady=10, padx=10)
entry2 = ttk.Entry(form_section, width=42)
entry2.grid(row=2, column=1, pady=10, padx=10)

ttk.Label(form_section, text="Enter Link:").grid(row=3, column=0, sticky="w", pady=10, padx=10)
entry3 = ttk.Entry(form_section, width=42)
entry3.grid(row=3, column=1, pady=10, padx=10)

ttk.Label(form_section, text="Enter Keyword:").grid(row=4, column=0, sticky="w", pady=10, padx=10)
entry4 = ttk.Entry(form_section, width=42)
entry4.grid(row=4, column=1, pady=10, padx=10)

# Button
ttk.Button(form_section, text="▶ Run Classified Ad Automation", command=run_selected).grid(row=5, column=0, columnspan=2, pady=15)


# ===============================
# Second Automation Section (RIGHT)
# ===============================
form_section2 = ttk.LabelFrame(forms_frame, text="Automation Images", padding=80, style="Section.TLabelframe")
form_section2.grid(row=0, column=1, padx=20, pady=20, sticky="n")

forms_frame.columnconfigure(0, weight=1)
forms_frame.columnconfigure(1, weight=1)


# Row 0
ttk.Label(form_section2, text="Choose Automation:").grid(row=0, column=0, sticky="w", pady=10, padx=10)
automation_choice2 = ttk.Combobox(
    form_section2,
    values=["pinterest", "clipix", "imgbb", "tumblr"],
    state="readonly", width=30
)
automation_choice2.grid(row=0, column=1, pady=10, padx=10)

ttk.Label(form_section2, text="Enter Image Path:").grid(row=0, column=2, sticky="w", pady=10, padx=10)
entry5 = ttk.Entry(form_section2, width=30)
entry5.grid(row=0, column=3, pady=10, padx=10)

# Row 1
ttk.Label(form_section2, text="Enter Title:").grid(row=1, column=0, sticky="w", pady=10, padx=10)
entry6 = ttk.Entry(form_section2, width=30)
entry6.grid(row=1, column=1, pady=10, padx=10)

ttk.Label(form_section2, text="Enter Desc:").grid(row=1, column=2, sticky="w", pady=10, padx=10)
entry7 = ttk.Entry(form_section2, width=30)
entry7.grid(row=1, column=3, pady=10, padx=10)

# Row 2
ttk.Label(form_section2, text="Enter Keyword:").grid(row=2, column=0, sticky="w", pady=10, padx=10)
entry8 = ttk.Entry(form_section2, width=30)
entry8.grid(row=2, column=1, pady=10, padx=10)

# Run button at same row
run_btn2 = ttk.Button(form_section2, text="▶ Run Image Automation", command=run_second_selected)
run_btn2.grid(row=2, column=3, pady=10, padx=10, sticky="e")

# Row 3
ttk.Label(form_section2, text="Enter Link:").grid(row=3, column=0, sticky="w", pady=10, padx=10)
entry9 = ttk.Entry(form_section2, width=30)
entry9.grid(row=3, column=1, pady=10, padx=10)


# ===============================
# Third Automation Section (Below)    id,password,title,description,link
# ===============================

# Parent frame for holding both sections
forms_frame = ttk.Frame(main_frame)
forms_frame.pack(fill="both", expand=True, pady=20)

forms_frame.columnconfigure(0, weight=1)
forms_frame.columnconfigure(1, weight=1)


# Left Frame: Blog Automation
form_section3 = ttk.LabelFrame(forms_frame, text="Blog Automation", padding=20, style="Section.TLabelframe")
form_section3.grid(row=0, column=0, sticky="nsew", padx=10, pady=20)

ttk.Label(form_section3, text="Choose Automation:").grid(row=0, column=0, sticky="w", pady=10, padx=10)
automation_choice3 = ttk.Combobox(
    form_section3,
    values=["livepositively", "chatterchat"],
    state="readonly", width=50
)
automation_choice3.grid(row=0, column=1, pady=10, padx=20)

ttk.Label(form_section3, text="Enter Title:").grid(row=1, column=0, sticky="w", pady=10, padx=10)
entry10 = ttk.Entry(form_section3, width=50)
entry10.grid(row=1, column=1, pady=10, padx=10)

ttk.Label(form_section3, text="Enter Description:").grid(row=2, column=0, sticky="w", pady=10, padx=10)
entry11 = ttk.Entry(form_section3, width=50)
entry11.grid(row=2, column=1, pady=10, padx=10)

ttk.Label(form_section3, text="Enter Link:").grid(row=3, column=0, sticky="w", pady=10, padx=10)
entry12 = ttk.Entry(form_section3, width=50)
entry12.grid(row=3, column=1, pady=10, padx=10)

run_btn3 = ttk.Button(form_section3, text="▶ Run Blog Automation", command=run_third_selected)
run_btn3.grid(row=4, column=0, columnspan=2, pady=15)

#---fourth automation---
# Right Frame: Automation Tags
form_section4 = ttk.LabelFrame(forms_frame, text="Automation Tags", padding=20, style="Section.TLabelframe")
form_section4.grid(row=0, column=1, sticky="nsew", padx=10, pady=20)

# Make both columns expand equally
forms_frame.columnconfigure(0, weight=1)
forms_frame.columnconfigure(1, weight=1)

ttk.Label(form_section4, text="Choose Automation:").grid(row=0, column=0, sticky="w", pady=10, padx=10)
automation_choice4 = ttk.Combobox(
    form_section4,
    values=["yookalo2","findmaster2","h1ad2","wallclassifieds2","classifiedfactors2",],
    state="readonly", width=50
)
automation_choice4.grid(row=0, column=1, pady=10, padx=20)

ttk.Label(form_section4, text="Enter Title:").grid(row=1, column=0, sticky="w", pady=10, padx=10)
entry13 = ttk.Entry(form_section4, width=50)
entry13.grid(row=1, column=1, pady=10, padx=10)

ttk.Label(form_section4, text="Enter Description:").grid(row=2, column=0, sticky="w", pady=10, padx=10)
entry14 = ttk.Entry(form_section4, width=50)
entry14.grid(row=2, column=1, pady=10, padx=10)

ttk.Label(form_section4, text="Enter Keyword:").grid(row=3, column=0, sticky="w", pady=10, padx=10)
entry15 = ttk.Entry(form_section4, width=50)
entry15.grid(row=3, column=1, pady=10, padx=10)

ttk.Label(form_section4, text="Enter link:").grid(row=4, column=0, sticky="w", pady=10, padx=10)
entry16 = ttk.Entry(form_section4, width=50)
entry16.grid(row=4, column=1, pady=10, padx=10)


run_btn4 = ttk.Button(form_section4, text="▶ Run Tag Automation", command=run_fourth_selected)
run_btn4.grid(row=5, column=1, columnspan=2, pady=15)



# Exit Button
exit_btn = ttk.Button(main_frame, text="✖ Exit", command=root.quit)
exit_btn.pack(pady=5)
 # --- Run App ---
try:
    root.mainloop()
except Exception as e:
    print("ERROR:", e)
    traceback.print_exc()
    input("Press Enter to close...")