FROM arm32v7/python

# set working directory
WORKDIR /code

# copy all files from the current working directory into the container
COPY ./code .

# RUN apt-get update
# RUN pip install --upgrade pip

# for using the GPIO ports on the RaspberryPi
# RUN pip install --no-cache-dir rpi.gpio
# install python packages from requirements.txt
RUN pip install -r requirements.txt

# run the script
CMD ["python", "script.py"]
