#!/usr/bin/env bash
BIN=/C/synopsys/Hspice_C-2009.03-SP1/BIN
$BIN/hspice.exe output.sp && $BIN/awaves output.sp
