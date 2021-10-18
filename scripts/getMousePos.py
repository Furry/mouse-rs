from ctypes import windll, Structure, c_long, byref
import time
import json

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]



def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}

iterations = 20
frequency = 30
seconds = 1

data = []
iter_count = 0
while True:
    print("Starting in 2 seconds...")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("go")

    iter_count = iter_count + 1
    # Loop 30 times a second
    cache = []
    while True:
        # Poll at a frequency of 30 times a second
        time.sleep(1 / frequency)
        pos = queryMousePosition()
        cache.append(pos)
        if len(cache) > frequency * seconds:
            break
        #END
    #END
    
    data.append(cache)
    cache = []

    if (iterations > 0):
        if (iter_count >= iterations):
            with open("mousePos.json", "w") as f:
                json.dump(data, f)
                f.write("\n")
            #END
            break
        #END
    #END
#END

pos = queryMousePosition()
print(pos)