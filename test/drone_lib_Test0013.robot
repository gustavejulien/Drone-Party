*** Settings ***
Library         Dialogs
Library         librairie.testDroneLibrary


*** Test Cases ***
test_0013: Square test
    [Tags]
    ...             campagne client web
    [Setup]  Setup test
    Have the drone turn on himslef
    [Teardown]   Teardown test

*** Keywords ***
Have the drone turn on himslef
    make_the_drone_take_off
    sleep  3s
    make_the_drone_turn_right
    sleep  3s
    make_the_drone_turn_right
    sleep  3s
    make_the_drone_turn_right
    sleep  3s
    make_the_drone_turn_right
    sleep  3s
    execute_manual_step  Have the drone turn on himslef ?
    make_the_drone_land

Teardown test
    kill test

Setup test
    init test
