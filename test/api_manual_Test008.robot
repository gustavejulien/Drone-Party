
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_008 : secup
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_secup
    [Teardown]   Teardown test

*** Keywords ***
test_secup
    secup
    sleep  3s
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

