#include <chrono>
#include <functional>
#include "APIService.hpp"

class Action {
public:
	bool repeatable;
	bool active;
	int triggerIntervalMs = 100; // cooldown, must be 0,10 sec
	std::chrono::time_point<std::chrono::steady_clock> timeOfLastTrigger;

	Action();
	void checkAndTrigger();
	void unTrigger();
private:
	virtual void trigger() = 0;
};