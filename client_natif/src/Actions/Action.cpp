#include <iostream>
#include "Action.hpp"

Action::Action()
{
	this->timeOfLastTrigger = std::chrono::steady_clock::now();
}

void Action::checkAndTrigger()
{
	std::chrono::time_point<std::chrono::steady_clock> now = std::chrono::steady_clock::now();

	auto milliseconds = std::chrono::duration_cast<std::chrono::milliseconds>(this->timeOfLastTrigger - now);
	auto ms = milliseconds.count();

	if (ms < this->triggerIntervalMs) {
		std::cout << "ms(" << ms << ") < " << "cooldown(" << this->triggerIntervalMs << ") -> Action not fired" << std::endl;
		return;
	}

	this->trigger();
	this->active = true;
	this->timeOfLastTrigger = std::chrono::steady_clock::now();
}

void Action::unTrigger()
{
	this->active = false;
}