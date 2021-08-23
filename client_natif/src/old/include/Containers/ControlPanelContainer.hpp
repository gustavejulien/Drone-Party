#include <gtkmm.h>
#include "Containers/DisplayContainer.hpp"
#include "GamePadService.hpp"
#include "APIService.hpp"
#include "DirectionButton.hpp"

class ControlPanelContainer: public Gtk::Box
{
public:
	ControlPanelContainer(APIService *apiService, GamePadService *gamePadService);

	// Left controls
	Gtk::Box *leftControlContainer;

	Gtk::ButtonBox *leftControlContainerTopRow;
	DirectionButton *ascendBtn;

	Gtk::ButtonBox *leftControlContainerBottomRow;
	DirectionButton *turnLeftBtn;
	DirectionButton *descendBtn;
	DirectionButton *turnRightBtn;

	// Capture control
	Gtk::Box *captureControlContainer;
	Gtk::Button *captureBtn;

	// GamePad control
	Gtk::Box *gamePadControlContainer;
	Gtk::Button *gamePadBtn;

	// right controls
	Gtk::Box *rightControlContainer;

	Gtk::ButtonBox *rightControlContainerTopRow;
	DirectionButton *forwardBtn;

	Gtk::ButtonBox *rightControlContainerBottomRow;
	DirectionButton *backwardBtn;
	DirectionButton *strafeLeftBtn;
	DirectionButton *strafeRightBtn;

};