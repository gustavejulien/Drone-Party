*** Settings ***
Library         Dialogs
Library         librairie.testDroneLibrary


*** Test Cases ***
test_0010 : Drone take off and land
    [Tags]
    ...             campagne lib drone
    [Setup]  Setup test
    Drone take off and land
    [Teardown]   Teardown test

*** Keywords ***
Drone take off and land
    make_the_drone_take_off
    sleep  3s
    execute_manual_step  Is the drone flying ? 
    make_the_drone_land
    sleep  3s
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test
