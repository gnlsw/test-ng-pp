
IF(MSVC)
  ADD_DEFINITIONS( -D_CRT_SECURE_NO_WARNINGS )
ENDIF(MSVC)

SET(TESTNGPP_SRCS
  StupidTimer.cpp
  OptionList.cpp 
  StringToOptions.cpp
  ConsoleState.cpp
)

IF(MSVC)
  INCLUDE_DIRECTORIES(
	${CMAKE_SOURCE_DIR}/src 
	${CMAKE_CURRENT_SOURCE_DIR}
  )
  SET(TESTNGPP_SRCS ${TESTNGPP_SRCS} GetOpt.c)
ENDIF(MSVC)

ADD_LIBRARY(testngpp-utils STATIC ${TESTNGPP_SRCS})

INCLUDE_DIRECTORIES(BEFORE ${CMAKE_SOURCE_DIR}/include)

