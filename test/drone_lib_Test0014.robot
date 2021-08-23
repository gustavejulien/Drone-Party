*** Settings ***
Library         Dialogs
Library         librairie.testDroneLibrary


*** Test Cases ***
test_0014: pic
    [Tags]
    ...             campagne client web
    [Setup]  Setup test
    Pic test
    [Teardown]   Teardown test

*** Keywords ***
Pic test
    make_the_drone_take_off
    make_the_drone_take_pic
    make_the_drone_land

Teardown test
    kill test

Setup test
    init test
