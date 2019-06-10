MAX_MEMORY=640
class FreeBlock:
    def __init__(self):
        # 块号
        self.index = 0
        # 起始地址
        self.position = 0
        # 大小
        self.size=0
        # 占用情况，False为空闲
        self.isUsed = False


class DynamicPartition:
    def __init__(self):
        self.init_one = FreeBlock()
        self.init_one.size = MAX_MEMORY
        self.freeChain = []
        self.freeChain.append(self.init_one)
        self.algorithmn=0

    def firstFit(self,_index,_size):
        toAllocate = FreeBlock()
        toAllocate.index=_index
        toAllocate.size=_size
        toAllocate.isUsed=True
        for i in range(len(self.freeChain)):

            if self.freeChain[i].size >= _size and self.freeChain[i].isUsed==False:
                # 如果空闲块大小等于要分配的大小
                if self.freeChain[i].size == _size:
                    self.freeChain[i].isUsed=True
                    self.freeChain[i].index=_index
                    return True
                # 如果空闲块大小大于要分配的大小
                if self.freeChain[i].size > _size:
                    toAllocate.position=self.freeChain[i].position
                    self.freeChain[i].position+=_size
                    self.freeChain[i].size-=_size
                    self.freeChain.insert(self.freeChain[i].index-1,toAllocate)
                    return True
        print('fail to allocate')
        return False

    def bestFit(self,_index,_size):
        # allocate a new free block
        toAllocate = FreeBlock()
        toAllocate.index = _index
        toAllocate.size = _size
        toAllocate.isUsed = True

        # to find the best block to allocate
        bestBlock = FreeBlock()
        iflag=False
        sizeDifference=MAX_MEMORY

        for i in range(len(self.freeChain)):
            if self.freeChain[i].size >= toAllocate.size and self.freeChain[i].isUsed == False:
                if (self.freeChain[i].size - toAllocate.size) < sizeDifference:
                    sizeDifference=self.freeChain[i].size-toAllocate.size
                    bestBlock= self.freeChain[i]
                    iflag=True
                    # print(bestBlock.position,bestBlock.index,bestBlock.size,sizeDifference,iflag)
        if iflag==False:
            print('fail to allocate')
            return False
        #
        if sizeDifference==0:
            self.freeChain[self.freeChain.index(bestBlock)].index=_index
            self.freeChain[self.freeChain.index(bestBlock)].isUsed=True
            return True
        else:
            toAllocate.position=bestBlock.position
            self.freeChain[self.freeChain.index(bestBlock)].position+=_size
            self.freeChain[self.freeChain.index(bestBlock)].size -=_size
            self.freeChain.insert(self.freeChain[i].index - 1, toAllocate)
            return True

    def release(self, _index):
        print('length:')
        print(len(self.freeChain))
        for i in range(len(self.freeChain)):
            if self.freeChain[i].index == _index:
                self.freeChain[i].index=0
                self.freeChain[i].isUsed = False
                # 前后都是空闲区
                if len(self.freeChain)-1>i>0 and self.freeChain[i-1].isUsed==False and self.freeChain[i+1]==False:
                    self.freeChain[i-1].size += self.freeChain[i].size + self.freeChain[i+1].size
                    self.freeChain.remove(self.freeChain[i])
                    self.freeChain.remove(self.freeChain[i+1])
                    break
                # 与前一个空闲区相邻
                if i>0 and self.freeChain[i-1].isUsed==False:
                    self.freeChain[i-1].size+=self.freeChain[i].size
                    self.freeChain.remove(self.freeChain[i])
                    break
                # 与后一个空闲区相邻
                if i<len(self.freeChain)-1 and self.freeChain[i+1].isUsed==False:
                    self.freeChain[i].size+=self.freeChain[i+1].size
                    self.freeChain.remove(self.freeChain[i+1])
                    break


# HH=DynamicPartition()
# print(HH.freeChain)
# HH.bestFit(1,30)
# HH.bestFit(2,50)
# HH.bestFit(3,24)
# HH.release(1)
# for i in HH.freeChain:
# print(i.position,i.index,i.size,i.isUsed)

















