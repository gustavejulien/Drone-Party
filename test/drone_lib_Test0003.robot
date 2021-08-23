*** Settings ***
Library         Dialogs
Library         librairie.testDroneLibrary


*** Test Cases ***
test_0003 : Test left
    [Tags]
    ...             campagne lib drone
    [Setup]  Setup test
    Test left
    [Teardown]   Teardown test

*** Keywords ***
Test left
    make_the_drone_take_off
    sleep  3s
    execute_manual_step  Is the drone flying ? 
    make_the_drone_go_left
    sleep  3s
    execute_manual_step  Is the drone flying ?

Teardown test
    kill test

Setup test
    init test
