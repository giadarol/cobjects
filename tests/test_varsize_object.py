from cobjects import CBuffer, CObject, CField


class MyObj(CObject):
    _typeid=3
    a=CField(0,'integer',const=True)
    b=CField(1,'real',length='a',default=1.1)
    c=CField(2,'real',length='2*a+1',default=1.2,pointer=True)

def test_access_object():
    obj=MyObj(a=2)
    obj.a=2
    obj.b=3.5
    obj.c[2]=1.5
    assert(obj.a==2)
    assert(obj.b[0]==3.5)
    assert(obj.c[2]==1.5)
    return obj

def test_init_object():
    obj=MyObj(a=2,b=8,c=[1,2,3,4,5])
    assert(obj.a==2)
    assert(obj.b[0]==8)
    assert(obj.c[2]==3)
    return obj


