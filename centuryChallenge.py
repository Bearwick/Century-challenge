import os
import time

def startCounter():
    for i in range(15,0, -1):
        print(i)
        time.sleep(1)

def shotPause():
    time.sleep(29)
    print(str(30) + " sek")
    time.sleep(5)
    print(str(25) + " sek")
    time.sleep(5)
    print(str(20) + " sek")
    time.sleep(5)
    print(str(15) + " sek")
    time.sleep(5)
    for i in range(10, 0, -1):
        print(str(i) + " sek")
        time.sleep(1)


def centuryCounter(i):
    for j in range(1, i+1):
        print("""
        +----------------------------+
        | Shot nr {0}! {1} shots igjen! |
        +----------------------------+
        """.format(str(j), str(i-j)))
        os.system("afplay " + "./dingdingding.mp3")
    
        if (j != i):
            shotPause()

def main(i):
    startCounter()
    centuryCounter(i)
    print("Finished! Congratulations!")
    


if __name__ == '__main__':
    main(100) #Choose playing minutes.