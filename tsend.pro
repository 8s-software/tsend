
TEMPLATE = aux
VERSION = 0.1.0

isEmpty(DESTDIR):DESTDIR = $${PWD}/output

script.files = $${DESTDIR}/tsend
script.CONFIG += \
	nostrip \
	no_check_exist \
	executable

script.extra += \
	$(SED) -e \"s:@VERSION@:$${VERSION}:\" $${PWD}/tsend > $${script.files}

isEmpty(INSTALL_BIN_DIR):script.path = /usr/local/bin
else:script.path = $${INSTALL_BIN_DIR}

INSTALLS += \
	script

bashcomp.files = $${PWD}/bash-completion/tsend
bashcop.CONFIG += \
	nostrip

isEmpty(INSTALL_BASHCOMP_DIR):bashcomp.path = /etc/bash_completion.d
else:bashcomp.path = $${INSTALL_BASHCOMP_DIR}

INSTALLS += \
	bashcomp
