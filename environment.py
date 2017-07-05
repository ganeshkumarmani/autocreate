from selenium import webdriver

def before_all(context):
	#context.browser= webdriver.PhantomJS()
	context.browser = webdriver.Chrome('/Users/ganesh/Desktop/TEST/AUTOMATION/chromedriver/chromedriver')
	context.browser.implicitly_wait(2)

def after_all(context):
	context.browser.quit()	