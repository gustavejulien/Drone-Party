#include <iostream>
#include <gtkmm.h>
#include "DirectionButton.hpp"
#include "APIService.hpp"
#include "PDCPMacros.hpp"

DirectionButton::DirectionButton(
	APIService *apiService,
	std::string buttonText,
	int targetedFunction)
	: Gtk::Button(buttonText)
{
	std::cout << "building direction button " << buttonText << std::endl;
	this->set_label(buttonText);
	switch (targetedFunction)
	{
	case PDCP::buttonFcts::DESCEND:
		this->signal_clicked().connect(sigc::mem_fun(apiService, &APIService::descend));
		break;
	case PDCP::buttonFcts::ASCEND:
		this->signal_clicked().connect(sigc::mem_fun(apiService, &APIService::ascend));
		break;
	case PDCP::buttonFcts::FORWARD:
		this->signal_clicked().connect(sigc::mem_fun(apiService, &APIService::forward));
		break;
	case PDCP::buttonFcts::BACKWARD:
		this->signal_clicked().connect(sigc::mem_fun(apiService, &APIService::backward));
		break;
	case PDCP::buttonFcts::TURN_LEFT:
		this->signal_clicked().connect(sigc::mem_fun(apiService, &APIService::turnLeft));
		break;
	case PDCP::buttonFcts::TURN_RIGHT:
		this->signal_clicked().connect(sigc::mem_fun(apiService, &APIService::turnRight));
		break;
	case PDCP::buttonFcts::STRAFE_LEFT:
		this->signal_clicked().connect(sigc::mem_fun(apiService, &APIService::strafeLeft));
		break;
	case PDCP::buttonFcts::STRAFE_RIGHT:
		this->signal_clicked().connect(sigc::mem_fun(apiService, &APIService::strafeRight));
		break;
	default:
		std::cerr << "Couldn't find function to assign for targetedFunction " << targetedFunction << std::endl;
		this->set_label("unbound");
		break;
	}
}