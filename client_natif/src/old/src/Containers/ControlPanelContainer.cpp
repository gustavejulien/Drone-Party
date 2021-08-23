#include <string>
#include "Containers/ControlPanelContainer.hpp"
#include "PDCPMacros.hpp"

ControlPanelContainer::ControlPanelContainer(APIService *apiService, GamePadService *gamePadService)
{
	/*
	** Containers & Buttons instancing
	*/
	// LeftControls
	this->leftControlContainer = new Gtk::Box(Gtk::ORIENTATION_VERTICAL);
	// topRow
	this->leftControlContainerTopRow = new Gtk::ButtonBox(Gtk::ORIENTATION_HORIZONTAL);
	this->ascendBtn = new DirectionButton(apiService, std::string("ASCEND"), PDCP::ASCEND);
	// bottomRow
	this->leftControlContainerBottomRow = new Gtk::ButtonBox(Gtk::ORIENTATION_HORIZONTAL);
	this->strafeLeftBtn = new DirectionButton(apiService, std::string("STRAFELEFT"), PDCP::STRAFE_LEFT);
	this->descendBtn = new DirectionButton(apiService, std::string("DESCEND"), PDCP::DESCEND);
	this->strafeRightBtn = new DirectionButton(apiService, std::string("STRAFERIGHT"), PDCP::STRAFE_RIGHT);

	// Capture Container
	this->captureControlContainer = new Gtk::Box(Gtk::ORIENTATION_VERTICAL);
	this->captureBtn = new Gtk::Button("Capture");
	
	//  gamepadControl
	this->gamePadControlContainer = new Gtk::Box(Gtk::ORIENTATION_VERTICAL);
	this->gamePadBtn = new Gtk::Button("GamePad");

	// Right Controllers
	this->rightControlContainer = new Gtk::Box(Gtk::ORIENTATION_VERTICAL);
	// top row
	this->rightControlContainerTopRow = new Gtk::ButtonBox(Gtk::ORIENTATION_HORIZONTAL);
	this->forwardBtn = new DirectionButton(apiService, std::string("FORWARD"), PDCP::FORWARD);
	// bottom row
	this->rightControlContainerBottomRow = new Gtk::ButtonBox(Gtk::ORIENTATION_HORIZONTAL);
	this->turnLeftBtn = new DirectionButton(apiService, std::string("TURNLEFT"), PDCP::TURN_LEFT);
	this->backwardBtn = new DirectionButton(apiService, std::string("BACKWARD"), PDCP::BACKWARD);
	this->turnRightBtn = new DirectionButton(apiService, std::string("TURNRIGHT"), PDCP::TURN_RIGHT);


	/*
	**	children to parents association
	*/
	this->leftControlContainerTopRow->pack_start(*(Gtk::Button *)(this->ascendBtn), Gtk::PACK_EXPAND_WIDGET, 10);
	this->leftControlContainerBottomRow->pack_start(*(Gtk::Button *)(this->turnLeftBtn), Gtk::PACK_EXPAND_WIDGET, 10);
	this->leftControlContainerBottomRow->pack_start(*(Gtk::Button *)(this->descendBtn), Gtk::PACK_EXPAND_WIDGET, 10);
	this->leftControlContainerBottomRow->pack_start(*(Gtk::Button *)(this->turnRightBtn), Gtk::PACK_EXPAND_WIDGET, 10);

	this->rightControlContainerTopRow->pack_start(*(Gtk::Button *)(this->forwardBtn), Gtk::PACK_EXPAND_WIDGET, 10);
	this->rightControlContainerBottomRow->pack_start(*(Gtk::Button *)(this->strafeLeftBtn), Gtk::PACK_EXPAND_WIDGET, 10);
	this->rightControlContainerBottomRow->pack_start(*(Gtk::Button *)(this->backwardBtn), Gtk::PACK_EXPAND_WIDGET, 10);
	this->rightControlContainerBottomRow->pack_start(*(Gtk::Button *)(this->strafeRightBtn), Gtk::PACK_EXPAND_WIDGET, 10);

	this->captureControlContainer->add(*(Gtk::Button *)(this->captureBtn));

	this->gamePadControlContainer->add(*(Gtk::Button *)(this->gamePadBtn));

	this->leftControlContainer->pack_start(*(Gtk::Box *)(this->leftControlContainerTopRow));
	this->leftControlContainer->pack_start(*(Gtk::Box *)(this->leftControlContainerBottomRow));
	this->rightControlContainer->pack_start(*(Gtk::Box*)(this->rightControlContainerTopRow));
	this->rightControlContainer->pack_start(*(Gtk::Box*)(this->rightControlContainerBottomRow));

	this->pack_start(*(Gtk::Box*)(this->leftControlContainer));
	this->pack_start(*(Gtk::Box*)(this->gamePadControlContainer));
	this->pack_start(*(Gtk::Box*)(this->captureControlContainer));
	this->pack_start(*(Gtk::Box*)(this->rightControlContainer));

	/*
	** Layout
	*/
	this->leftControlContainerTopRow->set_layout(Gtk::BUTTONBOX_CENTER);
	this->leftControlContainerBottomRow->set_layout(Gtk::BUTTONBOX_CENTER);
	this->leftControlContainerTopRow->set_spacing(20);
	this->leftControlContainerBottomRow->set_spacing(20);
}