from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def eulerPhi(n):
	path = "C:\Program Files (x86)\chromedriver.exe"
	driver = webdriver.Chrome(path)

	driver.get('https://www.alpertron.com.ar/ECM.HTM?fbclid=IwAR0RF-VhPs1UZAYyFvMYQ5IDui-FrjQoNzPP190H_QwzpEvIJmU9lzMI5cs')

	factor = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "factor")))
	box = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "value")))
	box.send_keys(n)
	box.send_keys(Keys.RETURN)
	factor.click()
	time.sleep(10)
	div = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "result")))
	lists = div.find_elements(By.TAG_NAME, 'p')

	t = "Euler's totient: "	
	ret = "-1"
	for p in lists:
		if (p.text[:len(t)] == t):
			ret = p.text[len(t):]
			break
	
	res = ""
	for c in ret:
		if (c == '('):
			break
		if (c != ' '):
			res += c

	return int(res)
	