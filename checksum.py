import zlib

def message_checksum(message):
    text =zlib.crc32(message)
    return text

def encode_message(message):
    compressed=zlib.compress(message)
    return compressed
def decode_message(message):
    decompressed=zlib.decompress(message)
    return decompressed