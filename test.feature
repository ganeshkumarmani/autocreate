Feature: Creating Instance for test

	Scenario: Creating a factsheet with 4 pages and different types of boxes
		Given I am in the parent category "CATEGORY FOR FACTSHEET"
		When I add a factsheet with 4 pages and different types of boxes
			
	Scenario: Creating the parent category for factsheet
		Given I login to the site as administrator
		When I add the parent category for "CATEGORY FOR FACTSHEET"
		Then I add a link for "CATEGORY FOR FACTSHEET" in the menu

	@ninja.chuck
	Scenario: Prerequsites
		Given I login to the site as administrator
		Given there is images for carousel box