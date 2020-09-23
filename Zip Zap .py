import sys
b = ' '
try:
    while True:
        
        for i in range(0,4):
            s = i * b
            print(s + '*****')
        for d in range(4,0,-1):
            f = d * b
            print(f  + '*****')
except KeyboardInterrupt:
    sys.exit()