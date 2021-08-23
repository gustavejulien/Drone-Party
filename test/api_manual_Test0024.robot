
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0024 : playsong
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_playsong
    [Teardown]   Teardown test

*** Keywords ***
test_playsong
    playsong
    sleep  3s
    turnright
    sleep  3s
    secdown
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

