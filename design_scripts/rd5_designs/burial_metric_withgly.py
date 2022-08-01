#!/usr/local/bin/python
import Bio.PDB
from numpy import *
from Bio.PDB import *
import sys
import os

def vtoa(v):
    return array([float(x) for x in v])

def unit(v):
    return v / (dot(v,v)**0.5)

def norm(v):
    return dot(v,v) ** 0.5

def analyze_pdb(file_loc):

        #name=file_loc.split('/')[-1]
    if not os.path.isfile('%s.burial' % file_loc):
        d_param = 9

        structure = Bio.PDB.PDBParser(QUIET=True).get_structure(file_loc,file_loc)
        residues = [res for res in structure.get_residues()]

        outfile = open(file_loc + '.burial','w')
        print(str(file_loc))
        for i, res in enumerate(residues):
            burial = 0.0
            #print vec_sum
            #if res.get_resname() != 'GLY':
                ########
                # script as currently written ignores glycines.  however, if glycines have explicit hydrogens
                # (as they do in rosetta files), then the script can be made to analyze glycines, by uncommenting
                # the code below and getting rid of the current "if" clause above that ignores glycines
                #
            if res.get_resname() == 'GLY':
                start = res['CA']
            else:
                start = res['CB']
                #
                #######
            #start = res['CB']
            my_cb_vector = unit(vtoa(start.get_vector() - res['CA'].get_vector()))
            
            for j, res2 in enumerate(residues):
                if res2 != res:
                    #print res2
                    to_res2 = vtoa(res2['CA'].get_vector() - start.get_vector())
                    dist_term = 1.0 / (1.0 + (exp(norm(to_res2) - d_param)))
                    angle_term = (0.5 + dot(unit(to_res2), my_cb_vector))
                    if angle_term < 0: angle_term = 0
                    angle_term = angle_term ** 2.0

                    burial += dist_term * angle_term / 2.25

            print(res, start, my_cb_vector, burial)        
            outfile.write('%s\t%s\t%s\n' % (i+1, res.get_resname(), burial))
        outfile.close()

            #print i+1, dot(vec_sum,vec_sum)**0.5
                    #vecs.append((res2['CA']-start, r/(res2['CA']-start)))

        #print vecs
        #sys.exit(0)


for i in sys.argv[1:]:
    analyze_pdb(i)


