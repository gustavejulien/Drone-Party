#ifndef PDCP_MACROS_HPP
#define PDCP_MACROS_HPP
#include <string>
#include <vector>
#include <functional>

#ifndef __FUNCTION_NAME__
    #ifdef WIN32   //WINDOWS
        #define __FUNCTION_NAME__   __FUNCTION__  
    #else          //*NIX
        #define __FUNCTION_NAME__   __func__ 
    #endif
#endif

namespace PDCP {
	enum exitCodes {
		EXITFAILURE = 84,
		EXITSUCCESS = 0
	};
	enum buttonFcts {
		PATROL,
		FOLLOW,
		ASCEND,
		DESCEND,
		TURN_LEFT,
		TURN_RIGHT,
		FORWARD,
		BACKWARD,
		STRAFE_LEFT,
		STRAFE_RIGHT,
		CONTROLLER,
		CAPTURE
	};
};

#endif