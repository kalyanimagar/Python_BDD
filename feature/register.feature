Feature: Register account functionality
    @dd
    Scenario: register with mandatory fields
    Given Naviagte to Register page
    When Enter below details in all mandatory fields        
        |first_name|last_name|telephone|password|confirm_password|
        |kalyani|Magar|34535|3432|34435|
        
    And Click on Continue button
    Then Account should get registered

    Scenario: register with all fields
    Given Naviagte to Register page
    When Enter details in all fields
    And Click on Continue button
    Then Account should get registered

    Scenario: register without email address
    Given Naviagte to Register page
    When Enter details in all fields and dont enter email address in email field
    And Click on Continue button
    Then proper warning message informing about missing emailshould get dispalyed

    Scenario: register with duplicate email address
    Given Naviagte to Register page
    When Enter details in all fields and enter dupliacte email address in email field
    And Click on Continue button
    Then proper warning message informing about duplicate account should get dispalyed

    Scenario: register without entering any details
    Given Naviagte to Register page
    When Dont enter details in any fields
    And Click on Continue button
    Then proper warning message for mandatory fields should get displayed

