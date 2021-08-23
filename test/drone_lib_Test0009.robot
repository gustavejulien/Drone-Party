*** Settings ***
Library         Dialogs
Library         librairie.testDroneLibrary


*** Test Cases ***
test_0009: test turn right
    [Tags]
    ...             campagne lib drone
    [Setup]  Setup test
    test turn right
    [Teardown]   Teardown test

*** Keywords ***
test turn right
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
