*** Settings ***
Library         Dialogs
Library         librairie.testDroneLibrary


*** Test Cases ***
test_0001 : Drone take off
    [Tags]
    ...             campagne lib drone
    [Setup]  Setup test
    Drone take off
    [Teardown]   Teardown test

*** Keywords ***
Drone take off
    make_the_drone_take_off
    sleep  3s
    execute_manual_step  Is the drone flying ? 

Teardown test
    kill test

Setup test
    init test
