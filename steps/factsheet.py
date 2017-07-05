from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import settings
import time


###############################################################################
##---GIVEN SECION---##
###############################################################################
@given(u'there is a redirection factsheet')
def step_impl(context):
	#This functions add 2 pages for redirection
	context.browser.get(settings.PARENT_FO+"lab/sondages/;view_content")
	try:
		assert(context.browser.find_element_by_link_text("redirection-factsheet-1-en"))
	except NoSuchElementException:
		context.browser.get(settings.PARENT_FO+"lab/sondages/;new_resource")
		context.browser.find_element_by_link_text("Factsheet").click()
		context.browser.find_element_by_name("title:en").clear()
		context.browser.find_element_by_name("title:en").send_keys("Redirection Factsheet 1 EN")
		context.browser.find_element_by_name("title:fr").clear()
		context.browser.find_element_by_name("title:fr").send_keys("Redirection Factsheet 1 FR")
		context.browser.find_element_by_name("action").click()
		context.browser.find_element_by_link_text("Add a box").click()
		context.browser.find_element_by_link_text("Title").click()
		context.browser.find_element_by_name("title:en").clear()
		context.browser.find_element_by_name("title:en").send_keys("EN REDIRECTION FACTSHEET PAGE 1")
		context.browser.find_element_by_name("title:fr").clear()
		context.browser.find_element_by_name("title:fr").send_keys("FR REDIRECTION FACTSHEET PAGE 1")
		context.browser.find_element_by_name("action").click()
		context.browser.find_element_by_link_text("Surveys").click()
		context.browser.find_element_by_link_text("redirection-factsheet-1-en").click()
		context.browser.find_element_by_link_text("Add a page").click()
		context.browser.find_element_by_name("title:en").clear()
		context.browser.find_element_by_name("title:en").send_keys("Page 2 EN")
		context.browser.find_element_by_name("title:fr").clear()
		context.browser.find_element_by_name("title:fr").send_keys("Page 2 FR")
		context.browser.find_element_by_name("action").click()
		context.browser.find_element_by_link_text("Add a box").click()
		context.browser.find_element_by_link_text("Title").click()
		context.browser.find_element_by_name("title:en").clear()
		context.browser.find_element_by_name("title:en").send_keys("EN REDIRECTION FACTSHEET PAGE 2")
		context.browser.find_element_by_name("title:fr").clear()
		context.browser.find_element_by_name("title:fr").send_keys("FR REDIRECTION FACTSHEET PAGE 2")
		context.browser.find_element_by_name("action").click()
		context.browser.find_element_by_link_text("Redirection Factsheet 1 EN").click()
		#Assing access right to all users
		context.browser.find_element_by_link_text("Modify access rules").click()
		context.browser.find_element_by_class_name("select2-selection__rendered").click()
		context.browser.find_element_by_class_name("select2-search__field").send_keys("All Users")
		context.browser.find_element_by_class_name("select2-search__field").send_keys(Keys.ENTER)
		context.browser.find_element_by_name("action").click()


