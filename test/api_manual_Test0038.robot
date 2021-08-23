
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0038 : cmleft
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_cmleft
    [Teardown]   Teardown test

*** Keywords ***
test_cmleft
    cmleft
    sleep  3s
    cmup
    sleep  3s
    secdown
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

