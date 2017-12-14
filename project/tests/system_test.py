import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def main():

    driver = webdriver.Firefox()

    driver.get("http://127.0.0.1:5000")
    assert "ScheduLIT" in driver.title
    print "Home page passed."

    timeout = 30
    try:
        element_present = EC.presence_of_element_located((By.LINK_TEXT, 'Register/Login'))
        WebDriverWait(driver, timeout).until(element_present)
        driver.get("http://127.0.0.1:5000/login")
    except TimeoutException:
        print "Could not find Register/Login button."
        return

    try:
        element_present = EC.presence_of_element_located((By.ID, 'email'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print "Timed out waiting for Login page to load."
        return
    assert "Please login" in driver.page_source
    driver.find_element_by_id('email').send_keys('test@test.com')
    driver.find_element_by_id('password').send_keys('testing')
    driver.find_element_by_xpath('//button[contains(text(), \'Sign In\')]').click()
    print "Login successful."

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), \'Welcome\')]'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print "Timed out waiting for All Trips page to load"
        return
    assert "Welcome" in driver.page_source
    assert "test@test.com" in driver.page_source
    driver.find_element_by_xpath('//a[contains(text(), \'Create New Trip\')]').click()
    print("Trips page passed.")

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), \'Create New Trip\')]'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print "Timed out waiting for Create New Trip page to load"
        return
    driver.find_element_by_id('name').send_keys('Spring Break4')
    driver.find_element_by_id('location').send_keys('Cabo San Lucas')
    driver.find_element_by_id('start_date').send_keys('03/15/2018')
    driver.find_element_by_id('end_date').send_keys('03/21/2018')
    driver.find_element_by_xpath('//button[contains(text(), \'Create Trip\')]').click()
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//a[contains(text(), \'Spring Break\')]'))
        WebDriverWait(driver, timeout).until(element_present)
        print "User successfully added."
    except TimeoutException:
        print "Timed out waiting for Invited User to load"
        return
    assert "Spring Break4" in driver.page_source
    assert "Cabo San Lucas" in driver.page_source
    assert "2018-03-15" in driver.page_source
    assert "2018-03-21" in driver.page_source
    driver.find_element_by_xpath('//a[contains(text(), \'Spring Break\')]').click()
    print "Trip successfully created"

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), \'Welcome to your trip: Spring Break\')]'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print "Timed out waiting for Trip page to load"
        return 
    driver.find_element_by_id('user').send_keys('friend@friends.com')
    driver.find_element_by_xpath('//button[contains(text(), \'Invite User\')]').click()
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//a[contains(text(), \'friend@friends.com\')]'))
        WebDriverWait(driver, timeout).until(element_present)
        print "User successfully added."
    except TimeoutException:
        print "Timed out waiting for Invited User to load"
        return
    driver.find_element_by_xpath('//a[contains(text(), \'Your itinerary\')]').click()

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//h4[contains(text(), \'You have no events! Create a new event below.\')]'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print "Timed out waiting for Itinerary page to load"
        return
    driver.find_element_by_xpath('//a[contains(text(), \'Create New Event\')]').click()
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), \'Create New Event\')]'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print "Timed out waiting for Create New Event page to load"
        return
    driver.find_element_by_id('name').send_keys('Booze Cruise')
    driver.find_element_by_id('description').send_keys('Meet at the docks at 6pm!')
    driver.find_element_by_id('start_date').send_keys('03/17/2018')
    driver.find_element_by_id('start_time').send_keys('18:00')
    driver.find_element_by_id('end_date').send_keys('03/17/2018')
    driver.find_element_by_id('end_time').send_keys('22:00')
    driver.find_element_by_xpath('//button[contains(text(), \'Create Event\')]').click()

    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), \'Spring Break itnerary!\')]'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print "Timed out waiting for Invited User to load"
        return
    assert "Booze Cruise" in driver.page_source
    assert "Meet at the docks at 6pm!" in driver.page_source
    assert "2018-03-17" in driver.page_source
    assert "18:00" in driver.page_source
    print "Event successfully created." 

    print "System test passed."
    #driver.close()



main()

