from cobjects import CBuffer, CObject, CField


class MyObj(CObject):
    _typeid=3
    a=CField(0,'integer',default=3)
    b=CField(1,'real',default=3.0)
    c=CField(2,'real',length=4,default=1.1)
    d=CField(3,'real',length=4,default=1.2,pointer=True)
    e=CField(4,'real',length=2,default=1.3,pointer=True)

def test_flat_object():
    obj=MyObj()
    obj.a=2
    obj.b=3.5
    obj.c[2]=1.5
    obj.d=2
    obj.e=[3,4]
    assert(obj.a==2)
    assert(obj.b==3.5)
    assert(obj.c[2]==1.5)
    assert(obj.e[0]==3)
    assert(obj.e[1]==4)
    assert(obj.e[1]==4)
    return obj



