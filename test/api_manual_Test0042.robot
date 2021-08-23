
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0042 : cmforward
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_cmforward
    [Teardown]   Teardown test

*** Keywords ***
test_cmforward
    cmforward
    sleep  3s
    playsong
    sleep  3s
    cmup
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

