#include <iostream>
#include "GamePadService.hpp"
#include "PDCPMacros.hpp"

GamePadService::GamePadService()
{
	std::cout << "building GAMEPAD" << std::endl;
}
void GamePadService::patrol()
{
	std::cout << "GAMEPAD" <<  __FUNCTION_NAME__ << std::endl;
}

void GamePadService::follow()
{
	std::cout << "GAMEPAD" <<  __FUNCTION_NAME__  << std::endl;
}

void GamePadService::ascend()
{
	std::cout << "GAMEPAD" <<  __FUNCTION_NAME__  << std::endl;
}

void GamePadService::descend()
{
	std::cout << "GAMEPAD" <<  __FUNCTION_NAME__  << std::endl;
}

void GamePadService::turnLeft()
{
	std::cout << "GAMEPAD" <<  __FUNCTION_NAME__  << std::endl;
}

void GamePadService::turnRight()
{
	std::cout << "GAMEPAD" <<  __FUNCTION_NAME__  << std::endl;
}

void GamePadService::forward()
{
	std::cout << "GAMEPAD" <<  __FUNCTION_NAME__  << std::endl;
}

void GamePadService::backward()
{
	std::cout << "GAMEPAD" <<  __FUNCTION_NAME__  << std::endl;
}

void GamePadService::strafeLeft()
{
	std::cout << "GAMEPAD" <<  __FUNCTION_NAME__  << std::endl;
}

void GamePadService::strafeRight()
{
	std::cout << "GAMEPAD" <<  __FUNCTION_NAME__  << std::endl;
}
