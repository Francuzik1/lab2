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
        (self.internal[self.word_hash]).pop(0)
        return ''.join(self.internal[self.word_hash])