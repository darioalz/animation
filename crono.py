from time import sleep
from chronometer import Chronometer

counter = 0
def long_running_task_that_can_fail():
    global counter
    counter += 1
    sleep(2.)
    return counter > 3

with Chronometer() as t:
    while not long_running_task_that_can_fail():
        print('Failed after {:.3f} seconds!'.format(t.reset()))
print('Success after {:.3f} seconds!'.format(float(t)))
