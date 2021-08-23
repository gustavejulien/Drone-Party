
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0037 : cmup
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_cmup
    [Teardown]   Teardown test

*** Keywords ***
test_cmup
    cmup
    sleep  3s
    cmleft
    sleep  3s
    secbackward
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

