###############################################################################
# This file implements the algorithm for generating PU on-off pattern on the timescale of seconds
# proposed in
#   Modeling and Simulation of Time-Correlation Properties of Spectrum Use in Cognitive Radio
#   by Miguel López-Benítez and Fernando Casadevall
#   Available at: https://www.researchgate.net/publication/224259687_Modeling_and_Simulation_of_Time-Correlation_Properties_of_Spectrum_Use_in_Cognitive_Radio
###############################################################################

import numpy as np
from Params import Params

def gen_pu_pattern(**kwarg):
  
  # parameter
  params = Params(
   # parameters for the idle period distribution (generalized Pareto)
   loc_idle = ,     # location
   scale_idle = ,   # scale
   shape_idle = ,   # shape
   # parameters for the idle period distribution (generalized Pareto)    
   loc_busy = ,     # location
   scale_busy = ,   # scale
   shape_busy = ,   # shape
  )
