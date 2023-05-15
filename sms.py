import time
import serial
import RPi.GPIO as GPIO

# Instancia de clase con tres pasos 
class EnviarSMS:
    def __init__(self, phone_number = "+527773008850", message = "Alerta!"):
        self.phone_number = phone_number
        self.message = message
        
    def start_connection(self):
        self.start_phone_connection = serial.Serial("/dev/ttyS0", 115200, timeout=1)
        
    def send_sms(self):
        try:
            time.sleep(0.5)
            self.start_phone_connection.write(b'ATZ\r')
            time.sleep(0.5)
            self.start_phone_connection.write(b'AT+CMGF=1\r')
            time.sleep(0.5)
            self.start_phone_connection.write(b'AT+CMGS="' + self.phone_number.encode() + b'"\r')
            time.sleep(0.5)
            self.start_phone_connection.write(self.message.encode() + b"\r")
            time.sleep(0.5)
            self.start_phone_connection.write(bytes([26]))
            time.sleep(0.5)
        finally:
            self.start_phone_connection.close()

# Declarando la clase con los valores por defecto
sms = EnviarSMS()
sms.start_connection()
sms.send_sms()

# sms1 = EnviarSMS("+52 56302561", "Se movio el pir 2")
# sms1.start_connection()
# sms1.send_sms()
