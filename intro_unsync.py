import time
from unsync import unsync


@unsync
def my_function():
    """ A function which we want to use asynchronously """
    time.sleep(1)
    return "something fascinating"


# Calling the decorated function starts the coroutine running
# and returns an unsync Unfuture object, NOT the return value (yet)

thing = my_function()
print(thing)
# -> <unsync.unsync.Unfuture object at 0x106f87b90>


# To wait for the coroutine to finish and get at the return value
# use the .result() method on this Unfuture object

print(thing.result())
# -> something fascinating
