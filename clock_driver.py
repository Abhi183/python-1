"""
hw-12
checking functions
"""
from my_classes import clock
my_clock=clock()
#checking display function
print my_clock.display_time()
#checking tick function
"""my_clock.tick()
my_clock.tick()
my_clock.tick()
my_clock.tick()
print my_clock.display_time()"""
#checking tick function using loop
for i in range(1440):
    my_clock.tick()
print my_clock.display_time()    
#checking reset
my_clock.reset()
print my_clock.display_time()
