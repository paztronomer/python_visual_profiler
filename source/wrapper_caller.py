"""
Wrapper to run the cProfiling CLI call over a function/script of interest
"""
import argparse
import subprocess
import shlex

# ToDo: 
# - logging of this wrapper 
# - export .prof to JSON

def get_args():
    """
    Retrieve arguments from CLI call to this script
    """
    txt = "Wrapper to run the cProfiling CLI call over a function/script of interest"
    arg = argparse.ArgumentParser(description=txt)
    arg.add_argument("target_prof", type=str, help="Script to profile")
    arg.add_argument("out_stats", type=str, help="Output file, .prof extension")
    arg.add_argument("-s", "--sort_by", type=str, default="cumulative", help="Sort by statistics. Default: cumulative")
    arg.add_argument("-f", "--function_name", type=str, default=None, help="Optional: Function to profile")
    arg.add_argument("-p", "--python_version", type=str, default="python3.11", help="Python executable. Default: python3.11")
    arg.add_argument("-a", "--args", type=str, default=None, help="Optional: Arguments to pass to the function/script. Enclose in quotes")
    return arg.parse_args()

def aux_main():
    """
    Simple auxilirary main to run the CLI call
    """
    # Get the arguments
    args = get_args()
    # Define the CLI call
    if args.function_name is None:
        cmd = f"{args.python_version} -m cProfile -o {args.out_stats} -s {args.sort_by} {args.target_prof}"
    else:
        cmd = f"{args.python_version} -m cProfile -o {args.out_stats} -s {args.sort_by} -m {args.function_name} {args.target_prof}"
    cmd = f"{args.python_version} -m cProfile -o {args.out_stats} -s {args.sort_by} {args.target_prof}"
    # Appending arguments
    if args.args is not None:
        cmd += f" {args.args}"
    # Run the CLI call
    subprocess.run(shlex.split(cmd))

if __name__ == "__main__":
    aux_main()
