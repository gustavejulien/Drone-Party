*** Settings ***
Library         Dialogs
Library         librairie.testDroneLibrary


*** Test Cases ***
test_0016: pic
    [Tags]
    ...             campagne client web
    [Setup]  Setup test
    z1 test
    [Teardown]   Teardown test

*** Keywords ***
z1 test
    make_the_drone_take_off
    sleep  3s
    make_the_drone_turn_right
    sleep  3s
    make_the_drone_go_forward
    sleep  3s
    make_the_drone_turn_left
    sleep  3s
    make_the_drone_go_forward
    execute_manual_step  Is the drone flying ?

Teardown test
    kill test

Setup test
    init test
