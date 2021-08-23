
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0049 : turnleft
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_turnleft
    [Teardown]   Teardown test

*** Keywords ***
test_turnleft
    turnleft
    sleep  3s
    secdown
    sleep  3s
    cmup
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

