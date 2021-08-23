#include "Actions/Action.hpp"

class UnParameterizedAction : public Action
{
public:
	std::function<void ()> &executor;

	UnParameterizedAction(std::function<void ()> &);
private:
	void trigger();
};