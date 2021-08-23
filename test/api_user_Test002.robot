
*** Settings ***
Library         Dialogs
Library         librairie.UserApiLibrary


*** Test Cases ***
test_2: test get user
    [Tags]
    ...             campagne user api
    [Setup]  Setup test
    test_get_user
    [Teardown]   Teardown test

*** Keywords ***
test_get_user
    getuser
    sleep  3s
    execute_manual_step  Is the user's information correctly returned ?

Teardown test
    kill test

Setup test
    init test
