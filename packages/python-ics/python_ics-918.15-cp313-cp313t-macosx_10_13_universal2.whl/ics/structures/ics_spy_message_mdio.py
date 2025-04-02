# This file was auto generated; Do not modify, if you value your sanity!
import ctypes
import enum



class Nameless23244(ctypes.Structure):
    _fields_ = [
        ('RegAddr', ctypes.c_uint32, 16),
        ('PhyAddr', ctypes.c_uint32, 5),
        ('DevType', ctypes.c_uint32, 5),
        ('', ctypes.c_uint32, 6),
    ]



class Nameless35608(ctypes.Union):
    _anonymous_  = ('Nameless23244',)
    _fields_ = [
        ('ArbIDOrHeader', ctypes.c_uint32),
        ('Nameless23244', Nameless23244),
    ]



class Nameless20259(ctypes.Structure):
    _fields_ = [
        ('StatusBitField3', ctypes.c_uint32),
        ('StatusBitField4', ctypes.c_uint32),
    ]



class Nameless39357(ctypes.Union):
    _anonymous_  = ('Nameless20259',)
    _fields_ = [
        ('Nameless20259', Nameless20259),
        ('AckBytes', ctypes.c_uint8 * 8),
    ]



class ics_spy_message_mdio(ctypes.Structure):
    _anonymous_  = ('Nameless35608', 'Nameless39357')
    _fields_ = [
        ('StatusBitField', ctypes.c_uint32),
        ('StatusBitField2', ctypes.c_uint32),
        ('TimeHardware', ctypes.c_uint32),
        ('TimeHardware2', ctypes.c_uint32),
        ('TimeSystem', ctypes.c_uint32),
        ('TimeSystem2', ctypes.c_uint32),
        ('TimeStampHardwareID', ctypes.c_uint8),
        ('TimeStampSystemID', ctypes.c_uint8),
        ('NetworkID', ctypes.c_uint8),
        ('NodeID', ctypes.c_uint8),
        ('Protocol', ctypes.c_uint8),
        ('MessagePieceID', ctypes.c_uint8),
        ('ExtraDataPtrEnabled', ctypes.c_uint8),
        ('NumberBytesHeader', ctypes.c_uint8),
        ('NumberBytesData', ctypes.c_uint8),
        ('NetworkID2', ctypes.c_uint8),
        ('DescriptionID', ctypes.c_uint16),
        ('Nameless35608', Nameless35608),
        ('Data', ctypes.c_uint8 * 8),
        ('Nameless39357', Nameless39357),
        ('ExtraDataPtr', ctypes.c_void_p),
        ('MiscData', ctypes.c_uint8),
        ('Reserved', ctypes.c_uint8 * 3),
    ]


_icsSpyMessageMdio = ics_spy_message_mdio
icsSpyMessageMdio = ics_spy_message_mdio

