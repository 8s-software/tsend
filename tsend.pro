
TEMPLATE = aux
VERSION = 0.2.0

isEmpty(DESTDIR):DESTDIR = .

isEmpty(INSTALL_PREFIX):INSTALL_PREFIX = /usr/local

system(pkg-config --exists bash-completion):\
	COMPLETIONS_DIR = $$system(pkg-config --variable=completionsdir bash-completion)
else:COMPLETIONS_DIR = /etc/bash_completion.d

INSTALLS += \
	completion \
	script

script.files = $${DESTDIR}/tsend
script.path = $${INSTALL_PREFIX}/bin
script.CONFIG += \
	nostrip \
	no_check_exist \
	executable

script.extra += cp -f $${PWD}/scripts/tsend $${script.files}
script.extra +=	$$escape_expand(\\n\\t)$(SED) -e \"s:@VERSION@:$${VERSION}:\" -i $${script.files}

completion.files = $${PWD}/bash-completion/tsend
completion.path = $${COMPLETIONS_DIR}
completion.CONFIG += \
	nostrip
