import zlib


class Adapter:
    internal = [i for i in range(1000)]

    def __init__(self, key, value):
        self.key = key
        self.b_key = bytes(self.key, 'utf-8')
        self.value = value
        self.hash_total = zlib.crc32(self.b_key) % 1000
        self.internal[self.hash_total] = [key, value]

    def for_printer(self, key_word):
        self.b_word = bytes(key_word, 'utf-8')
        self.word_hash = zlib.crc32(self.b_word) % 1000
        riter = (self.internal[self.word_hash])
        return riter[1]

    def deliter(self, del_key):
        self.del_key =del_key
        self.b_del = bytes(self.del_key, 'utf-8')
        self.num_b = zlib.crc32(self.b_del) % 1000
        self.internal[self.num_b] = None
