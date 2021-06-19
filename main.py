from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.keys import Keys
from pprint import pprint
import os
from selenium.common.exceptions import NoSuchElementException
import time
LINKEDIN_DUMMY_USER = os.environ["EMAIL"]
LINKEDIN_DUMMY_PASS = os.environ["EMAIL_PASSWORD"]
JOB_TYPE = "programmer"
LINKEDIN_JOB = "https://www.linkedin.com/jobs/search/?keywords=" + JOB_TYPE
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
#The purpose of this program is to apply to the easy apply jobs in linkedin with a submit button as soon as the job is clicked on


#Find and go to the LinkedIn sign in page
driver.get(LINKEDIN_JOB)
sign_in_link = driver.find_element_by_xpath('/html/body/div[3]/a[1]').get_attribute('href')
driver.get(sign_in_link)

#Find and enter the email in the username text field
username = driver.find_element_by_id('username')
username.send_keys(LINKEDIN_DUMMY_USER)

#Find and enter the password in the password field
password = driver.find_element_by_id('password')
password.send_keys(LINKEDIN_DUMMY_PASS)

#Find and click the sign in button
sign_in_button = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()

#Get a list of the current jobs listed by linkedin
job_list = driver.find_elements_by_class_name("job-card-container")
#Loop through the list of current jobs
for i in job_list:
    #Click to the specific job posting and give it some time to load
    i.click()
    time.sleep(1)
    #Try to see if there is an apply button for the job, if there is no apply button
    #it means this job was previously applied to
    try:
        #Find and click the apply button
        apply_button = driver.find_element_by_class_name("jobs-apply-button")
        apply_button.click()
        #Check for the instant submit application button, if no submit button we exit out of the application
        submit_button = driver.find_elements_by_class_name('artdeco-button--2')
        for i in submit_button:
            if i.text == "Submit application":
                i.click()
        #Give the page some time to load
        time.sleep(3)
        #Find the exit button and click it
        exit_button = driver.find_element_by_class_name("mercado-match")
        exit_button.click()
        #Find the discard option and click it if we exited out of an application without applying.
        #LinkedIn forces the user to hit discard
        discard_list = driver.find_elements_by_class_name('artdeco-button__text')
        for i in discard_list:
            if i.text == "Discard":
                i.click()
    except NoSuchElementException:
        pass
    #Wait for the page to load then go to the next job
    time.sleep(5)