from behave import *
from selenium.webdriver.common.by import By
import settings
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

import time

###############################################################################
##---GIVEN SECION---##
###############################################################################
@given(u'I add all images for the test')
def step_impl(context):
	carousel_images =[
	["CarouselImage1","carousel_image_1.png"],
	["CarouselImage2","carousel_image_2.jpg"],
	["CarouselImage3","carousel_image_3.jpg"],
	["CarouselImage4","carousel_gif_1.gif"],
	["FactsheetImage1","factsheet_image_1.jpg"]
	]
	for image in carousel_images:
		context.browser.get(settings.PARENT_FO+"images/;view")
		context.browser.find_element_by_name("q").clear()
		context.browser.find_element_by_name("q").send_keys(image[0])
		context.browser.find_element_by_class_name("btn-primary").click()
		try:
			assert(context.browser.find_element_by_link_text(image[0]))
		except NoSuchElementException:
			context.browser.find_element_by_link_text("Add an image").click()
			context.browser.find_element_by_name("title:en").clear()
			context.browser.find_element_by_name("title:en").send_keys(image[0])
			context.browser.find_element_by_name("multilingual_data:en").click()
			time.sleep(2)
			context.browser.find_element_by_css_selector('input[type="file"]').clear()
			context.browser.find_element_by_css_selector('input[type="file"]').send_keys("/Users/ganesh/Desktop/TEST/autocreate/TEST_IMAGES"+image[1])
			context.browser.find_element_by_name("action").click()
			time.sleep(5)


@when('I add a Image box to the page')
def step_impl(context):
	#ADD IMAGE
	context.browser.find_element_by_link_text("Add a box").click()
	context.browser.find_element_by_link_text("Image").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("IMAGE BOX TITLE EN")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("IMAGE BOX TITLE FR")
	#Display the title of the Image+
	context.browser.find_element_by_id("display-title-1").click()
	#Selecting the Image
	context.browser.find_element_by_link_text("Select Image").click()
	iframe = context.browser.find_elements_by_xpath("/html/body/div[5]/div[2]/iframe")[0]
	context.browser.switch_to_frame(iframe)
	context.browser.find_element_by_id("q").clear()
	context.browser.find_element_by_id("q").send_keys("FactsheetImage1")
	context.browser.find_element_by_class_name("btn-primary").click()
	context.browser.find_element_by_class_name("img-responsive").click()
	context.browser.switch_to_default_content()

	#Adapt the Size of the Image to the box
	context.browser.find_element_by_id("adapt-image-size-1").click()
	#Border
	context.browser.find_element_by_id("box-border-1").click()
	#SAVE
	context.browser.find_element_by_name("action").click()
	pass


@when('I add a Score box to the page with "{score_title}"')
def step_impl(context, score_title):
	#ADD Score Box
	context.browser.find_element_by_link_text("Add a box").click()
	context.browser.find_element_by_link_text("Scoring result").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("SCORE BOX TITLE EN")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("SCORE BOX TITLE FR")
	#Display the title of the Image
	context.browser.find_element_by_id("display-title-1").click()
	#Border
	context.browser.find_element_by_id("box-border-1").click()
	#Select Score
	select = Select(context.browser.find_element_by_id("scoring-form"))
	select.select_by_value("SCORE FOR FORM EN")
	#SAVE
	context.browser.find_element_by_name("action").click()

@then(u'I can see the Image box in the list of boxes of the page')
def step_impl(context):
	Image_link = context.browser.find_element_by_link_text("IMAGE BOX TITLE EN")
	assert(Image_link)


@when('I add a Vimeo video to the page')
def step_impl(context):
	#ADD vimeo video
	context.browser.find_element_by_link_text("Add a box").click()
	context.browser.find_element_by_link_text("Youtube / Vimeo video").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("Vimeo Video EN")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("Vimeo Video FR")
	#Display the title of the Video
	context.browser.find_element_by_id("display-title-1").click()
	#Box alignment to center
	select = Select(context.browser.find_element_by_id("box-alignment"))
	select.select_by_value("text-center")
	#Width Half
	select = Select(context.browser.find_element_by_id("box-columns"))
	select.select_by_value("6")
	#Border
	context.browser.find_element_by_id("box-border-1").click()
	context.browser.find_element_by_name("video_id:en").clear()
	context.browser.find_element_by_name("video_id:en").send_keys("https://vimeo.com/123000558")
	context.browser.find_element_by_name("video_id:fr").clear()
	context.browser.find_element_by_name("video_id:fr").send_keys("https://vimeo.com/13359364")
	context.browser.find_element_by_name("action").click()

