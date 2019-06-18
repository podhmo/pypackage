readme: NAME ?= foo
readme: PKG ?= gh:podhmo/pypackage
readme:
	rm -rf ${NAME}
	echo '{"name": "${NAME}", "pkg": "${PKG}"}' | kamidana -i json -a reader misc/README.md.j2 | tee README.md

readme-dev:
	$(MAKE) readme PKG=.

.PHONY: readme readme-dev
