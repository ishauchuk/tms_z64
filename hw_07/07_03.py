import json
import os
from hashlib import md5 as md

blockchain_dir = 'blockchain/'


def get_hash(prev_block):
    with open(blockchain_dir + prev_block, 'rb') as f:
        content = f.read()
    return md(content).hexdigest()


def write_block(sender, recipient, amount):
    blocks_count = len(os.listdir(blockchain_dir))
    if blocks_count == 0:
        prev_block = ''
    else:
        prev_block = str(blocks_count)

    data = {
        "sender": sender,
        "recipient": recipient,
        "amount": amount,
        "prev_block": {
            "hash": get_hash(prev_block),
            "filename": prev_block,
        }
    }

    current_block = blockchain_dir + str(blocks_count + 1)

    with open(current_block, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write('\n')


def main():
    sender = input("Enter the sender's name: ")
    recipient = input("Enter recipient's name: ")
    amount = int(input("Enter transfer amount: "))
    write_block(sender, recipient, amount)


if __name__ == '__main__':
    main()
