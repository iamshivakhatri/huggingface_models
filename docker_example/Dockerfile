# base image
FROM python:3.11



# specify working directory
WORKDIR /code

 

# copy package list
COPY ./requirements.txt /code/requirements.txt

# Install dependencies
RUN apt-get update && apt-get install -y \
    libhdf5-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for HDF5
ENV HDF5_DIR=/usr/lib/x86_64-linux-gnu/hdf5/serial
ENV LD_LIBRARY_PATH=$HDF5_DIR/lib:$LD_LIBRARY_PATH
ENV CFLAGS="-I$HDF5_DIR/include"
ENV LDFLAGS="-L$HDF5_DIR/lib"

# install packages
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy application code
COPY ./app /code/app

# copy pretrained models
COPY .cvlib /root/.cvlib

# expose port
EXPOSE 80

# run server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]