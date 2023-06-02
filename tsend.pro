
TEMPLATE = aux

script.files = $${PWD}/tsend
script.CONFIG += \
	nostrip

isEmpty($$list($$(NITABIN))):script.path = /usr/local/bin
else:script.path = $$(NITABIN)

INSTALLS += \
	script
