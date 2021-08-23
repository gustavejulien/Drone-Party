#include "Actions/Action.hpp"

class ParameterizedAction : public Action
{
public:
	int param; // cm
	std::function<void (int)> &executor;

	ParameterizedAction(std::function<void (int)> &, int param);
private:
	void trigger();
};
