from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import settings
import time

###############################################################################
##---GIVEN SECION---##
###############################################################################
@given(u'I am in the parent category "{category_title}"')
def step_impl(context,category_title):
	context.browser.get(settings.PARENT_FO+"lab/;view_content")
	destination = category_title.replace(' ', '-').lower()
	context.browser.find_element_by_link_text(destination).click()


###############################################################################
##---WHEN SECION---##
###############################################################################
@when(u'I add the parent category for "{category_title}"')
def step_impl(context,category_title):
	#Go to the lab section
	context.browser.get(settings.PARENT_FO+"lab/;view_content")
	try:
		assert(context.browser.find_element_by_link_text(category_title))
	except NoSuchElementException:
		#Add the parent category
		context.browser.find_element_by_link_text("Add Content").click()
		context.browser.find_element_by_link_text("Category").click()
		#Add the category details in the edit page
		context.browser.find_element_by_name("title:en").clear()
		context.browser.find_element_by_name("title:en").send_keys(category_title)
		#Save the category
		context.browser.find_element_by_name("action").click()
		#Assing access right to all users
		context.browser.find_element_by_link_text("Modify access rules").click()
		context.browser.find_element_by_class_name("select2-selection__rendered").click()
		context.browser.find_element_by_class_name("select2-search__field").send_keys("All Users")
		context.browser.find_element_by_class_name("select2-search__field").send_keys(Keys.ENTER)
		context.browser.find_element_by_name("action").click()


###############################################################################
##---THEN SECION---##
###############################################################################
@then(u'I add a link for "{category_title}" in the menu')
def step_impl(context,category_title):
	context.browser.get(settings.PARENT_FO+";list_websites")
	context.browser.find_element_by_xpath("//*[@id='form-table']/table/tbody/tr/td[2]/a").click()
	context.browser.find_element_by_link_text("Configuring").click()
	context.browser.find_element_by_link_text("List of sections").click()
	context.browser.find_element_by_link_text("Survey").click()
	context.browser.find_element_by_link_text("List of sections").click()
	try:
		assert(context.browser.find_element_by_link_text(category_title))
	except NoSuchElementException:
		context.browser.find_element_by_link_text("Add a resource").click()
		context.browser.find_element_by_name("title:en").clear()
		context.browser.find_element_by_name("title:en").send_keys(category_title)
		context.browser.find_element_by_class_name("select2-selection--single").click()
		context.browser.find_element_by_class_name("select2-search__field").send_keys(category_title)
		context.browser.find_element_by_class_name("select2-search__field").send_keys(Keys.ENTER)
		context.browser.find_element_by_name("action").click()





