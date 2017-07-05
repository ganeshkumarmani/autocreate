Feature: Creating Instance for test
	@implement
	Scenario: Prerequsites
		Given I login to the site as administrator
		Given there are images for factsheets

	Scenario: Creating the parent category for factsheet
		Given I login to the site as administrator
		When I add the parent category for "CATEGORY FOR FACTSHEET"
		Then I add a link for "CATEGORY FOR FACTSHEET" in the menu

	@implement
	Scenario: Creating a factsheet with 4 pages and different types of boxes
		Given I am in the parent category "CATEGORY FOR FACTSHEET"
		When I add a factsheet with 4 pages and different types of boxes

	Scenario: Creating a factsheet with one page
		Given there is a redirection factsheet
		Given I am in the parent category "CATEGORY FOR FACTSHEET"
		When I add a one page factsheet with redirection links
		

