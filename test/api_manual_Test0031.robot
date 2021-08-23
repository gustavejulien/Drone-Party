
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0031 : secright
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_secright
    [Teardown]   Teardown test

*** Keywords ***
test_secright
    secright
    sleep  3s
    cmdown
    sleep  3s
    cmup
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

