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

    def print(self):
        print('Data:', self.data)
        print('Time:', self.timestamp.isoformat())
        print('Hash:', self.hash)

class Blockchain:

    def __init__(self):
        self.blocks =[]
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

    def print(self):
        for index, block in enumerate( self.blocks ):
            print('Block', index)
            block.print()

chain = Blockchain()
chain.add( "Block Data 1" )
chain.add( "Block Data 2" )
chain.add( "Block Data 3" )
chain.print()

print()
print("Verification before hacking:", chain.verify())
chain.blocks[2].data += '34'
chain.get(2).print()
print("Verification after hacking:", chain.verify())