*** Settings ***
Library         Dialogs
Library         librairie.MasterApiManual


*** Test Cases ***
test_0001 : Drone take off
    [Tags]
    ...             campagne master api manual
    [Setup]  Setup test
    Drone take off
    [Teardown]   Teardown test

*** Keywords ***
Drone take off
    sleep  3s

Teardown test
    kill test

Setup test
    init test
