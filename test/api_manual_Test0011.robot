
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0011 : secdown
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_secdown
    [Teardown]   Teardown test

*** Keywords ***
test_secdown
    secdown
    sleep  3s
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

