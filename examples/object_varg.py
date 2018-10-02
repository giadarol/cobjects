from cobjects import CBuffer, CObject, CField

class MyObj(CObject):
    _typeid = 3
    typeid_id=CField(0,'int64',default=_typeid)
    length   =CField(1,'int32',default=10,const=True)
    c        =CField(2,'real' ,length='length',default=1.1)
    d        =CField(3,'uint8',length='2*length+10',default=1,pointer=True)
    e        =CField(4,'real' ,length='length',default=1.3,pointer=True)


obj=MyObj(length=2)
print(obj)
