
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0010 : cmdown
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_cmdown
    [Teardown]   Teardown test

*** Keywords ***
test_cmdown
    cmdown
    sleep  3s
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

