from constants import width,height, block_height
class Block:
    def __init__(self, x, y, w, h):
        self.position = [x,y]
        self.size = [w,h]
blocks = []

def get_blocks():
    return blocks
def add_block(block):
    blocks.append(block)
def remove_block(block):
    blocks.remove(block)
def create_blocks():
    padding = 5
    rows = 4
    cols = 9
    margin = 20
    block_width = width / cols
    for y in range(0,rows-1):
        for x in range(0, cols-1):
            add_block(Block(margin+x*block_width+x*padding,y*block_height+y*padding, block_width, block_height))