#ifndef MAINCONTAINER_HPP
#define MAINCONTAINER_HPP

#include "APIService.hpp"
#include "GamePadService.hpp"

class MainContainer {
public:
	MainContainer(APIService *apiService, GamePadService* gamePadService);

};

#endif