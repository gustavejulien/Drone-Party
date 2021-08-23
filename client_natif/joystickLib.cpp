#include <iostream>
#include <SFML/Window/Joystick.hpp>
#include <thread>
#include <chrono>
#include <map>
#include <string>

/*
**	Compile with 
**  g++ -Wall -Wextra main.cpp  -lsfml-window -lsfml-system
*/

template<class T>
T abs(T val)
{
	if (val < 0)
		return val *= -1;
	return val;
}

/*
** class inputData should have all the variables common to the class below, 
** and these classes should inherit from it.
** It should accept an Action *, have a fct to call it, and a public fct to change it
*/


class AxisData {
public:
	int belongsTo;
	sf::Joystick::Axis axisNumber;
	std::string axisName;
	bool isTriggered = false;
	float position = 0;
	float threshold = 50;

	AxisData(unsigned int joystickNb, sf::Joystick::Axis axisNb, std::string name)
		:belongsTo(joystickNb), axisNumber(axisNb), axisName(name) {}
	virtual ~AxisData() = default;
	virtual bool isTriggering(float toTest) = 0;
	virtual void refreshState() = 0;
};

class StickAxisData : public AxisData{
public:

	StickAxisData(unsigned int joystickNb, sf::Joystick::Axis axisNb, std::string name)
	:AxisData(joystickNb, axisNb, name) {
		std::cout << "Building AxisData no " << joystickNb << std::endl;
	};
	~StickAxisData() = default;

	bool isTriggering (float toTest)
	{
		return (abs(toTest) > threshold);
	}

	void refreshState() {
		float pst = sf::Joystick::getAxisPosition(this->belongsTo, this->axisNumber);

		if (pst != this->position) {
			if (this->isTriggered == false && isTriggering(pst)) {
				std::cout << "-> PRESSED" << std::endl;
				this->isTriggered = true;
			} else if (this->isTriggered == true && !isTriggering(pst)) {
				std::cout << "-> LET GO" << std::endl;
				this->isTriggered = false;
			}
			this->position = pst;
		}
	}
};

struct TriggerAxisData : public AxisData {
public:

	TriggerAxisData(unsigned int joystickNb, sf::Joystick::Axis axisNb, std::string name)
	:AxisData(joystickNb, axisNb, name){};

	~TriggerAxisData() = default;

	bool isTriggering (float toTest)
	{
		return (toTest > this->threshold);
	}

	void refreshState() {
		float pst = sf::Joystick::getAxisPosition(this->belongsTo, this->axisNumber);

		if (pst != this->position) {
			std::cout << "refreshing axis " << this->axisNumber << " (" << this->axisName << ")(" << pst << ")" << std::endl;
			if (this->isTriggered == false && isTriggering(pst)) {
				std::cout << "-> PRESSED" << std::endl;
				this->isTriggered = true;
			} else if (this->isTriggered == true && pst < this->threshold) {
				std::cout << "-> LET GO" << std::endl;
				this->isTriggered = false;
			}
			this->position = pst;
		}
	}
};


struct ButtonData {
	unsigned int belongsTo;
	unsigned int buttonNumber;
	bool isPressed = false;
	std::string buttonName;

	ButtonData(unsigned int jstNo, unsigned int btnNo, std::string name): belongsTo(jstNo), buttonNumber(btnNo), buttonName(name) {};
	~ButtonData() = default;

	void refreshState() {
		bool isPrs = sf::Joystick::isButtonPressed(this->belongsTo, this->buttonNumber);
		if (this->isPressed == false && isPrs == true) {
			std::cout << buttonName << " -> PRESSED" << std::endl;
			this->isPressed = true;
		} else if (this->isPressed == true && isPrs == false) {
			std::cout << buttonName << " -> LET GO" << std::endl;
			this->isPressed = false;
		}
	}
};


class jostikState {
public:
	unsigned int jstNo;
	bool isConnected;
	bool isInited = false;
	bool hasX;
	int buttonsCount;
	sf::Joystick::Identification id;
	std::map<unsigned int, AxisData*> axises;
	std::map<unsigned int, ButtonData*> buttons;

	jostikState(unsigned int jstNo): jstNo(jstNo) {
		std::cout << "Building js no " << jstNo << std::endl;
		this->axises.insert({0, new StickAxisData(this->jstNo, sf::Joystick::Axis::X, "X")});
		this->axises.insert({1, new StickAxisData(this->jstNo, sf::Joystick::Axis::Y, "Y")});
		this->axises.insert({2, new TriggerAxisData(this->jstNo, sf::Joystick::Axis::Z, "Z")});
		this->axises.insert({3, new TriggerAxisData(this->jstNo, sf::Joystick::Axis::R, "R")});
		this->axises.insert({4, new StickAxisData(this->jstNo, sf::Joystick::Axis::U, "U")});
		this->axises.insert({5, new StickAxisData(this->jstNo, sf::Joystick::Axis::V, "V")});
		this->axises.insert({6, new StickAxisData(this->jstNo, sf::Joystick::Axis::PovX, "PovX")});
		this->axises.insert({7, new StickAxisData(this->jstNo, sf::Joystick::Axis::PovY, "PovY")});
		this->isConnected = sf::Joystick::isConnected(this->jstNo);

		std::string names[] = {"A","B","X","Y","LB","RB","VIEW","MENU","XBOX","LSB","RSB", "SHARE"};
		std::cout << "buttons = " << sf::Joystick::getButtonCount(this->jstNo) << std::endl;
		for (unsigned int i = 0; i <= sf::Joystick::getButtonCount(this->jstNo); ++i) {
			this->buttons.insert({i, new ButtonData(this->jstNo, i, names[i])});
		}
		if (this->isConnected) {
			this->refreshState();
			this->isInited = true;
		}
	};
	~jostikState() {
		for (auto curr = buttons.begin(); curr != buttons.end(); ++curr)
			delete curr->second;
		for (auto curr = axises.begin(); curr != axises.end(); ++curr)
			delete curr->second;
	};

	void refreshState()
	{
		bool isCted = sf::Joystick::isConnected(this->jstNo);

		if (isCted && this->isConnected == false) {
			std::cout << "CONNECTED js " << this->jstNo << std::endl;
			this->isConnected = true;
		} else if (isCted == false && this->isConnected == true) {
			std::cout << "DISCONNECTED js " << this->jstNo << std::endl;
			this->isConnected = false;
		}
		if (this->isConnected) {
			if (!this->isInited) {
				this->id = sf::Joystick::getIdentification(jstNo);
				std::cout << "Joystick name : " << this->id.name.toAnsiString() << std::endl;
				std::cout << "Joystick productId : " << this->id.productId << std::endl;
				std::cout << "Joystick vendorId : " << this->id.vendorId << std::endl;
				this->buttonsCount = sf::Joystick::getButtonCount(this->jstNo);
				this->isInited = true;
			}
			for (unsigned int i = 0; i < this->axises.size(); ++i)
				this->axises.at(i)->refreshState();
			for (unsigned int i = 0; i < this->buttons.size(); ++i)
				this->buttons.at(i)->refreshState();
		}
	}
};

int main(void)
{
	sf::Joystick::update();
	jostikState jst0 = jostikState(0);

	while (true) {
		sf::Joystick::update();
		jst0.refreshState(); // call actions.trigger()
	}
}