*** Settings ***
Library         Dialogs
Library         librairie.testDroneLibrary


*** Test Cases ***
test_0011: Square test
    [Tags]
    ...             campagne client web
    [Setup]  Setup test
    Square test
    [Teardown]   Teardown test

*** Keywords ***
Square test
    make_the_drone_take_off
    sleep  3s
    make_the_drone_turn_left
    sleep  3s
    make_the_drone_go_forward
    sleep  3s
    make_the_drone_turn_left
    sleep  3s
    make_the_drone_go_forward
    sleep  3s
    make_the_drone_turn_left
    sleep  3s
    make_the_drone_go_forward
    sleep  3s
    make_the_drone_turn_left
    sleep  3s
    execute_manual_step  Have the drone draw a square ?
    make_the_drone_land

Teardown test
    kill test

Setup test
    init test
