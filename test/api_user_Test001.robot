
*** Settings ***
Library         Dialogs
Library         librairie.UserApiLibrary


*** Test Cases ***
test_1: test connect user
    [Tags]
    ...             campagne user api
    [Setup]  Setup test
    test_connect_user
    [Teardown]   Teardown test

*** Keywords ***
test_connect_user
    connect
    sleep  3s
    execute_manual_step  Is the user connected ?

Teardown test
    kill test

Setup test
    init test
