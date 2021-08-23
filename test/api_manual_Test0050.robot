
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0050 : secforward
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_secforward
    [Teardown]   Teardown test

*** Keywords ***
test_secforward
    secforward
    sleep  3s
    cmright
    sleep  3s
    cmbackward
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

