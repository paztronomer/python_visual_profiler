""" 
Simple script to do the profiling of Python codes

Usage:
    Load your module (in this case is aps_utils_CASU) and know which
    function you want to profile. If you want to get the assessment
    from the __name__ == "call", then create a funtion holding all the 
    calls. Use the latter for the call of cProfile.run()

Additional information:
    https://docs.python.org/3/library/profile.html

CLI call
python3 -m cProfile -s cumulative script.py

"""

import cProfile
import pstats
from pstats import SortKey
# Import your module of interest
import aps_utils_CASU

# Define which funtion of your module you want to profile. Call it by
# simply replacing the below string with <your_module>.<function_name>
target_prof = "aps_utils_CASU.main()"

# Define the output file where the profiler will dump the information. 
# Note this is a binary file.
out_stats = "restats"

# Run the profiler 
cProfile.run(target_prof, out_stats)

# Reads the binary file the profiler just generated and formats it by
# - strip_dirs(): removing extraneous path from all modules
# - sort_stats(<argument>): sort the output by some desired statistics. 
#   See https://docs.python.org/3/library/profile.html#pstats.Stats.sort_stats
# - print_stats(<optional N>): if a positive integer is given, then 
#   just print  
p = pstats.Stats(out_stats).strip_dirs()
n_print = 20

# Sort by time
p.sort_stats(SortKey.TIME).print_stats(n_print)

# Sort by number of calls, using string
p.sort_stats("ncalls").print_stats(n_print)

# Sort by cumulative calls
p.sort_stats(SortKey.CUMULATIVE).print_stats(n_print)