#include "PDCPApp.hpp"
#include "GamePadService.hpp"
#include "APIService.hpp"

#include <iostream>

void PDCPApp::bindGUIButtons()
{
	this->builder->get_widget("patrolBtn", this->patrolBtn);
	if (this->patrolBtn) {
		this->patrolBtn->signal_clicked().connect(sigc::mem_fun(this->apiService, &APIService::patrol));
	}
	this->builder->get_widget("followBtn", this->followBtn);
	if (this->followBtn) {
		this->followBtn->signal_clicked().connect(sigc::mem_fun(this->apiService, &APIService::follow));
	}
	this->builder->get_widget("ascendBtn", this->ascendBtn);
	if (this->ascendBtn) {
		this->ascendBtn->signal_clicked().connect(sigc::mem_fun(this->apiService, &APIService::ascend));
	}
	this->builder->get_widget("descendBtn", this->descendBtn);
	if (this->descendBtn) {
		this->descendBtn->signal_clicked().connect(sigc::mem_fun(this->apiService, &APIService::descend));
	}
	this->builder->get_widget("turnLeftBtn", this->turnLeftBtn);
	if (this->turnLeftBtn) {
		this->turnLeftBtn->signal_clicked().connect(sigc::mem_fun(this->apiService, &APIService::turnLeft));
	}
	this->builder->get_widget("turnRightBtn", this->turnRightBtn);
	if (this->turnRightBtn) {
		this->turnRightBtn->signal_clicked().connect(sigc::mem_fun(this->apiService, &APIService::turnRight));
	}
	// capture Button and gamepad Button behaviors to define
	this->builder->get_widget("forwardBtn", this->forwardBtn);
	if (this->forwardBtn) {
		this->forwardBtn->signal_clicked().connect(std::bind(sigc::mem_fun(this->apiService, &APIService::forward), 10));
	}
	this->builder->get_widget("backwardBtn", this->backwardBtn);
	if (this->backwardBtn) {
		this->backwardBtn->signal_clicked().connect(std::bind(sigc::mem_fun(this->apiService, &APIService::backward), 10));
	}
	this->builder->get_widget("strafeLeftBtn", this->strafeLeftBtn);
	if (this->strafeLeftBtn) {
		this->strafeLeftBtn->signal_clicked().connect(std::bind(sigc::mem_fun(this->apiService, &APIService::strafeLeft), 10));
	}
	this->builder->get_widget("strafeRightBtn", this->strafeRightBtn);
	if (this->strafeRightBtn) {
		this->strafeRightBtn->signal_clicked().connect(std::bind(sigc::mem_fun(this->apiService, &APIService::strafeRight), 10));
	}
}

PDCPApp::PDCPApp()
{
	this->builder = Gtk::Builder::create();
	try	{
		this->builder->add_from_file("PDCP_layout.glade");
	} catch (const Glib::FileError &ex) {
		std::cerr << "FileError: " << ex.what() << std::endl;
	} catch (const Glib::MarkupError &ex) {
		std::cerr << "MarkupError: " << ex.what() << std::endl;
	} catch (const Gtk::BuilderError &ex) {
		std::cerr << "BuilderError: " << ex.what() << std::endl;
	}
	this->builder->get_widget("appWindow", this->window);
	if (this->window) {
		this->bindGUIButtons();
		// build actions
		// joystick elements must wrapper function calling Action *
		 /* each Button must received an Action *
		 ** 
		 */
		// this->bindActionsToGP
	}
}

PDCPApp::~PDCPApp()
{
	delete this->window;
}