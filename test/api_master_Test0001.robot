*** Settings ***
Library         Dialogs
Library         librairie.template


*** Test Cases ***
test_0001 : drone go up and down
    [Tags]
    ...             campagne client web
    [Setup]  Setup test
    drone goes up and down
    [Teardown]   Teardown test

*** Keywords ***
drone goes up and down
    go_up_and_down
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test
