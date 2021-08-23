
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0017 : setspeed
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_setspeed
    [Teardown]   Teardown test

*** Keywords ***
test_setspeed
    setspeed
    sleep  3s
    secdown
    sleep  3s
    cmdown
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

