Feature: Index Page Feature
       
  Scenario: Verify the presence of the 'Hello World!' heading
    Given I visit the index page
    Then I should see the heading "Hello World!"
	
  Scenario: Verify the presence of the input field on the index page
    Given I visit the index page
    Then I should see an input field with the name "name"

  Scenario: Submitting valid input
    Given I visit the index page
    When I submit valid input "John" in the input field
    Then I should see the heading "Heading with Inputs Added"
    And I should see the submitted input "name: John" displayed on the page
