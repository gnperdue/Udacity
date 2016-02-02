# TensorFlow

Fork and clone a copy of the main TensorFlow repo - our class notebooks are
there.

## Starting up a Docker container

Assuming we have created a "docker machine" named `default`:

    docker-machine start default
    eval "$(docker-machine env default)"
    docker-machine stop default    # to halt

## Working with Docker

### Run for IPython NB

    docker run -it -v "$PWD":/notmnist -p 5000:8888 b.gcr.io/tensorflow/tensorflow:latest-devel

This sets up a directory mount ("`$PWD`" as `/notmnist` on the container) and maps
the internal port 8888 to the host port of 5000. We can get the host port with:

    docker-machine url default

Or,

    $ docker-machine url default | perl -ne '@l=split(":");print split("/",@l[1]);print "\n";'
    192.168.99.100

We can navigate to this IP and use the host port set above (e.g. 5000) to use
IPython Notebook (or `tensorboard`, below). Then, go to the `/notmnist` directory
on the docker host. Next, run `ipython notebook` at the docker host prompt, then
go to, e.g. `192.168.99.100:5000` if we chose port 5000 above, etc.

### TensorBoard

    tensorboard --logdir=. --port=8888  # use the port we set to face outwards

Then, naviagate to the URL from `docker-machine url default` (or whatever the
machine name is) and set the port to `:5000` (or whatever we mapped the container
port to).
