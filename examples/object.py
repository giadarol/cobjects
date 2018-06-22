from cobjects import CBuffer, CObject, CField

class MyObj(CObject):
    _typeid=3
    a=CField(0,'integer',default=3)
    b=CField(1,'real',default=3.0)
    c=CField(2,'real',length=4,default=1.2)


obj=MyObj()
obj.a==3
obj.b==3.0
obj.c[2]==1.2


