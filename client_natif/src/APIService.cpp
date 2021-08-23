#include <iostream>
#include "PDCPMacros.hpp"
#include "APIService.hpp"

APIService::APIService()
{
	std::cout << "building APIService" << std::endl;
}

void APIService::patrol()
{
	std::cout << "APIService " << __FUNCTION_NAME__ << std::endl;
}

void APIService::follow()
{
	std::cout << "APIService " << __FUNCTION_NAME__ << std::endl;
}

void APIService::ascend()
{
	std::cout << "APIService " << __FUNCTION_NAME__ << std::endl;
}

void APIService::descend()
{
	std::cout << "APIService " << __FUNCTION_NAME__ << std::endl;
}

void APIService::turnLeft()
{
	std::cout << "APIService " << __FUNCTION_NAME__ << std::endl;
}

void APIService::turnRight()
{
	std::cout << "APIService " << __FUNCTION_NAME__ << std::endl;
}

void APIService::forward(int cm)
{
	std::cout << "APIService " << __FUNCTION_NAME__ << '(' << cm << ')' << std::endl;
}

void APIService::backward(int cm)
{
	std::cout << "APIService " << __FUNCTION_NAME__ << '(' << cm << ')' << std::endl;
}

void APIService::strafeLeft(int cm)
{
	std::cout << "APIService " << __FUNCTION_NAME__ << '(' << cm << ')' << std::endl;
}

void APIService::strafeRight(int cm)
{
	std::cout << "APIService " << __FUNCTION_NAME__ << '(' << cm << ')' << std::endl;
}
