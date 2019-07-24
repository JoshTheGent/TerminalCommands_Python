from selenium import webdriver 
import sys

query = sys.argv
n = len(query)
print(query)
search = "https://www.google.com"
if(n > 1):
    search = "https://www.google.com/search?q=" + query[1]
    i = 2
    for x in range(n-2):
        search += " " + query[i]
        i += 1


driver = webdriver.Chrome()
driver.get(search)

quit()