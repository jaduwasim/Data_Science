'''
Creation array(ndarray) by using python array module
'''
import array
a = array.array('i', [1,2,3,4])

print(__doc__)
print(a)
print(f'Type of a: {type(a)}')
for i in a:
	print(i)
