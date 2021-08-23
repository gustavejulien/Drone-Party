*** Settings ***
Library         Dialogs
Library         librairie.testDroneLibrary


*** Test Cases ***
test_0005 : forward
    [Tags]
    ...             campagne lib drone
    [Setup]  Setup test
    test forward
    [Teardown]   Teardown test

*** Keywords ***
test forward
    make_the_drone_take_off
    sleep  3s
    execute_manual_step  Is the drone flying ? 
    make_the_drone_go_forward
    sleep  3s
    execute_manual_step  Is the drone flying ?

Teardown test
    kill test

Setup test
    init test
