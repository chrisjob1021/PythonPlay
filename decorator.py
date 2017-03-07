
import time

def time_elapsed(func, *args, **kwargs):
	def wrapper(*args, **kwargs):
		start_time = time.time()
		func(*args, **kwargs)
		print args
		print kwargs
		end_time = time.time()
		return "%s ran in %dms" % (str(func), int(round((end_time - start_time) * 1000)))
	return wrapper

@time_elapsed
def test(x, y, tt="s"):
	time.sleep(2)
	return x, y, tt

print test(2, 3, tt="ms")