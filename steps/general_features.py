from behave import *
from selenium.webdriver.common.by import By
import settings

###############################################################################
##---GIVEN SECION---##
###############################################################################
@given(u'I login to the site as administrator')
def step_impl(context):
	#Go to the back office page
	context.browser.get(settings.PARENT_BO)
	#Login using the admin user credentials from the settings page
	context.username = settings.ADMIN_USER_NAME
	context.password = settings.ADMIN_PASSWORD
	context.browser.find_element_by_name('loginname').send_keys(context.username)
	context.browser.find_element_by_name('password').send_keys(context.password)
	context.browser.find_element_by_name('action').click()
	context.browser.implicitly_wait(10)
"""	
###############################################################################
##---WHEN SECION---##
###############################################################################
@when(u'bla bla bla bla bla')
def step_impl(context):
	pass
###############################################################################
##---THEN SECION---##
###############################################################################
@then(u'bla bla bla bla bla')
def step_impl(context):
	pass
"""