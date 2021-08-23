#include "Actions/ParameterizedAction.hpp"

ParameterizedAction::ParameterizedAction(std::function<void (int)> & executor, int param)
: Action(), executor(executor) {}

void ParameterizedAction::trigger()
{
	this->executor(this->param);
}