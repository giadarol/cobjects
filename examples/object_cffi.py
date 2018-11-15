from cobjects import CBuffer, CObject, CField

class MyObj(CObject):
    _typeid = 3
    typeid_id=CField(0,'int64',default=_typeid)
    a=CField(1,'int32',default=3)
    b=CField(2,'real',default=3.0)
    c=CField(3,'real',length=4,default=1.1)
    d=CField(4,'uint8',length=4,default=1,pointer=True)
    e=CField(5,'real',length=2,default=1.3,pointer=True)

obj=MyObj()
print(obj)
obj._buffer.info()

obj.a=2
obj.b=3.5
obj.c[2]=1.5
obj.d=2
obj.e=[3,4]
print(obj)

print(obj._to_cdebug())
ffi,lib,cobj=obj._cdebug()
