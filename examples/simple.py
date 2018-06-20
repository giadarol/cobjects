from cobjects import CBuffer

b=CBuffer()
b.info()

b.new_object(24,2,[])
b.info()
obj=b.get_object_buffer(0).view('uint64')
obj[0]=31

b.reallocate(100,100,100,100)
b.info()
