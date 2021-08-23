
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0016 : turnright
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_turnright
    [Teardown]   Teardown test

*** Keywords ***
test_turnright
    turnright
    sleep  3s
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

