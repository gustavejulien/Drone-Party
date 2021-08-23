
*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0018 : playsong
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    test_playsong
    [Teardown]   Teardown test

*** Keywords ***
test_playsong
    playsong
    sleep  3s
    cmleft
    sleep  3s
    setspeed
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test

