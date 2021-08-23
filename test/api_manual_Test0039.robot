
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0039 : turnleft
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_turnleft
    [Teardown]   Teardown test

*** Keywords ***
test_turnleft
    turnleft
    sleep  3s
    takepicture
    sleep  3s
    turnright
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

