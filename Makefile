BIN=/C/synopsys/Hspice_C-2009.03-SP1/BIN

all: output.tr0
	${BIN}/awaves output.sp

output.tr0: output.sp
	${BIN}/hspice.exe output.sp

output.sp:
	python generate.py

.PHONY: clean
clean:
	git clean -Xdf
