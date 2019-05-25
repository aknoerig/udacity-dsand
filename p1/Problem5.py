import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update( self.data.encode('utf-8') )
        sha.update( self.timestamp.isoformat().encode('utf-8') )
        if self.previous_hash:
            sha.update( self.previous_hash.encode('utf-8') )
        return sha.hexdigest()

    def __str__(self):
        string =  'Data: ' + self.data + '\n'
        string += 'Time: ' + self.timestamp.isoformat() + '\n'
        string += 'Hash: ' + self.hash + '\n'
        return string

class Blockchain:

    def __init__(self):
        self.blocks = []
        first_block = Block(
            datetime.datetime.utcnow(), 
            "Root", 
            None)
        self.blocks.append(first_block)

    def add(self, data):
        block = Block(
            datetime.datetime.utcnow(),
            data,
            self.blocks[-1].hash)
        self.blocks.append(block)

    def get(self, index):
        return self.blocks[index]

    def length(self):
        return len(self.blocks)

    def verify(self, index=None):
        if not index:
            index = len(self.blocks) - 1
        assert(index < self.length())
        for index, block in enumerate( self.blocks[:index+1] ):
            if block.hash != block.calc_hash():
                print("Modification detected in block", index)
                return False
        return True

    def __str__(self):
        string = ''
        for index, block in enumerate( self.blocks ):
            string += 'Block ' + str(index) + '\n'
            string += str(block)
        return string

chain = Blockchain()
print(chain)
#Block 0
#Data: Root
#Time: 2019-05-25T20:28:31.512319
#Hash: 3d4633cb6c75653b57c16687f994ce87477c5d4b1d648deea6a7eb81e5970c52

chain.add( "Block Data 1" )
chain.add( "Block Data 2" )
chain.add( "Block Data 3" )
print(chain)
#Block 0
#Data: Root
#Time: 2019-05-25T20:28:31.512319
#Hash: 3d4633cb6c75653b57c16687f994ce87477c5d4b1d648deea6a7eb81e5970c52
#Block 1
#Data: Block Data 1
#Time: 2019-05-25T20:28:31.512638
#Hash: 2d970edcfc61c649a3b3a9952d86a570252db82f8eac1a77b9840ea97dec0e0e
#Block 2
#Data: Block Data 2
#Time: 2019-05-25T20:28:31.512661
#Hash: ba48622eb62bf5c7a892269e27fdb1992ca90e83e3aa7ec03de6b6bc851fc218
#Block 3
#Data: Block Data 3
#Time: 2019-05-25T20:28:31.512678
#Hash: 4d6f46f8bef2db859d48b5e45a542a54dfba042f1643a454c4c7cddb139517ac

print("Verification before hacking:", chain.verify())
#Verification before hacking: True

chain.blocks[2].data += '34'
print("Verification after hacking:", chain.verify())
#Modification detected in block 2
#Verification after hacking: False