from .cbuffer import CBuffer
from .cfield import CField


class CObject(object):
    @classmethod
    def get_fields(cls):
        for nn, vv in cls.__dict__.items():
            if isinstance(vv, CField):
                yield nn, vv

    @classmethod
    def get_itemsize(cls, nargs):
        for name, field in self._fields():
            ftype = self._buffer.resolve_type(field.ftype)
            length = field.get_length(nargs)
            self._flength.append(length)

    def _fields(self):
        return self.__class__.get_fields()

    def __init__(self, cbuffer=None, _offset=None, _size=None, **nargs):
        if cbuffer is None:
            cbuffer = CBuffer(template=CBuffer.c_types)
        self._buffer = cbuffer
        self._build_from_args(nargs, _offset, _size)

    def _build_from_args(self, nargs, offset=None, size=None):
        self._offsets = []
        self._ftypes = []
        self._fsizes = []
        self._fnames = []
        self._flength = []
        self._fconst = []
        curr_size = 0
        new_object = True
        if offset is not None:
            curr_offset = offset
            new_object = False
            self._offset = offset
            self._size = size
        else:
            curr_offset = 0
        curr_pointers = 0
        pointer_list = []
        # first pass for normal fields
        for name, field in self._fields():
            ftype = self._buffer.resolve_type(field.ftype)
            length = field.get_length(nargs)
            self._flength.append(length)
            size = field.get_size(ftype, curr_offset, nargs)
            self._fconst.append(False)
            self._fnames.append(name)
            self._ftypes.append(ftype)
            self._fsizes.append(size)
            if field.pointer is False:
                if field.alignment is not None:
                    pad = field.alignment-curr_offset % field.alignment
                    pad = pad % field.alignment
                    curr_size += pad
                    curr_offset += pad
                self._offsets.append(curr_offset)
                pad = (8-size % 8) % 8
                curr_offset += size+pad
                curr_size += size+pad
            else:  # is pointer
                self._offsets.append(curr_offset)
                pointer_list.append(curr_offset)
                curr_offset += 8
                curr_size += 8
            if new_object is False:
                if field.const is True:
                    nargs[name] = getattr(self, name)
        # second pass for pointer fields
        pointer_data = []
        for name, field in self._fields():
            if field.pointer is True:
                if field.alignment is not None:
                    pad = field.alignment-curr_offset % field.alignment
                    pad = pad % field.alignment
                    curr_size += pad
                    curr_offset += pad
                offset = self._offsets[field.index]
                pointer_data.append([offset, curr_offset])
                self._offsets[field.index] = curr_offset
                size = self._fsizes[field.index]
                curr_size += size
                curr_offset += size
        if new_object is True:
            # allocate data
            _address = self._buffer.new_object(curr_size,
                                               self.__class__,
                                               pointer_list)
            self._offset = self._buffer.address_to_offset(_address)
            self._size = curr_size
            for index in range(len(self._offsets)):
                self._offsets[index] += self._offset
            # store pointer data
            for offset, address in pointer_data:
                doffset = offset+self._offset
                self._buffer.set_field(_address+address, doffset, 'int64', 8)
            # store data in fields
            for name, field in self._fields():
                setattr(self, name, nargs.get(name, field.default))
                if field.const is True:
                    self._const[field.index] = True

    def __repr__(self):
        out = [f"<{self.__class__.__name__} at {self._offset}"]
        for nn, ff in self._fields():
            out.append(f"  {nn}:{getattr(self,nn)}")
        out.append(">")
        return "\n".join(out)

