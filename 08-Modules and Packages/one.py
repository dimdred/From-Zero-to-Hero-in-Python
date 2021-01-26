#one.py

def func():
	print('FUNC() IN ONE.PY')

print('TOP LEVEL IN ONE.PY')

def func1():
	pass

def func2():
	pass

if __name__ == "__main__":
	print('ONE.PY IS BEING RUN DIRECTLY!')
	# run the script!
	func1()
	func2()
else:
	print('ONE.PY HAS BEEN IMPORTED!')