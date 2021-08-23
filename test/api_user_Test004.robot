
*** Settings ***
Library         Dialogs
Library         librairie.UserApiLibrary


*** Test Cases ***
test_4: test delete user
    [Tags]
    ...             campagne user api
    [Setup]  Setup test
    test_delete_user
    [Teardown]   Teardown test

*** Keywords ***
test_delete_user
    deleteuser
    sleep  3s
    execute_manual_step  Is the user deleted ?

Teardown test
    kill test

Setup test
    init test

