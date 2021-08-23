
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0023 : secright
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_secright
    [Teardown]   Teardown test

*** Keywords ***
test_secright
    secright
    sleep  3s
    cmup
    sleep  3s
    playsong
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

