#include <gtkmm.h>
#include "Containers/DisplayContainer.hpp"
#include "PDCPMacros.hpp"

DisplayContainer::DisplayContainer(APIService *apiService)
{
	this->doggyButtonContainer = new SideContainer(this, apiService, PDCP::FOLLOW);
	this->patrolButtonContainer = new SideContainer(this, apiService, PDCP::PATROL);
	this->pack_start(*(this->doggyButtonContainer), Gtk::PACK_EXPAND_WIDGET);
	this->pack_start(*(this->patrolButtonContainer), Gtk::PACK_EXPAND_WIDGET);
}