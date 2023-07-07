
FROM ubuntu:22.04 AS base

ARG BUILD_DATE

LABEL imweek.developer="Francisco Paz - DART"
LABEL imweek.date=$BUILD_DATE

RUN apt-get update -y \
    && apt-get install -y \
    bash build-essential zlib1g-dev libncurses5-dev libgdbm-dev \
    libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev \
    wget libbz2-dev \
    nano sudo \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* 

# Get Python directly from source
WORKDIR /tmp
RUN wget https://www.python.org/ftp/python/3.11.3/Python-3.11.3.tgz \
    && tar -xf Python-3.11.3.tgz
WORKDIR /tmp/Python-3.11.3
# Set `make -j` to the number of cores you have, or leave it out for the default
# Set `--enable-optimizations` to enable optimizations
# Set `--prefix` to change the install location (default is `/usr/local`)
# Set `--with-ensurepip` to install pip
# Set `--with-venv` to install the `venv` module
RUN ./configure --enable-optimizations
RUN make -j 4 && make altinstall \
    && rm -rf /tmp/Python-3.11.3*

# Add a non-root user
ARG USER=fpaz
RUN useradd -m ${USER} \
    && usermod -aG sudo ${USER} \
    && echo "${USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
ARG USERNAME=user-name-goes-here
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ENV HOME /home/${USER}
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3.11 install --no-cache-dir --upgrade pip \
    && pip3.11 install --no-cache-dir -r requirements.txt

EXPOSE 8080
VOLUME /app
VOLUME /home/${USER}
WORKDIR /home/${USER}
USER ${USER}
CMD ["bash"]

# EXPOSE <port> [<port>/<protocol>...]
# VOLUMNE
# ENV PATH=/usr/local/nginx/bin:$PATH
# Only RUN, COPY, and ADD creates layers
