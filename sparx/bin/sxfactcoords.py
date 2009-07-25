#!/usr/bin/env python

import global_def
from global_def import *
from optparse import OptionParser
from EMAN2_cppwrap import *

import os
import sys

      
def main():
	progname = os.path.basename(sys.argv[0])
	usage = progname + " prj_stack .. average eigvol output_factcoords --rad=radius --neigvol=number_of_eigvol --of=output_format"
	parser = OptionParser(usage, version=SPARXVERSION)
	parser.add_option("--rad",       type="int",    default=-1, help="radius of mask")
	parser.add_option("--neigvol",   type="int",    default=-1, help="number of eigvenvectors to use (default all)")
	parser.add_option("--of",        type="string", default="hdf", help="output format: hdf or txt (default is hdf)")
	parser.add_option("--MPI",       action="store_true", help="flag for MPI version")

	(options, args) = parser.parse_args()

	if( len(args) < 4 ):
		print "usage: " + usage
		print "Please run '" + progname + " -h' for details"
	else:
		stacks = args[0:-3]
		avgvol = args[-3]
		eigvol = args[-2]
		output = args[-1]
		
		if options.rad < 0:
			print "Error: mask radius is not given"
			sys.exit(-1)
		if options.MPI:
			from mpi import mpi_init	
			sys.argv = mpi_init( len(sys.argv), sys.argv )

			from utilities import init_mpi_bdb
			init_mpi_bdb()

		from utilities import get_im
		global_def.BATCH = True
		nz = get_im( stacks[0]).get_zsize()
		if( nz == 1):
			from applications import factcoords_prj
			factcoords_prj(stacks, avgvol, eigvol, output, options.rad, options.neigvol, options.of, options.MPI)
		else:
			from applications import factcoords_vol
			factcoords_vol(stacks, avgvol, eigvol, output, options.rad, options.neigvol, options.of, options.MPI)
		global_def.BATCH = False
		

if __name__ == "__main__":
	main()
