from cobjects import CBuffer, CObject, CField

class MyObj(CObject):
    _typeid=3
    a=CField(0,'integer',default=3)
    b=CField(1,'real',default=3.0)
    c=CField(2,'real',length=4)


obj=MyObj()
obj.a
obj.b
obj.c

b=CBuffer()
b.info()

b.new_object(24,2,[])
b.info()
obj=b.get_object_buffer(0).view('uint64')
obj[0]=31

b.reallocate(100,100,100,100)
b.info()

b._test_cffilib()

