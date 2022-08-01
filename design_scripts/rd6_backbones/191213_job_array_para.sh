#!/bin/bash
parallel -j 4 -N 1 --joblog joblog 'rosetta_scripts.static.linuxgccrelease -parser:protocol 191205_make_bbs_constraint.xml -in:file:s start{}.pdb -nstruct 100 -parser:script_vars rg_weight=1.0 constraint_file_name=ConstraintFile_atompair_sw blueprint_file_name=heeh_{}.bp use_abego_bias=True ss_file_name=heeh_{}.bp.ss ss_threshold=0.9' ::: 11 12 13 14
