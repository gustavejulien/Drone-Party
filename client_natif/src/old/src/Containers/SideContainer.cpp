#include "Containers/SideContainer.hpp"
#include "PDCPMacros.hpp"

SideContainer::SideContainer(Gtk::Box *parent, APIService *apiService, int type)
{
	switch (type) {
	case PDCP::PATROL:
		this->button = new Gtk::Button("PATROL MODE");
		this->button->signal_clicked().connect(sigc::mem_fun(apiService, &APIService::patrol));
		break;
	case PDCP::FOLLOW:
		this->button = new Gtk::Button("FOLLOW MODE");
		this->button->signal_clicked().connect(sigc::mem_fun(apiService, &APIService::follow));
		break;
	default:
		this->button = new Gtk::Button("UNKNOWN");
	}
	this->set_layout(Gtk::BUTTONBOX_CENTER);
	parent->add(*(this->button));
}