###############################################################################
##---WHEN SECION---##
###############################################################################
@when(u'I add a one page factsheet with redirection links')
def step_impl(context):
	context.browser.find_element_by_link_text("Add Content").click()
	context.browser.find_element_by_link_text("Factsheet").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("One page Factsheet with redirection links EN")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("One page Factsheet with redirection links FR")
	context.browser.find_element_by_name("description:en").clear()
	context.browser.find_element_by_name("description:fr").clear()
	context.browser.find_element_by_name("description:fr").send_keys(u"FR Je veux d'l'amour, d'la joie, de la bonne humeur Ce n'est pas votre argent qui f'ra mon bonheur Moi j'veux crever la main sur le coeur, papalapapapala Allons ensemble, découvrir ma liberté Oubliez donc tous vos clichés, bienvenue dans ma réalité")
	context.browser.find_element_by_name("description:en").send_keys(u"EN I want love, joy, good humor It's not your money that will make my happiness I want to put a hand on my heart, papalapapapala Let's go together, discover my freedom So forget all your clichés, welcome to my reality")
	context.browser.find_element_by_name("action").click()
	#Adding a Title BOX
	context.browser.find_element_by_link_text("Add a box").click()
	context.browser.find_element_by_link_text("Title").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("EN BOX with redirection links")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("FR BOX with redirection links")
	#Colour of the box and title
	context.browser.find_element_by_xpath("//*[contains(text(),'Background color')]/../div/div[2]").click()
	context.browser.find_elements_by_class_name("sp-input")[0].clear()
	context.browser.find_elements_by_class_name("sp-input")[0].send_keys("#e23636")
	context.browser.find_element_by_xpath("//*[contains(text(),'Text color')]/../div/div[2]").click()
	context.browser.find_elements_by_class_name("sp-input")[1].clear()
	context.browser.find_elements_by_class_name("sp-input")[1].send_keys("#ffffff")
	#Box alignment to center
	select = Select(context.browser.find_element_by_id("box-alignment"))
	select.select_by_value("text-center")
	#Save
	context.browser.find_element_by_name("action").click()
	#Adding the links using the text box
	context.browser.find_element_by_link_text("Add a box").click()
	context.browser.find_element_by_link_text("Text").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("EN REDIRECTION TEXT")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("FR REDIRECTION TEXT")
	#Display the title of the Text
	context.browser.find_element_by_id("display-title-1").click()
	#Content in English
	context.browser.find_element_by_name("data_txt:en").clear()
	context.browser.find_element_by_name("data_txt:en").send_keys("EN. The following are the links to get redirected to either internal or external links")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys("EXTERNAL LINKS")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys(".")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys("To get redirected to bepatient site click [here](https://www.bepatient.com/)")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys(".")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys("To get redirected to open a PDF document click [here](http://www.euro.who.int/__data/assets/pdf_file/0012/302331/From-Innovation-to-Implementation-eHealth-Report-EU.pdf/)")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys(".")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys("To get redirected to see BePATIENT Logo click [here](https://pbs.twimg.com/profile_images/786842116932657152/4dM8fFMB.jpg/)")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys(".")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys("To get redirected to bepatient youtube video click [here](https://www.youtube.com/watch?v=TSCugj_jDgU/)")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys(".")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys(".")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys(".")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys("INTERNAL LINKS")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys(".")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys("To get redirected to survey category site click [here](/lab/sondages/)")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys(".")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys("To get redirected to a factsheet click [here](/lab/sondages/redirection-factsheet-1-en/)")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys(".")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys("To get redirected to the 2nd page of a factsheet click [here](/lab/sondages/redirection-factsheet-1-en/page-2-en/)")
	context.browser.find_element_by_name("data_txt:en").send_keys("\n")
	context.browser.find_element_by_name("data_txt:en").send_keys(".")
	#Content in FRENCH
	context.browser.find_element_by_name("data_txt:fr").clear()
	context.browser.find_element_by_name("data_txt:fr").send_keys("FR. The following are the links to get redirected to either internal or external links")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys("EXTERNAL LINKS")
	context.browser.find_element_by_name("data_txt:fr").send_keys(".")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys("To get redirected to bepatient site click [here](https://www.bepatient.com/)")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys(".")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys("To get redirected to open a PDF document click [here](http://www.euro.who.int/__data/assets/pdf_file/0012/302331/From-Innovation-to-Implementation-eHealth-Report-EU.pdf/)")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys(".")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys("To get redirected to see BePATIENT Logo click [here](https://pbs.twimg.com/profile_images/786842116932657152/4dM8fFMB.jpg/)")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys(".")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys("To get redirected to bepatient youtube video click [here](https://www.youtube.com/watch?v=TSCugj_jDgU/)")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys(".")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys(".")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys(".")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys("INTERNAL LINKS")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys(".")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys("To get redirected to survey category site click [here](/lab/sondages/)")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys(".")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys("To get redirected to a factsheet click [here](/lab/sondages/redirection-factsheet-1-en/)")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys(".")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys("To get redirected to the 2nd page of a factsheet click [here](/lab/sondages/redirection-factsheet-1-en/page-2-en/)")
	context.browser.find_element_by_name("data_txt:fr").send_keys("\n")
	context.browser.find_element_by_name("data_txt:fr").send_keys(".")
	context.browser.find_element_by_name("action").click()


@when(u'I add a factsheet with 4 pages and different types of boxes')
def step_impl(context):
	context.browser.find_element_by_link_text("Add Content").click()
	context.browser.find_element_by_link_text("Factsheet").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("Factsheet with 4 pages and different types of boxes EN")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("Factsheet with 4 pages and different types of boxes FR")
	context.browser.find_element_by_name("description:en").clear()
	context.browser.find_element_by_name("description:fr").clear()
	context.browser.find_element_by_name("description:fr").send_keys(u"FR Je veux d'l'amour, d'la joie, de la bonne humeur Ce n'est pas votre argent qui f'ra mon bonheur Moi j'veux crever la main sur le coeur, papalapapapala Allons ensemble, découvrir ma liberté Oubliez donc tous vos clichés, bienvenue dans ma réalité")
	context.browser.find_element_by_name("description:en").send_keys(u"EN I want love, joy, good humor It's not your money that will make my happiness I want to put a hand on my heart, papalapapapala Let's go together, discover my freedom So forget all your clichés, welcome to my reality")
	context.browser.find_element_by_name("action").click()
	context.execute_steps(u"""
		when I add a title to the page
		when I add a Text to the page
		when I add a Image box to the page
		when I add a Youtube video to the page
		when I add a Vimeo video to the page
		when I add a Icon to the page
		""")
	context.browser.find_element_by_link_text("CATEGORY FOR FACTSHEET").click()
	context.browser.find_element_by_link_text("factsheet-with-4-pages-and-different-types-of-boxes-en").click()
	context.browser.find_element_by_link_text("Add a page").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("Page 2 EN")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("Page 2 FR")
	context.browser.find_element_by_name("action").click()
	context.execute_steps(u"""
		when I add a contact box
		""")

	context.browser.find_element_by_link_text("CATEGORY FOR FACTSHEET").click()
	context.browser.find_element_by_link_text("factsheet-with-4-pages-and-different-types-of-boxes-en").click()
	context.browser.find_element_by_link_text("Add a page").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("Page 3 EN")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("Page 3 FR")
	context.browser.find_element_by_name("action").click()
	context.execute_steps(u"""
		when I add a carousel to the page
		""")
	context.browser.find_element_by_link_text("CATEGORY FOR FACTSHEET").click()
	context.browser.find_element_by_link_text("factsheet-with-4-pages-and-different-types-of-boxes-en").click()
	context.browser.find_element_by_link_text("Add a page").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("Page 4 EN")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("Page 4 FR")
	context.browser.find_element_by_name("action").click()
	context.execute_steps(u"""
		when I add a Navigation button to the page
		when I add a Author section to the page
		""")


###############################################################################
##---THEN SECION---##
###############################################################################