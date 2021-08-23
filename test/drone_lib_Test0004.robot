*** Settings ***
Library         Dialogs
Library         librairie.testDroneLibrary


*** Test Cases ***
test_0004 : Test right
    [Tags]
    ...             campagne lib drone
    [Setup]  Setup test
    Test right
    [Teardown]   Teardown test

*** Keywords ***
Test right
    make_the_drone_take_off
    sleep  3s
    execute_manual_step  Is the drone flying ? 
    make_the_drone_go_right
    sleep  3s
    execute_manual_step  Is the drone flying ?

Teardown test
    kill test

Setup test
    init test
