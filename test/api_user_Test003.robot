
*** Settings ***
Library         Dialogs
Library         librairie.UserApiLibrary


*** Test Cases ***
test_3: test modify user
    [Tags]
    ...             campagne user api
    [Setup]  Setup test
    test_put_user
    [Teardown]   Teardown test

*** Keywords ***
test_put_user
    putuser
    sleep  3s
    execute_manual_step  Is the user's information correctly changed ?

Teardown test
    kill test

Setup test
    init test
