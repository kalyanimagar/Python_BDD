Feature: Login functionality
    @login
    Scenario: Verify the login functionality with valid credentails
    Given Launch login page
    When Enter valid username as "kal@gmail.com" and password as "12345"
    And click on login button
    Then User looged in successfully
    @ddt
    Scenario Outline: Login with invalid email and valid password
    Given Launch login page
    When Enter invalid username as "<email_id>" and password as "<password>"
    And click on login button
    Then proper warning message should be displayed

    Examples: 
    
    | email_id | password |
    | jhghj    | jhkj     |
    | jhgjhg   | jhgjh    |
    | 876687   | 9878     |

    Scenario: Login with valid email and invalid password
    Given Launch login page
    When Enter valid username as "kal@gmail.com" and invalid password as "534"
    And click on login button
    Then proper warning message should be displayed

    Scenario: Login with invalid credentails
    Given Launch login page
    When Enter invalid username as "hjgjf" and inpassword as "jhgjh"
    And click on login button
    Then proper warning message should be displayed

    Scenario: Login with no credentails
    Given Launch login page
    When Dont enter email and password
    And click on login button
    Then proper warning message should be displayed
