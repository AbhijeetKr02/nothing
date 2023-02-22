import struct

i = int(input("enter data: "))

binary = struct.pack("i",i)

print(binary)

unbinary = struct.unpack("i", binary)[0]

print(unbinary)