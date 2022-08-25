import itertools as it

import multiprocessing as mp
from abc import ABC, abstractmethod
import numpy as np

class Tessellation:

	def __init__( self, pattern = None ):

		pass

def cycler( iterable ):

	length = len( iterable )

	indexCycle = it.cycle( range( length ) )

	stringIter = np.array( [ str(x) for x in iterable ] )

	cycleString = ' "{" + "},".join( stringIter ) + " = {" + stringIter[ {n} : ] + stringIter[ 0 ] + stringIter[ -1 : ] '

	return ( exec( "{x}, {y} = {y}, {x}".format(  ) )x for x in  )

#######################################################################