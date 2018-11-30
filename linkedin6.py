from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome() #I actually used the chromedriver and did not test firefox, but it should work.
profile_link="https://www.linkedin.com/company/the-center-of-applied-data-science/"
driver.get(profile_link)
html=driver.page_source
soup=BeautifulSoup(html) #specify parser or it will auto-select for you
summary=soup.find('section', { "id" : "summary" })
print (summary.getText())
