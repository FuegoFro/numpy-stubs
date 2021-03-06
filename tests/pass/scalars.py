import numpy as np


# Construction
class C:
    def __complex__(self):
        return 3j


class A:
    def __float__(self):
        return 4


np.complex32(3)
np.complex64(3j)
np.complex64(C())

np.int8(4)
np.int16(3.4)
np.int32(4)
np.int64(-1)
np.uint8(A())
np.uint32()

np.float16(A())
np.float32(16)
np.float64(3.0)

np.bytes_(b"hello")
np.str_("hello")

# Protocols
float(np.int8(4))
int(np.int16(5))
np.int8(np.float32(6))

# TODO(alan): test after https://github.com/python/typeshed/pull/2004
# complex(np.int32(8))

abs(np.int8(4))

# Array-ish semantics
np.int8().real
np.int16().imag
np.int32().data
np.int64().flags

np.uint8().itemsize * 2
np.uint16().ndim + 1
np.uint32().strides
np.uint64().shape
