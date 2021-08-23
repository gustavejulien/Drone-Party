
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0025 : cmbackward
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_cmbackward
    [Teardown]   Teardown test

*** Keywords ***
test_cmbackward
    cmbackward
    sleep  3s
    playsong
    sleep  3s
    cmup
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

