
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0040 : cmright
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_cmright
    [Teardown]   Teardown test

*** Keywords ***
test_cmright
    cmright
    sleep  3s
    secforward
    sleep  3s
    cmbackward
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

