#ifndef API_SERVICE_HPP
#define API_SERVICE_HPP

#include <iostream>
class APIService
{
public:
	APIService();
	~APIService() = default;
	// connect
	void patrol();
	void follow();
	void ascend();
	void descend();
	void turnLeft();
	void turnRight();
	void forward(int cm);
	void backward(int cm);
	void strafeLeft(int cm);
	void strafeRight(int cm);
};

#endif /* API_SERVICE_HPP */