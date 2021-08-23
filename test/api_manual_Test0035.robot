
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0035 : cmdown
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_cmdown
    [Teardown]   Teardown test

*** Keywords ***
test_cmdown
    cmdown
    sleep  3s
    secdown
    sleep  3s
    cmleft
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

