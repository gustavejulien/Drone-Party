
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0029 : cmdown
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_cmdown
    [Teardown]   Teardown test

*** Keywords ***
test_cmdown
    cmdown
    sleep  3s
    takepicture
    sleep  3s
    secup
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

