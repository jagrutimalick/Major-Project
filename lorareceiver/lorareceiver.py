import spidev
import RPi.GPIO as GPIO
from SX127x.LoRa import *
from SX127x.board_config import BOARD

class Receiver(LoRa):
    def __init__(self, verbose=False):
        super(Receiver, self).__init__(verbose)
        self.set_mode(MODE.STDBY)

    def start_receive(self):
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)

    def on_rx_done(self):
        self.clear_irq_flags(RxDone=1)
       	payload = self.read_payload(nocheck=True)
        integer_list = []
        for byte in bytes(payload):
           integer_list.append(byte)
        print("Received:", integer_list)

BOARD.setup()
receiver = Receiver()
receiver.set_mode(MODE.STDBY)
receiver.set_pa_config(pa_select=1)

receiver.start_receive()

while True:
    pass

