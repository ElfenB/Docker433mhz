FROM arm32v7/python

COPY scripts/led_blinker.py .
COPY scripts/requirements.txt .

# RUN apt-get update
RUN pip install --upgrade pip
RUN pip install --no-cache-dir rpi.gpio
RUN pip install -r requirements.txt

CMD ["python", "led_blinker.py"]
