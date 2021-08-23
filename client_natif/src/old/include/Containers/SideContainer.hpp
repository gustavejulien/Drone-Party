#ifndef SIDECONTAINER_HPP
#define SIDECONTAINER_HPP

#include <gtkmm.h>
#include <string>
#include "APIService.hpp"

class SideContainer : public Gtk::ButtonBox {
public:
	SideContainer(Gtk::Box *, APIService *apiService, int type);

	Gtk::Button *button;
};

#endif