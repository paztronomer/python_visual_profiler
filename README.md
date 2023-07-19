# Notes

- use already available tools as much as possible
- what do other solutions uses? 
    - py-spy: written in Rust, based on a Ruby profiler, https://github.com/benfred/py-spy
- using `time` command insidwe the container and then pipe out 

## cProfile AND pstats
**Extensive, whole code. Results can be analysed/visualised with pstats/snakeviz/others**
- can be called form CLI
- can analyse specific module of a library (would it work for a method in a script?)
- check output could be formatted to a JSON
- pstats gives urther information on the stats, calls to/from other functions (`pstat.print_callees()`, `pstat.print_callers()`)
- call from CLI `python -m cProfile [-o output_file] [-s sort_order] (-m module | myscript.py)` See [documentation here](https://docs.python.org/3/library/profile.html)

### SnakeViz
For visualization of cProfiling

## line_profiler
This is a more focused tool, to be used after we get first assessment from `cProfile`. [See repo here](https://github.com/pyutils/line_profiler)

## What is not particularly useful for our case
- `functools.wraps` print-like hardcoded decorators.  

# Articles, official documentation
- [x] Python profiling blog `alexisalulema.com`:
    - part 1: https://alexisalulema.com/2022/07/17/python-tips-time-profiling/
    - part 2: https://alexisalulema.com/2022/07/24/python-tips-cprofile-and-line_profiler-tools/
    - part 3: https://alexisalulema.com/2022/08/07/python-profiling-memory-profiling-part-3-final/
- [x] Performance Python book
- [x] Python official documentation
- [x] PyPi packages
- [x] Docker official docs

# Instructions

1. Build the container from the same directory it's located. Note the created user
   has `sudo` permissions but isn't `root`
   ```pwsh
   docker build -t imw .
   ```
2. Call the run and deploy of the docker container directly from PowerShell Core.
   ```pwsh
   docker run -it -p 8888:8888 -p 8080:8080 -v ${PWD}:/home/{usernameInsideContainer} --rm imw
   ```
3. Inside the container run
   ```pwsh
   jupyter-lab --ip 0.0.0.0 --no-browser --port=8080
   ```
   This call allows to see the Jupyter Lab to be seen from outside the container. 
   And on the local machine, go to `localhost:8888` and input the token generated
   by running Jupyter. Or simply used the suggested call from `jupyter-lab`:
   `http://127.0.0.1:{port}/lab?token={tokenHere}`. If no port is selected, then the 
   `8888` is used.
4. To connect to the running container from another terminal session
   ```
   docker exec -it {containerID} /bin/bash
   ```
4. Activate viens
   ```
   source imw_venv/bin/activate
   ```
5. To install packages within an enviroonment use
   ```
   python3 -m pip install 'packageName==2.18.4'
   python3 -m pip install packageName
   ```

In a nutshell
```pwsh
docker build -t imw .
docker run -it -p 8888:8888 -p 8080:8080 -v ${PWD}:/home/fpaz --rm imw

jupyter-lab --ip 0.0.0.0 --no-browser --port=8080
# got to localhost:8080/lab?token={tokenHere}

docker ps
docker exec -it {containerID} /bin/bash

source source/deploy_venv.sh

# profile time and memory: MSTL 
python3.11 -m cProfile -o mstl_decomposition.prof mstl_decomposition.py

# display snakeviz
snakeviz -H 0.0.0.0 -p 8888 -s mstl_decomposition.prof

# profile time and memory: time-series demo
python3.9 -m cProfile -o mstl_decomposition.prof mstl_decomposition.py


```
------------------------------------------------------------------------

# DEV Notes

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


# Achieved steps

- [x] Create Dockerfile to build a container for development
- [x] deploy the container locally
- [ ] deploy the container on a kubernetes cluster - harpoon
- [x] Get some example scripts
- [x] Toy model for: cProfiling
- [x] Toy model for: memTrace
- [x] understand what the output form snakeviz means
- [ ] test why creating venv with requeriments file dindn't install deps
