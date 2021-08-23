#include "Actions/UnparameterizedAction.hpp"

UnParameterizedAction::UnParameterizedAction(std::function<void ()> & executor)
: Action(), executor(executor) {}


void UnParameterizedAction::trigger()
{
	this->executor();
}