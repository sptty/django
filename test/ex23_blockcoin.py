# -*- coding:utf-8 -*-
# __author__ = 'sean'
# Fri Mar 16 14:52:43     2018

import hashlib as hasher
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.preious_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.preious_hash))
        return sha.hexdigest()


def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash.
    return Block(0, date.datetime.now(), "Genesis Block ,and I am sean wan.", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "hey,I am block." + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


# create the blockchain and add the genesis block.
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# how many blocks shoud we add to the chain.
# after the genesis block.

num_of_blocks_to_add = 20

# add blocks to the chain.
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    # tell everyone about it.
    print "Block #{} has been added to the blockchain!".format(block_to_add.index)
    print "Hash: {}\n".format(block_to_add.hash)
