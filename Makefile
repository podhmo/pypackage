readme: NAME ?= foo
readme:
	rm -rf ${NAME}
	echo '{"name": "${NAME}"}' | kamidana -i json -a reader misc/README.md.j2 | tee README.md
	rm -rf ${NAME}
.PHONY:
