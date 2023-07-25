from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os # to get the resume file
from selenium.webdriver.chrome.service import Service
import time # to sleep
from selenium.webdriver.common.by import By

URL = 'https://boards.greenhouse.io/gleanwork/jobs/4006898005'

# Fill in this dictionary with your personal details!
JOB_APP = {
    "first_name": "Hari Prasad",
    "last_name": "Renganathan",
    "email": "hr2514@columbia.edu",
    "phone": "917-238-4627",
    # "org": "Self-Employed",
    # "resume": "resume.pdf",
    "resume_textfile": "resume_short.txt",
    "linkedin": "https://www.linkedin.com/",
    # "website": "www.youtube.com",
    # "github": "https://github.com",
    # "twitter": "www.twitter.com",
    # "location": "San Francisco, California, United States",
    # "grad_month": '06',
    # "grad_year": '2021',
    # "university": "MIT" # if only o.O
}

# Greenhouse has a different application form structure than Lever, and thus must be parsed differently
def greenhouse(driver):

    # basic info
    print('Started')
    driver.find_element('id','first_name').send_keys(JOB_APP['first_name'])
    driver.find_element('id','last_name').send_keys(JOB_APP['last_name'])
    driver.find_element('id','email').send_keys(JOB_APP['email'])
    driver.find_element(By.ID,'phone').send_keys(JOB_APP['phone'])

    # # This doesn't exactly work, so a pause was added for the user to complete the action
    # try:
    #     loc = driver.find_element_by_id('job_application_location')
    #     loc.send_keys(JOB_APP['location'])
    #     loc.send_keys(Keys.DOWN) # manipulate a dropdown menu
    #     loc.send_keys(Keys.DOWN)
    #     loc.send_keys(Keys.RETURN)
    #     time.sleep(2) # give user time to manually input if this fails

    # except NoSuchElementException:
    #     pass

    # Upload Resume as a Text File
    # driver.find_element(By.CLASS_NAME, "unstyled-button link-button").click()
    driver.find_element(By.XPATH, "//*[contains(text(), 'or enter manually')]").click()
    # driver.find_element(By.XPATH, '//button[@class="unstyled-button link-button"]').send_keys('Hari Prasad Resume.pdf')
    resume_zone = driver.find_element('id','resume_text')
    with open(JOB_APP['resume_textfile']) as f:
        lines = f.readlines() # add each line of resume to the text area
        for line in lines:
            resume_zone.send_keys(line)

    # add linkedin
    try:
        driver.find_element(By.XPATH, "//label[contains(.,'LinkedIn')]").send_keys(JOB_APP['linkedin'])

    except NoSuchElementException:
        pass
    
    # add linkedin
    try:
        driver.find_element(By.XPATH, "//label[contains(.,'Do you know anyone')]").send_keys('No')
    except NoSuchElementException:
        pass

    # add linkedin
    try:
        driver.find_element(By.XPATH, "//label[contains(.,'Why are you interested')]").send_keys('I am interested')
    except NoSuchElementException:
        pass

    # # add graduation year
    # try:
    #     driver.find_element_by_xpath("//select/option[text()='2021']").click()
    # except NoSuchElementException:
    #     pass

    # # add university
    # try:
    #     driver.find_element_by_xpath("//select/option[contains(.,'Harvard')]").click()
    # except NoSuchElementException:
    #     pass

    # # add degree
    # try:
    #     driver.find_element_by_xpath("//select/option[contains(.,'Bachelor')]").click()
    # except NoSuchElementException:
    #     pass

    # # add major
    # try:
    #     driver.find_element_by_xpath("//select/option[contains(.,'Computer Science')]").click()
    # except NoSuchElementException:
    #     pass

    # # add website
    # try:
    #     driver.find_element_by_xpath("//label[contains(.,'Website')]").send_keys(JOB_APP['website'])
    # except NoSuchElementException:
    #     pass

    # # add work authorization
    # try:
    #     driver.find_element_by_xpath("//select/option[contains(.,'any employer')]").click()
    # except NoSuchElementException:
    #     pass

    driver.find_element("id","submit_app").click()

if __name__ == '__main__':

    # call get_links to automatically scrape job listings from glassdoor
    # aggregatedURLs = get_links.getURLs()
    # print(f'Job Listings: {aggregatedURLs}')
    # print('\n')

    service = Service("chromedriver")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    # driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    print('\n')
    url = URL

    if 'greenhouse' in url:
        driver.get(url)
        # try:
        greenhouse(driver)
        print(f'SUCCESS FOR: {url}')
        # except Exception:
        #     print(f"FAILED FOR {url}")
            

    # elif 'lever' in url:
    #     driver.get(url)
    #     try:
    #         lever(driver)
    #         print(f'SUCCESS FOR: {url}')
    #     except Exception:
    #         # print(f"FAILED FOR {url}")
    #         continue
    # i dont think this else is needed
    # else:
    #     # print(f"NOT A VALID APP LINK FOR {url}")
    #     continue

    time.sleep(10) # can lengthen this as necessary (for captcha, for example)

    driver.close()
