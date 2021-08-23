
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0045 : secbackward
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_secbackward
    [Teardown]   Teardown test

*** Keywords ***
test_secbackward
    secbackward
    sleep  3s
    cmdown
    sleep  3s
    setspeed
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

