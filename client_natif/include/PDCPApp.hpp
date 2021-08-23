#include <gtkmm.h>
#include "APIService.hpp"
#include "GamePadService.hpp"

class PDCPApp {
public:
	GamePadService gamePadService;
	APIService apiService;
	Gtk::Window *window = nullptr;
	Glib::RefPtr<Gtk::Builder> builder;
	Gtk::Button *followBtn = nullptr;
	Gtk::Button *patrolBtn = nullptr;
	Gtk::Button *ascendBtn = nullptr;
	Gtk::Button *descendBtn = nullptr;
	Gtk::Button *turnRightBtn = nullptr;
	Gtk::Button *turnLeftBtn = nullptr;
	Gtk::Button *captureBtn = nullptr;
	Gtk::Button *gamepadBtn = nullptr;
	Gtk::Button *forwardBtn = nullptr;
	Gtk::Button *backwardBtn = nullptr;
	Gtk::Button *strafeRightBtn = nullptr;
	Gtk::Button *strafeLeftBtn = nullptr;

	PDCPApp();
	~PDCPApp();
	void bindGUIButtons();
};