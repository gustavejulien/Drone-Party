#ifndef GAMEPAD_SERVICE_HPP
#define GAMEPAD_SERVICE_HPP

class GamePadService {
public:
	/*
		This is where the peripheral will be used.
	*/
	GamePadService();
	~GamePadService() = default;
	bool GamepadIsConnected();

	// sighanders
	void patrol();
	void follow();
	void ascend();
	void descend();
	void turnLeft();
	void turnRight();
	void forward();
	void backward();
	void strafeLeft();
	void strafeRight();
	void params();
};

#endif