@then(u'I can see the Vimeo video box in the list of boxes of the page')
def step_impl(context):
	Image_link = context.browser.find_element_by_link_text("Vimeo Video EN")
	assert(Image_link)


@when('I add a Youtube video to the page')
def step_impl(context):
	#Add youtube video
	context.browser.find_element_by_link_text("Add a box").click()
	context.browser.find_element_by_link_text("Youtube / Vimeo video").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("YouTubeVideo EN")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("YouTubeVideo FR")
	#Display the title of the Video
	context.browser.find_element_by_id("display-title-1").click()
	#Box alignment to center
	select = Select(context.browser.find_element_by_id("box-alignment"))
	select.select_by_value("text-center")
	#Width Half
	select = Select(context.browser.find_element_by_id("box-columns"))
	select.select_by_value("6")
	#Border
	context.browser.find_element_by_id("box-border-1").click()
	context.browser.find_element_by_name("video_id:en").clear()
	context.browser.find_element_by_name("video_id:en").send_keys("https://www.youtube.com/watch?v=YqeW9_5kURI")
	context.browser.find_element_by_name("video_id:fr").clear()
	context.browser.find_element_by_name("video_id:fr").send_keys("https://www.youtube.com/watch?v=Tm88QAI8I5A")
	context.browser.find_element_by_name("action").click()


@then(u'I can see the Youtube video box in the list of boxes of the page')
def step_impl(context):
	Image_link = context.browser.find_element_by_link_text("YouTubeVideo EN")
	assert(Image_link)


@when('I add a title to the page')
def step_impl(context):
	#Adding a Title BOX and Subtitle in both the language
	context.browser.find_element_by_link_text("Add a box").click()
	context.browser.find_element_by_link_text("Title").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("EN BOX GRAND Title")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("FR BOX GRAND Title")
	context.browser.find_element_by_name("previous_title:en").clear()
	context.browser.find_element_by_name("previous_title:en").send_keys("EN Subtitle for the BOX")
	context.browser.find_element_by_name("previous_title:fr").clear()
	context.browser.find_element_by_name("previous_title:fr").send_keys("FR Subtitle for the BOX")
	#Underline the title
	context.browser.find_element_by_id("is-title-underlined-1").click()
	#Border
	context.browser.find_element_by_id("box-border-1").click()
	#Box alignment to center
	select = Select(context.browser.find_element_by_id("box-alignment"))
	select.select_by_value("text-center")
	#Colour of the box and title
	context.browser.find_element_by_xpath("//*[contains(text(),'Background color')]/../div/div[2]").click()
	context.browser.find_elements_by_class_name("sp-input")[0].clear()
	context.browser.find_elements_by_class_name("sp-input")[0].send_keys("#000000")
	context.browser.find_element_by_xpath("//*[contains(text(),'Text color')]/../div/div[2]").click()
	context.browser.find_elements_by_class_name("sp-input")[1].clear()
	context.browser.find_elements_by_class_name("sp-input")[1].send_keys("#ffffff")
	#Save
	context.browser.find_element_by_name("action").click()


@then(u'I can see the Title box in the list of boxes of the page')
def step_impl(context):
	title_link = context.browser.find_element_by_link_text("EN BOX GRAND Title")
	assert(title_link)


