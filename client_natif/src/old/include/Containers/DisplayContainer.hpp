#ifndef DISPLAY_CONTAINER_HPP
#define DISPLAY_CONTAINER_HPP

#include <gtkmm.h>
#include "APIService.hpp"
#include "Containers/SideContainer.hpp"

class DisplayContainer : Gtk::Box {
public:
	DisplayContainer(APIService *apiService);

	SideContainer *doggyButtonContainer;
	Gtk::Box *videoFeedContainer;
	SideContainer *patrolButtonContainer;

	Gtk::Button *patrolBtn;
	Gtk::Button *followBtn;
};

#endif