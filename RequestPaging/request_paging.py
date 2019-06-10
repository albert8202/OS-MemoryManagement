import random

# 块结构
class Block:
    def __init__(self,time):
        # 页号
        self.page  = -1
        # 是否在内存中，False为不在
        self.accessed = False
        # 记录顺序
        self.time = time

# 模拟类
class Simulator:
    def __init__(self):
        # 初始化内存块序列
        self.blocks = [Block(4),Block(3),Block(2),Block(1)]
        # 所有块是否可用
        self.accessed_all = False
        # 缺页率
        self.missing_page_counter = 0

    def accessed_all_check(self):
        flag = True
        for i in self.blocks:
            if not i.accessed:
                flag = False
        self.accessed_all = flag

    # 获取新的页
    def access_new_page(self,new_page,algorithm):
        replacement = True
        self.accessed_all_check()
        for i in self.blocks:
            # 检查是否可获得
            if not self.accessed_all:
                # 如果已经存在
                if i.page == new_page:
                    replacement = False
                    break
                elif not i.accessed:
                    i.page = new_page
                    i.accessed = True
                    replacement = False
                    break
            # 检查页面是否已经在块中
            elif i.page == new_page:
                replacement = False
                if algorithm == 1:
                    i.time = 1
                    for j in self.blocks:
                        if not j == i:
                            j.time += 1

        if replacement:
            self.missing_page_counter += 1
            #  FIFO 算法
            if algorithm == 0:
                for i in self.blocks:
                    if i.time == 4:
                        i.page = new_page
                        i.time = 1
                        for j in self.blocks:
                            if not j == i:
                                j.time += 1
                        break

            # LRU 算法
            elif algorithm == 1:
                max_value = max(self.blocks[i].time for i in range(4))
                for i in self.blocks:
                    if i.time == max_value:
                        i.page = new_page
                        i.time = 1
                        for j in self.blocks:
                            if not j == i:
                                j.time += 1
                        break
            else:
                raise print("Algorithm type error!")

# 创建指令序列和相关页表序列
def generate_list():
    m = random.randint(1, 318)
    instructions = list()
    pages = list()
    instructions.append(m)
    pages.append(int(m / 10))
    instructions.append(m + 1)
    pages.append(int((m + 1) / 10))
    while len(instructions) <= 316:
        m1 = random.randint(0, m - 1)
        instructions.append(m1)
        instructions.append(m1 + 1)
        pages.append(int(m1/10))
        pages.append(int((m1 + 1) / 10))
        m2 = random.randint(m1 + 2, 318)
        instructions.append(m2)
        instructions.append(m2 + 1)
        pages.append(int(m2 / 10))
        pages.append(int((m2 + 1) / 10))
        m = m2
    return instructions,pages