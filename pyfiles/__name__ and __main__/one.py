#one.py

def func():
	print('func() in one.py')

print('Top level in one.py')

if __name__ == '__main__':
	print('One.py is being run direclty.')
else:
	print('One.py has been imported.')