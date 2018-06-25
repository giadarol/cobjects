from cobjects import CBuffer, CObject, CField

class MyObj(CObject):
    _typeid=3
    a=CField(0,'integer',default=3)
    b=CField(1,'real',default=3.0)
    c=CField(2,'real',length=4,default=1.1)
    d=CField(3,'int8',length=4,default=1.2,pointer=True)
    e=CField(4,'real',length=2,default=1.3,pointer=True)


obj=MyObj()
print(obj)
obj._buffer.info()

obj.a=2
obj.b=3.5
obj.c[2]=1.5
obj.d=2
obj.e=[3,4]
print(obj)


b=CBuffer()
obj1=MyObj(cbuffer=b)
obj2=MyObj(cbuffer=b)
obj2.e=[3,4]
print(obj1)
print(obj2)


