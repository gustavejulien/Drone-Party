*** Settings ***
Library         Dialogs
Library         librairie.testDroneLibrary


*** Test Cases ***
test_0008 : test turn left
    [Tags]
    ...             campagne lib drone
    [Setup]  Setup test
    test turn left
    [Teardown]   Teardown test

*** Keywords ***
test turn left
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
