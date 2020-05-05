import pymem

def write_color( process_handle, address, colors:list ):
    offset = 0x0
    for color in colors:
            pymem.memory.write_float( process_handle, address + offset, float(color) )
            offset += 0x4

def write_vector( process_handle, address, angles:list ):
    offset = 0x0
    for angle in angles:
            pymem.memory.write_float( process_handle, address + offset, float(angle) )
            offset += 0x4

def read_vector( process_handle, address ):
    offset = 0x0
    return_angle = [ 0, 0, 0 ]

    for i in range( 0, 3 ):
        return_angle[ i ] = pymem.memory.read_float( process_handle, address + offset )
        offset += 0x4

    return return_angle