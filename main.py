# Bitcoin mining with 15 lines of python code | Python Bitcoin Tutorial

from hashlib import sha256
# print(sha256("ABC".encode("ascii")))
# print(sha256('ABC'.encode('ascii')).hexdigest())
max_nonce=10000000
def SHA256(text):
    return sha256(text.encode('ascii')).hexdigest()


def mine(block_number,transactions,previous_hash,prefix_zeros):
    prfix_str='0'*prefix_zeros
    for nonce in range(max_nonce):
        text=str(block_number)+transactions+previous_hash+str(nonce)
        new_hash=SHA256(text)
        if new_hash.startswith(prfix_str):
            print(f"yay! successfully mined bitcones with nonce value:{nonce}")
            return new_hash
    raise BaseException(f"Couldn't find correct has after trying {max_nonce} times")


if __name__ == '__main__':
    transactions='''
    Dhaval->Bhavin->20,
    Mando->Cara->45
    '''
    difficulty=6
    import time
    start=time.time()
    print('start mining:')
    new_hash=mine(5,transactions,
                  '0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7',
                  difficulty)

    totai_time=str((time.time()-start))
    print(f"end mining.mining took: {totai_time} seconds")
    print(new_hash)
