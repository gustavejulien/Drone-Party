
*** Settings ***
Library         Dialogs
Library         librairie.UserApiLibrary


*** Test Cases ***
test_0: test post user
    [Tags]
    ...             campagne user api
    [Setup]  Setup test
    test_post_user
    [Teardown]   Teardown test

*** Keywords ***
test_post_user
    postuser
    sleep  3s
    execute_manual_step  Is the user created ?

Teardown test
    kill test

Setup test
    init test
