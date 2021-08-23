*** Settings ***
Library         Dialogs
Library         librairie.testDroneLibrary


*** Test Cases ***
test_0002 : forward
    [Tags]
    ...             campagne lib drone
    [Setup]  Setup test
    test forward
    [Teardown]   Teardown test

*** Keywords ***
test forward
    make_the_drone_take_off
    sleep  3s
    make_the_drone_go_forward
    execute_manual_step  is the drone going forward

Teardown test
    kill test

Setup test
    init test
