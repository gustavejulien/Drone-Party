
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0026 : cmleft
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_cmleft
    [Teardown]   Teardown test

*** Keywords ***
test_cmleft
    cmleft
    sleep  3s
    secbackward
    sleep  3s
    secleft
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

