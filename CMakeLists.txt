cmake_minimum_required(VERSION 2.8)

if(POLICY CMP0048)
	cmake_policy(SET CMP0048 NEW)
endif()

project(tsend
#	VERSION 0.4.0
#	DESCRIPTION "Send telegram messages from command-line"
)

include(GNUInstallDirs)
#include(CPack)
include(FindPkgConfig)

pkg_check_modules(BASHCOMP bash-completion)

if(BASHCOMP_FOUND)
	#pkg_get_variable(COMPLETIONS_DIR bash-completion completionsdir)
	execute_process(
		COMMAND ${PKG_CONFIG_EXECUTABLE} bash-completion --variable=completionsdir
		OUTPUT_VARIABLE COMPLETIONS_DIR
	)
endif(BASHCOMP_FOUND)

if(NOT DEFINED COMPLETIONS_DIR)
        set(COMPLETIONS_DIR "/etc/bash_completion.d")
endif(NOT DEFINED COMPLETIONS_DIR)


file(READ ${CMAKE_SOURCE_DIR}/scripts/tsend TSEND_BODY_IN)
string(REPLACE "@VERSION@" "${CMAKE_PROJECT_VERSION}" TSEND_BODY_OUT "${TSEND_BODY_IN}")
file(WRITE ${CMAKE_BINARY_DIR}/scripts/tsend ${TSEND_BODY_OUT})

install(PROGRAMS
	${CMAKE_BINARY_DIR}/scripts/tsend
	DESTINATION ${CMAKE_INSTALL_FULL_BINDIR}
)
install(FILES
	${CMAKE_SOURCE_DIR}/bash-completion/tsend
	DESTINATION ${COMPLETIONS_DIR}
)


message(STATUS "Install scripts to ${CMAKE_INSTALL_FULL_BINDIR}")
message(STATUS "Install completions to ${COMPLETIONS_DIR}")


