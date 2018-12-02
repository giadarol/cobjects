from cobjects import CBuffer, CObject, CField

class Obj1(CObject):
    _typeid = 3
    typeid_id=CField(0,'int64',default=_typeid)
    a        =CField(1,'real' ,default=1.1)
    b        =CField(2,'uint8',default=1)
    c        =CField(3,'real' ,default=1.3)

class Obj2(CObject):
    _typeid = 3
    typeid_id=CField(0,'int64',default=_typeid)
    obj      =CField(1,Obj1,length=10)

#obj1=Obj1()
obj2=Obj2()
#print(obj1)
#print(obj2)
