#ifndef DIRECTION_BUTTON_HPP
#define DIRECTION_BUTTON_HPP

#include <gtkmm.h>
#include <functional>
#include <string>
#include <iostream>
#include "APIService.hpp"

class DirectionButton : public Gtk::Button
{
public:
	DirectionButton(APIService *apiService, std::string buttonText, int targetedFunction);
	~DirectionButton() {
		std::cout << "Direction button '" << this->get_label() << "' destroyed" << std::endl;
	}
};

#endif