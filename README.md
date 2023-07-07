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

   docker run -it -p 8888:8888 -v ${PWD}:/home/{username} --rm imw
   ```
1. Inside the container run
   ```pwsh
   jupyter-lab --ip 0.0.0.0 --no-browser
   ```
   This call allows to see the Jupyter Lab to be seen from outside the container. 
   And on the local machine, go to `localhost:8888` and input the token generated
   by running Jupyter. Or simply used the suggested call from `jupyter-lab`:
   `http://127.0.0.1:8888/lab?token={tokenHere}`
1. To connect to the running container from another terminal session
   ```
   docker exec -it {containerID} /bin/bash
   ```
------------------------------------------------------------------------

# DEV Notes
The pipeline.py just has functions, I need a script that actually does something
Seems like I'll neeed to use some script from astronomy.

To generate a profile output from the CLI, use 
`python3.11 -m cProfile -s cumulative -o test_pipeline.prof test_pipeline.py`
And then call snakevix from CLI with
`snakeviz -H 0.0.0.0 -p 8888 -s test_pipeline.prof`
and visualise in the browser on the local machine using 
`http://localhost:{exposedPort:8888}/snakeviz/{path}` as in
`http://localhost:8888/snakeviz/%2Fhome%2Ffpaz%2Fheader_to_json.prof`
Make sure to use `localhost`, as otherwise you won't be able to mirror
the process running in the container. Also, if you're running Jupyter
or other app that uses an open port, you may need to expose a second 
port when running the container, so you'll have a open connection available
(otherwise snakeviz won't show on the outside)

Can use the pro from header to json. Just know how to ectract the info.

Packages to add
- scipy
- matplotlib
- astropy


# Achieved steps

- [x] Create Dockerfile to build a container for development
- [x] deploy the container locally
- [ ] deploy the container on a kubernetes cluster - harpoon
- [ ] Get some example scripts
- [ ] Toy model for: cProfiling
- [ ] Toy model for: memTrace
- [ ] understand what the output form snakeviz means
- [ ] test with a code easy to run with mock arguments
- [ ] run venv with requirements_venv.txt
