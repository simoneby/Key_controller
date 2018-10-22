#keypad

import RPi.GPIO as GPIO
import time
class Keypad:
    #skal tallene gis ut som streng eller tall?


    def __init__(self):

        self.pressed=None
        self.rowpins=[18,23,24,25]
        self.colpins=[17,27,22]
        self. dict={(18,17):1, (18,27):2, (18,22):3, (23,17):4, (23,27):5, (23,22):6, (24,17):7, (24,27):8, (24,22):9, (25,17):'*', (25,27):0, (25,22):'#'}


    def setup(self):
        GPIO.setmode(GPIO.BCM)
        for rp in self.rowpins:
            GPIO.setup(rp,GPIO.OUT)

        for cp in self.colpins:
            GPIO.setup(cp,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)



    def do_polling(self):
        val=False
        for r in self.rowpins:
            GPIO.output(r,GPIO.HIGH)
            for c in self.colpins:

                if GPIO.input(c) == GPIO.HIGH:
                    self.pressed=(r,c)

                    val= True

            GPIO.output(r,GPIO.LOW)
        return val


#må legge inn sikkerhet for å unngå flere signaler her, eller må man det?
    def get_next_signal(self):
        x=0
        while True:
            if self.do_polling():
                time.sleep(0.001)
                x+=1
            else:
                x=0

            if x==90:
                break




        self.get_symbol()



    def get_symbol(self):
        #self.returned()
        return self.dict[self.pressed]

    #def returned(self):
     #   return True




def main():
    keypad=Keypad()
    keypad.setup()
    keypad.get_next_signal()
    while keypad.get_symbol()!='*':
        keypad.get_next_signal()



if __name__ == "__main__":
    main()


