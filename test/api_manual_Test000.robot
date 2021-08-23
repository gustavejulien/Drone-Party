
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_000 : secforward
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_secforward
    [Teardown]   Teardown test

*** Keywords ***
test_secforward
    secforward
    sleep  3s
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