@when('I add a Text to the page')
def step_impl(context):
	#Add Text
	context.browser.find_element_by_link_text("Add a box").click()
	context.browser.find_element_by_link_text("Text").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("EN TEXT Title")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("FR TEXT Title")
	#Display the title of the Text
	context.browser.find_element_by_id("display-title-1").click()
	#Content in English
	context.browser.find_element_by_name("data_txt:en").clear()
	context.browser.find_element_by_name("data_txt:en").send_keys(u"EN I want love, joy, good humor It's not your money that will make my happiness I want to put a hand on my heart, papalapapapala Let's go together, discover my freedom So forget all your clichés, welcome to my reality")
	context.browser.find_element_by_name("data_txt:en").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:en").send_keys("# My first level heading")
	context.browser.find_element_by_name("data_txt:en").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:en").send_keys("## My second level heading")
	context.browser.find_element_by_name("data_txt:en").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:en").send_keys("### My first third heading")
	context.browser.find_element_by_name("data_txt:en").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:en").send_keys("** Bold text **")
	context.browser.find_element_by_name("data_txt:en").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:en").send_keys("_Italics_")
	context.browser.find_element_by_name("data_txt:en").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:en").send_keys("[Mon lien](http://www.google.fr)")
	context.browser.find_element_by_name("data_txt:en").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:en").send_keys("* Apples")
	context.browser.find_element_by_name("data_txt:en").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:en").send_keys("* Pears")
	context.browser.find_element_by_name("data_txt:en").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:en").send_keys("I put a line break here.<espace><espace>")
	context.browser.find_element_by_name("data_txt:en").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:en").send_keys("> _The causes of hypertension are multiple._")
	context.browser.find_element_by_name("data_txt:en").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:en").send_keys("> _We discover how to prevent them and keep a heart")
	context.browser.find_element_by_name("data_txt:en").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:en").send_keys("healthy._")
	context.browser.find_element_by_name("data_txt:en").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:en").send_keys("> **-Dr Jean Paul**")
	#Content in French
	context.browser.find_element_by_name("data_txt:fr").clear()
	context.browser.find_element_by_name("data_txt:fr").send_keys(u"FR Je veux d'l'amour, d'la joie, de la bonne humeur Ce n'est pas votre argent qui f'ra mon bonheur Moi j'veux crever la main sur le coeur, papalapapapala Allons ensemble, découvrir ma liberté Oubliez donc tous vos clichés, bienvenue dans ma réalité")
	context.browser.find_element_by_name("data_txt:fr").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:fr").send_keys("# My first level heading")
	context.browser.find_element_by_name("data_txt:fr").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:fr").send_keys("## My second level heading")
	context.browser.find_element_by_name("data_txt:fr").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:fr").send_keys("### My first third heading")
	context.browser.find_element_by_name("data_txt:fr").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:fr").send_keys("** Bold text **")
	context.browser.find_element_by_name("data_txt:fr").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:fr").send_keys("_Italics_")
	context.browser.find_element_by_name("data_txt:fr").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:fr").send_keys("[Mon lien](http://www.google.fr)")
	context.browser.find_element_by_name("data_txt:fr").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:fr").send_keys("* Apples")
	context.browser.find_element_by_name("data_txt:fr").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:fr").send_keys("* Pears")
	context.browser.find_element_by_name("data_txt:fr").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:fr").send_keys("I put a line break here.<espace><espace>")
	context.browser.find_element_by_name("data_txt:fr").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:fr").send_keys("> _The causes of hypertension are multiple._")
	context.browser.find_element_by_name("data_txt:fr").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:fr").send_keys("> _We discover how to prevent them and keep a heart")
	context.browser.find_element_by_name("data_txt:fr").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:fr").send_keys("healthy._")
	context.browser.find_element_by_name("data_txt:fr").send_keys(Keys.RETURN)
	context.browser.find_element_by_name("data_txt:fr").send_keys("> **-Dr Jean Paul**")
	#Border
	context.browser.find_element_by_id("box-border-1").click()
	#Colour of the box and title
	context.browser.find_element_by_xpath("//*[contains(text(),'Background color')]/../div/div[2]").click()
	context.browser.find_elements_by_class_name("sp-input")[0].clear()
	context.browser.find_elements_by_class_name("sp-input")[0].send_keys("#000000")
	context.browser.find_element_by_xpath("//*[contains(text(),'Text color')]/../div/div[2]").click()
	context.browser.find_elements_by_class_name("sp-input")[1].clear()
	context.browser.find_elements_by_class_name("sp-input")[1].send_keys("#ffffff")

	#SAVE
	context.browser.find_element_by_name("action").click()
	pass

@then(u'I can see the Text Box in the list of boxes of the page')
def step_impl(context):
	Image_link = context.browser.find_element_by_link_text("EN TEXT Title")
	assert(Image_link)


@when('I add a Icon to the page')
def step_impl(context):
	#We are going to add 3 icons with 1/3 Size
	#First Icon
	context.browser.find_element_by_link_text("Add a box").click()
	context.browser.find_element_by_link_text("Icon").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("Icon Heart EN")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("Icon Heart FR")
	context.browser.find_element_by_name("fontawesome_icon").clear()
	context.browser.find_element_by_name("fontawesome_icon").send_keys("fa-heart")
	context.browser.find_element_by_name("data_txt:en").clear()
	context.browser.find_element_by_name("data_txt:en").send_keys("EN I want love, joy, good humor")
	context.browser.find_element_by_name("data_txt:fr").clear()
	context.browser.find_element_by_name("data_txt:fr").send_keys("FR Je veux d'l'amour, d'la joie, de la bonne humeur")
	#Display the title of the icon
	context.browser.find_element_by_id("display-title-1").click()
	#Box alignment to center
	select = Select(context.browser.find_element_by_id("box-alignment"))
	select.select_by_value("text-center")
	#Width Half
	select = Select(context.browser.find_element_by_id("box-columns"))
	select.select_by_value("4")
	#Colour of the box and title
	context.browser.find_element_by_xpath("//*[contains(text(),'Background color')]/../div/div[2]").click()
	context.browser.find_elements_by_class_name("sp-input")[0].clear()
	context.browser.find_elements_by_class_name("sp-input")[0].send_keys("#0000FF")
	context.browser.find_element_by_xpath("//*[contains(text(),'Text color')]/../div/div[2]").click()
	context.browser.find_elements_by_class_name("sp-input")[1].clear()
	context.browser.find_elements_by_class_name("sp-input")[1].send_keys("#ffffff")
	context.browser.find_element_by_name("action").click()
	#Second Icon
	context.browser.find_element_by_link_text("Add a box").click()
	context.browser.find_element_by_link_text("Icon").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("Icon AREA CHART EN")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("Icon AREA CHART FR")
	context.browser.find_element_by_name("fontawesome_icon").clear()
	context.browser.find_element_by_name("fontawesome_icon").send_keys("fa-area-chart")
	context.browser.find_element_by_name("data_txt:en").clear()
	context.browser.find_element_by_name("data_txt:en").send_keys("EN I want love, joy, good humor")
	context.browser.find_element_by_name("data_txt:fr").clear()
	context.browser.find_element_by_name("data_txt:fr").send_keys("FR Je veux d'l'amour, d'la joie, de la bonne humeur")
	#Display the title of the icon
	context.browser.find_element_by_id("display-title-1").click()
	#Box alignment to center
	select = Select(context.browser.find_element_by_id("box-alignment"))
	select.select_by_value("text-center")
	#Width Half
	select = Select(context.browser.find_element_by_id("box-columns"))
	select.select_by_value("4")
	#Colour of the box and title
	context.browser.find_element_by_xpath("//*[contains(text(),'Background color')]/../div/div[2]").click()
	context.browser.find_elements_by_class_name("sp-input")[0].clear()
	context.browser.find_elements_by_class_name("sp-input")[0].send_keys("#000000")
	context.browser.find_element_by_xpath("//*[contains(text(),'Text color')]/../div/div[2]").click()
	context.browser.find_elements_by_class_name("sp-input")[1].clear()
	context.browser.find_elements_by_class_name("sp-input")[1].send_keys("#ffffff")
	context.browser.find_element_by_name("action").click()

	#Third Icon
	context.browser.find_element_by_link_text("Add a box").click()
	context.browser.find_element_by_link_text("Icon").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("Icon University EN")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("Icon University FR")
	context.browser.find_element_by_name("fontawesome_icon").clear()
	context.browser.find_element_by_name("fontawesome_icon").send_keys("fa-university")
	context.browser.find_element_by_name("data_txt:en").clear()
	context.browser.find_element_by_name("data_txt:en").send_keys("EN I want love, joy, good humor")
	context.browser.find_element_by_name("data_txt:fr").clear()
	context.browser.find_element_by_name("data_txt:fr").send_keys("FR Je veux d'l'amour, d'la joie, de la bonne humeur")
	#Display the title of the icon
	context.browser.find_element_by_id("display-title-1").click()
	#Box alignment to center
	select = Select(context.browser.find_element_by_id("box-alignment"))
	select.select_by_value("text-center")
	#Width Half
	select = Select(context.browser.find_element_by_id("box-columns"))
	select.select_by_value("4")
	#Colour of the box and title
	context.browser.find_element_by_xpath("//*[contains(text(),'Background color')]/../div/div[2]").click()
	context.browser.find_elements_by_class_name("sp-input")[0].clear()
	context.browser.find_elements_by_class_name("sp-input")[0].send_keys("#FF0000")
	context.browser.find_element_by_xpath("//*[contains(text(),'Text color')]/../div/div[2]").click()
	context.browser.find_elements_by_class_name("sp-input")[1].clear()
	context.browser.find_elements_by_class_name("sp-input")[1].send_keys("#ffffff")
	context.browser.find_element_by_name("action").click()
	pass

@then(u'I can see the Icon Box in the list of boxes of the page')
def step_impl(context):
	Image_link = context.browser.find_element_by_link_text("Icon Heart EN")
	assert(Image_link)


@when('I add a Navigation button to the page')
def step_impl(context):
	context.browser.find_element_by_link_text("Add a box").click()
	context.browser.find_element_by_link_text("Navigation button box").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("Navigation button EN")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("Navigation button FR")
	context.browser.find_element_by_name("action").click()
	

@then(u'I can see the Navigation button Box in the list of boxes of the page')
def step_impl(context):
	Image_link = context.browser.find_element_by_link_text("Navigation button EN")
	assert(Image_link)


@when('I add a Author section to the page')
def step_impl(context):
	#Add Author
	context.browser.find_element_by_link_text("Add a box").click()
	context.browser.find_element_by_link_text("Author").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("Author Section EN")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("Author Section FR")
	#Colour of the box and title
	context.browser.find_element_by_xpath("//*[contains(text(),'Background color')]/../div/div[2]").click()
	context.browser.find_elements_by_class_name("sp-input")[0].clear()
	context.browser.find_elements_by_class_name("sp-input")[0].send_keys("#000000")
	context.browser.find_element_by_xpath("//*[contains(text(),'Text color')]/../div/div[2]").click()
	context.browser.find_elements_by_class_name("sp-input")[1].clear()
	context.browser.find_elements_by_class_name("sp-input")[1].send_keys("#ffffff")
	context.browser.find_element_by_name("action").click()
	

@when('I add a contact box')
def step_impl(context):
	#Contact Box
	context.browser.find_element_by_link_text("Add a box").click()
	context.browser.find_element_by_link_text("Contact form").click()
	context.browser.find_element_by_name("title:en").clear()
	context.browser.find_element_by_name("title:en").send_keys("Contact Section EN")
	context.browser.find_element_by_name("title:fr").clear()
	context.browser.find_element_by_name("title:fr").send_keys("Contact Section FR")
	#Display the title of the Contact section
	context.browser.find_element_by_id("display-title-1").click()
	#Recipients
	context.browser.find_element_by_id("to-addr").clear()
	context.browser.find_element_by_id("to-addr").send_keys("ganesh.mani@bepatient.com")
	#Button Title
	context.browser.find_element_by_name("button_title:en").clear()
	context.browser.find_element_by_name("button_title:en").send_keys("SEND EN")
	context.browser.find_element_by_name("button_title:fr").clear()
	context.browser.find_element_by_name("button_title:fr").send_keys("ENVOYER FR")
	#Message to display when the user has submitted the form 
	context.browser.find_element_by_name("end_msg:en").clear()
	context.browser.find_element_by_name("end_msg:en").send_keys("THANK YOU VERY MUCH FOR SENDING THE MESSAGE EN")
	context.browser.find_element_by_name("end_msg:fr").clear()
	context.browser.find_element_by_name("end_msg:fr").send_keys("MERCI POUR ENVOYER LE QUESTION OU FEEDBACK FR")
	# Title of the mail for the acknowledgment *
	context.browser.find_element_by_name("confirm_email_subject:en").clear()
	context.browser.find_element_by_name("confirm_email_subject:en").send_keys("EMAIL SENT EN")
	context.browser.find_element_by_name("confirm_email_subject:fr").clear()
	context.browser.find_element_by_name("confirm_email_subject:fr").send_keys("EMAIL A ENVOYE FR")
	# Body of the mail for the acknowledgment *
	context.browser.find_element_by_name("confirm_email_body:en").clear()
	context.browser.find_element_by_name("confirm_email_body:en").send_keys(u"EN I want love, joy, good humor It's not your money that will make my happiness I want to put a hand on my heart, papalapapapala Let's go together, discover my freedom So forget all your clichés, welcome to my reality")
	context.browser.find_element_by_name("confirm_email_body:fr").clear()
	context.browser.find_element_by_name("confirm_email_body:fr").send_keys(u"FR Je veux d'l'amour, d'la joie, de la bonne humeur Ce n'est pas votre argent qui f'ra mon bonheur Moi j'veux crever la main sur le coeur, papalapapapala Allons ensemble, découvrir ma liberté Oubliez donc tous vos clichés, bienvenue dans ma réalité")
	#Colour of the box and title
	context.browser.find_element_by_xpath("//*[contains(text(),'Background color')]/../div/div[2]").click()
	context.browser.find_elements_by_class_name("sp-input")[0].clear()
	context.browser.find_elements_by_class_name("sp-input")[0].send_keys("#000000")
	context.browser.find_element_by_xpath("//*[contains(text(),'Text color')]/../div/div[2]").click()
	context.browser.find_elements_by_class_name("sp-input")[1].clear()
	context.browser.find_elements_by_class_name("sp-input")[1].send_keys("#ffffff")
	context.browser.find_element_by_name("action").click()


@when('I add a carousel to the page')
def step_impl(context):
	#Add Carousel
	context.browser.find_element_by_link_text("Add a box").click()
        context.browser.find_element_by_link_text("Carousel").click()
        context.browser.find_element_by_name("title:en").clear()
        context.browser.find_element_by_name("title:en").send_keys("Title of carousel EN")
        context.browser.find_element_by_name("title:fr").clear()
        context.browser.find_element_by_name("title:fr").send_keys("Title of carousel FR")
        context.browser.find_element_by_xpath("//*[contains(text(),'Background color')]/../div/div[2]").click()
        context.browser.find_elements_by_class_name("sp-input")[0].clear()
        context.browser.find_elements_by_class_name("sp-input")[0].send_keys("#e23636")
        context.browser.find_element_by_xpath("//*[contains(text(),'Text color')]/../div/div[2]").click()
        context.browser.find_elements_by_class_name("sp-input")[1].clear()
        context.browser.find_elements_by_class_name("sp-input")[1].send_keys("#ffffff")
        context.browser.find_element_by_name("action").click()

        context.browser.find_element_by_link_text("Title of carousel EN").click()
        #First Carousel Box
        context.browser.find_element_by_link_text("Add a resource").click()
        context.browser.find_element_by_name("title:en").clear()
        context.browser.find_element_by_name("title:en").send_keys("Carousel box 1")
        context.browser.find_element_by_name("action").click()
        context.browser.find_element_by_name("page_text:en").clear()
        context.browser.find_element_by_name("page_text:en").send_keys("EN Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.")
        context.browser.find_element_by_name("page_text:fr").clear()
        context.browser.find_element_by_name("page_text:fr").send_keys("FR Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.")
        context.browser.find_element_by_xpath("//a/span").click()
        iframe = context.browser.find_elements_by_xpath("/html/body/div[5]/div[2]/iframe")[0]
        context.browser.switch_to_frame(iframe)
        context.browser.find_element_by_id("q").clear()
        context.browser.find_element_by_id("q").send_keys("CarouselImage1")
        context.browser.find_element_by_class_name("btn-primary").click()
        context.browser.find_element_by_class_name("img-responsive").click()
        context.browser.switch_to_default_content()
        context.browser.find_element_by_xpath("//*[contains(text(),'Background color')]/../div/div[2]").click()
        context.browser.find_elements_by_class_name("sp-input")[0].clear()
        context.browser.find_elements_by_class_name("sp-input")[0].send_keys("#ffffff")
        context.browser.find_element_by_xpath("//*[contains(text(),'Text color')]/../div/div[2]").click()
        context.browser.find_elements_by_class_name("sp-input")[1].clear()
        context.browser.find_elements_by_class_name("sp-input")[1].send_keys("#e23636")
        context.browser.find_element_by_name("action").click()

        context.browser.find_element_by_link_text("Title of carousel EN").click()
        #Second Carousel Box
        context.browser.find_element_by_link_text("Add a resource").click()
        context.browser.find_element_by_name("title:en").clear()
        context.browser.find_element_by_name("title:en").send_keys("Carousel box 2")
        context.browser.find_element_by_name("action").click()
        context.browser.find_element_by_name("page_text:en").clear()
        context.browser.find_element_by_name("page_text:en").send_keys("EN Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo.")
        context.browser.find_element_by_name("page_text:fr").clear()
        context.browser.find_element_by_name("page_text:fr").send_keys("FR Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo.")
        context.browser.find_element_by_xpath("//a/span").click()
        iframe = context.browser.find_elements_by_xpath("/html/body/div[5]/div[2]/iframe")[0]
        context.browser.switch_to_frame(iframe)
        context.browser.find_element_by_id("q").clear()
        context.browser.find_element_by_id("q").send_keys("CarouselImage2")
        context.browser.find_element_by_class_name("btn-primary").click()
        context.browser.find_element_by_class_name("img-responsive").click()
        context.browser.switch_to_default_content()
        context.browser.find_element_by_xpath("//*[contains(text(),'Background color')]/../div/div[2]").click()
        context.browser.find_elements_by_class_name("sp-input")[0].clear()
        context.browser.find_elements_by_class_name("sp-input")[0].send_keys("#e23636")
        context.browser.find_element_by_xpath("//*[contains(text(),'Text color')]/../div/div[2]").click()
        context.browser.find_elements_by_class_name("sp-input")[1].clear()
        context.browser.find_elements_by_class_name("sp-input")[1].send_keys("#ffffff")
        context.browser.find_element_by_name("action").click()

        context.browser.find_element_by_link_text("Title of carousel EN").click()
        #Third Carousel Box
        context.browser.find_element_by_link_text("Add a resource").click()
        context.browser.find_element_by_name("title:en").clear()
        context.browser.find_element_by_name("title:en").send_keys("Carousel box 3")
        context.browser.find_element_by_name("action").click()
        context.browser.find_element_by_name("page_text:en").clear()
        context.browser.find_element_by_name("page_text:en").send_keys("EN Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.")
        context.browser.find_element_by_name("page_text:fr").clear()
        context.browser.find_element_by_name("page_text:fr").send_keys("FR Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.")
        context.browser.find_element_by_xpath("//a/span").click()
        iframe = context.browser.find_elements_by_xpath("/html/body/div[5]/div[2]/iframe")[0]
        context.browser.switch_to_frame(iframe)
        context.browser.find_element_by_id("q").clear()
        context.browser.find_element_by_id("q").send_keys("CarouselImage3")
        context.browser.find_element_by_class_name("btn-primary").click()
        context.browser.find_element_by_class_name("img-responsive").click()
        context.browser.switch_to_default_content()
        context.browser.find_element_by_xpath("//*[contains(text(),'Background color')]/../div/div[2]").click()
        context.browser.find_elements_by_class_name("sp-input")[0].clear()
        context.browser.find_elements_by_class_name("sp-input")[0].send_keys("#ffffff")
        context.browser.find_element_by_xpath("//*[contains(text(),'Text color')]/../div/div[2]").click()
        context.browser.find_elements_by_class_name("sp-input")[1].clear()
        context.browser.find_elements_by_class_name("sp-input")[1].send_keys("#e23636")
        context.browser.find_element_by_name("action").click()

        context.browser.find_element_by_link_text("Title of carousel EN").click()
        #Fourth Carousel Box
        context.browser.find_element_by_link_text("Add a resource").click()
        context.browser.find_element_by_name("title:en").clear()
        context.browser.find_element_by_name("title:en").send_keys("Carousel box 4")
        context.browser.find_element_by_name("action").click()
        context.browser.find_element_by_name("page_text:en").clear()
        context.browser.find_element_by_name("page_text:en").send_keys("EN Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.")
        context.browser.find_element_by_name("page_text:fr").clear()
        context.browser.find_element_by_name("page_text:fr").send_keys("FR Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.")
        context.browser.find_element_by_xpath("//a/span").click()
        iframe = context.browser.find_elements_by_xpath("/html/body/div[5]/div[2]/iframe")[0]
        context.browser.switch_to_frame(iframe)
        context.browser.find_element_by_id("q").clear()
        context.browser.find_element_by_id("q").send_keys("CarouselImage4")
        context.browser.find_element_by_class_name("btn-primary").click()
        context.browser.find_element_by_class_name("img-responsive").click()
        context.browser.switch_to_default_content()
        context.browser.find_element_by_xpath("//*[contains(text(),'Background color')]/../div/div[2]").click()
        context.browser.find_elements_by_class_name("sp-input")[0].clear()
        context.browser.find_elements_by_class_name("sp-input")[0].send_keys("#ffffff")
        context.browser.find_element_by_xpath("//*[contains(text(),'Text color')]/../div/div[2]").click()
        context.browser.find_elements_by_class_name("sp-input")[1].clear()
        context.browser.find_elements_by_class_name("sp-input")[1].send_keys("#e23636")
        context.browser.find_element_by_name("action").click()


        context.browser.find_element_by_link_text("Title of carousel EN").click()
        #Fourth Carousel Box
        context.browser.find_element_by_link_text("Add a resource").click()
        context.browser.find_element_by_name("title:en").clear()
        context.browser.find_element_by_name("title:en").send_keys("Carousel box 5")
        context.browser.find_element_by_name("action").click()
        #context.browser.find_element_by_name("page_text:en").clear()
        #context.browser.find_element_by_name("page_text:en").send_keys("EN Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.")
        #context.browser.find_element_by_name("page_text:fr").clear()
        #context.browser.find_element_by_name("page_text:fr").send_keys("FR Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.")
        context.browser.find_element_by_xpath("//a/span").click()
        iframe = context.browser.find_elements_by_xpath("/html/body/div[5]/div[2]/iframe")[0]
        context.browser.switch_to_frame(iframe)
        context.browser.find_element_by_id("q").clear()
        context.browser.find_element_by_id("q").send_keys("CarouselImage1")
        context.browser.find_element_by_class_name("btn-primary").click()
        context.browser.find_element_by_class_name("img-responsive").click()
        context.browser.switch_to_default_content()
        context.browser.find_element_by_xpath("//*[contains(text(),'Background color')]/../div/div[2]").click()
        context.browser.find_elements_by_class_name("sp-input")[0].clear()
        context.browser.find_elements_by_class_name("sp-input")[0].send_keys("#e23636")
        context.browser.find_element_by_xpath("//*[contains(text(),'Text color')]/../div/div[2]").click()
        context.browser.find_elements_by_class_name("sp-input")[1].clear()
        context.browser.find_elements_by_class_name("sp-input")[1].send_keys("#ffffff")
        context.browser.find_element_by_name("action").click()

        context.browser.find_element_by_link_text("Title of carousel EN").click()
        #Fifth Carousel Box
        context.browser.find_element_by_link_text("Add a resource").click()
        context.browser.find_element_by_name("title:en").clear()
        context.browser.find_element_by_name("title:en").send_keys("Carousel box 6")
        context.browser.find_element_by_name("action").click()
        context.browser.find_element_by_name("page_text:en").clear()
        context.browser.find_element_by_name("page_text:fr").clear()
        context.browser.find_element_by_name("page_text:en").send_keys("** Bold text **")
        context.browser.find_element_by_name("page_text:fr").send_keys("** Bold text **")
        context.browser.find_element_by_name("page_text:en").send_keys("# HEADING")
        context.browser.find_element_by_name("page_text:fr").send_keys("# HEADING")
        context.browser.find_element_by_name("page_text:en").send_keys("## SECOND HEADING")
        context.browser.find_element_by_name("page_text:fr").send_keys("## SECOND HEADING")
        context.browser.find_element_by_name("page_text:en").send_keys("Factsheet click [here](/lab/sondages/redirection-factsheet-1-en/)")
        context.browser.find_element_by_name("page_text:fr").send_keys("Factsheet click [here](/lab/sondages/redirection-factsheet-1-en/)")
        context.browser.find_element_by_name("page_text:en").send_keys("EN Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo.")
        context.browser.find_element_by_name("page_text:fr").send_keys("FR Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo.")
        context.browser.find_element_by_xpath("//*[contains(text(),'Background color')]/../div/div[2]").click()
        context.browser.find_elements_by_class_name("sp-input")[0].clear()
        context.browser.find_elements_by_class_name("sp-input")[0].send_keys("#000000")
        context.browser.find_element_by_xpath("//*[contains(text(),'Text color')]/../div/div[2]").click()
        context.browser.find_elements_by_class_name("sp-input")[1].clear()
        context.browser.find_elements_by_class_name("sp-input")[1].send_keys("#ffffff")
        context.browser.find_element_by_name("action").click()


@then(u'I can see the contact box in the list of boxes of the page')
def step_impl(context):
	Image_link = context.browser.find_element_by_link_text("Contact Section EN")
	assert(Image_link)

@then(u'I can see the Author section Box in the list of boxes of the page')
def step_impl(context):
	Image_link = context.browser.find_element_by_link_text("Author Section EN")
	assert(Image_link)


@when('I delete a box')
def step_impl(context):
	context.browser.find_element_by_xpath(".//*[@id='form-table']/table/thead/tr/th[1]/input").click()
	context.browser.find_element_by_class_name("btn-danger").click()
	
