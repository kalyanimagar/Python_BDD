Feature: Search functionality
    @search
    Scenario: Search for valid functionality
    Given Open home page
    When Enter valid product in search box
    And click on Search button
    Then Valid product should get listed in search results
    
    Scenario: serach for invalid product
    Given Open Home page
    When Enter invalid product in search box
    And click on Search button
    Then Proper validation message should be displayed

    Scenario: serach withput entering product
    Given Open Home page
    When Dont enter any product in search box
    And click on Search button
    Then Proper validation message should be displayed