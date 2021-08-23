
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0013 : takepicture
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_takepicture
    [Teardown]   Teardown test

*** Keywords ***
test_takepicture
    takepicture
    sleep  3s
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

