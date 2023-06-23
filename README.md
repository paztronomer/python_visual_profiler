<<<<<<< HEAD
# Notes

- use already available tools as much as possible
- what do other solutions uses? 
    - py-spy: written in Rust, based on a Ruby profiler, https://github.com/benfred/py-spy
- using `time` command insidwe the container and then pipe out 

## cProfile AND pstats
**Extensive, whole code. Results can be analysed/visualised with pstats/snakeviz/others**
- can be called form CLI
- can analyse specific module of a library (would it work for a method in a script?)
- output could be formatted to a JSON 
- pstats gives urther information on the stats, calls to/from other functions (`pstat.print_callees()`, `pstat.print_callers()`)

### SnakeViz
For visualization of cProgiling

## line_profiler
This is a more focused tool, to be used after we get first assessment from `cProfile`

## What is not particularly useful for our case
- `functools.wraps` print-like hardcoded decorartors.  

# Articles, official documentation
- [ ] Python profiling blog `alexisalulema.com`:
    - part 1: https://alexisalulema.com/2022/07/17/python-tips-time-profiling/
    - part 2: https://alexisalulema.com/2022/07/24/python-tips-cprofile-and-line_profiler-tools/
    - part 3: https://alexisalulema.com/2022/08/07/python-profiling-memory-profiling-part-3-final/
- [ ] Performance Python book

# Instructions

1. Call the run and deploy of the docker container directly from PowerShell Core.
   ```pwsh
   docker build -t imw .

   docker run -it -p 8888:8080 -v .:/app --rm imw
 
   ```
------------------------------------------------------------------------

# Achieved steps

- [x] Create Dockerfile to build a container for development
- [x] deploy the container locally
- [ ] deploy the container on a kubernetes cluster - harpoon
- [ ] Get some example scripts
- [ ] Toy model for: cProfiling
- [ ] Toy model for: memTrace
- [ ] 
