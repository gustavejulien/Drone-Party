
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0048 : cmbackward
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_cmbackward
    [Teardown]   Teardown test

*** Keywords ***
test_cmbackward
    cmbackward
    sleep  3s
    cmforward
    sleep  3s
    secbackward
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

