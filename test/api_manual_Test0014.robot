
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0014 : setspeed
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_setspeed
    [Teardown]   Teardown test

*** Keywords ***
test_setspeed
    setspeed
    sleep  3s
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

