import hashlib
import itertools

def mineAdventCoin(key, leading_zeroes):
    while True:
        zero_string = '0' * leading_zeroes
        for i in itertools.count():
            num = str(i).encode('utf-8')
            hash_num = key + num
            if hashlib.md5(hash_num).hexdigest()[:leading_zeroes] == zero_string:
                return i

secret_key = b'bgvyzdsv'
print(mineAdventCoin(secret_key, 5))
print(mineAdventCoin(secret_key, 6))