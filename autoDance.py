import os
import time
import asyncio
from deploy.python.ad_infer import Predictor
from airtest.core import api as air

def getScreen() -> None:
    air.snapshot("screen.jpg")

async def tap(wt: float, x: int, y: int) -> None:
    #tsk.add((x, y))
    print("click: %d, %d  after %f" % (x, y, wt))
    #await asyncio.sleep(wt)
    #os.system("adb shell input tap %d %d &" % (x, y))
    air.touch((x, y))
    #tsk.remove((x,y))

def getWait(w: float) -> float:
    #return 0
    return max(0, (w-cenD)/rat-(time.time() - ori))

def near(x1: int, x2: int) -> bool:
    return abs(x1 - x2) < 200

async def main() -> None:
    #while True:
    #    await tap(0, 300, 300)
    #    input()
    #global ori
    pre = Predictor()
    loop = asyncio.get_running_loop()
    while True:
        #ori = time.time()
        getScreen()
        #tm = time.time()
        fut = loop.run_in_executor(None, pre.work)
        res = await fut
        #print(time.time() - tm)
        '''
        '''
        for box in res:
            if round(box[0]) != 1:
                continue
            ctr_x = round((box[2] + box[4]) / 100) * 50
            ctr_y = round((box[3] + box[5]) / 100) * 50
            if (ctr_x, ctr_y) in tsk:
                continue
            if len(tsk) > 3:
                tsk.clear()
            tsk.add((ctr_x, ctr_y))
            air.touch((ctr_x,ctr_y))
            #await tap(0, ctr_x, ctr_y)
            '''
            #os.system("adb shell input tap %d %d &" % (ctr_x, ctr_y))
            #wt = getWait(box[4] - box[2])
            #asyncio.create_task(tap(wt, ctr_x, ctr_y))
            for x, y in tsk:
                if near(x, ctr_x) and near(y, ctr_y):
                    break
            else:
                #os.system("cp screen.jpg temp/%d,%d,%f.png" % (ctr_x, ctr_y, wt))
                if len(tsk) > 3:
                    tsk.clear()
                tsk.add((ctr_x, ctr_y))
                tap(0, ctr_x, ctr_y)
                #os.system("sleep 0.05 && adb shell input tap %d %d &" % (ctr_x, ctr_y))
                #print("click: %d, %d  after %f" % (ctr_x, ctr_y, wt))
                #asyncio.create_task(tap(wt, ctr_x, ctr_y))
            '''
            

air.init_device("Android")
cenD = 243
#rat = 251
rat = 365
ori = float()
tsk = set()
asyncio.run(main())