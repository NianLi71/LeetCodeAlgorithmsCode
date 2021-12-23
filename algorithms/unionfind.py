
from pprint import pprint

class UnionFind:
    def __init__(self):
        self.sets_list = []

    def union(self, a, b):
        temp_set = {a, b}
        first_inter = None
        second_inter = None
        for each_set in self.sets_list:
            if temp_set.intersection(each_set):
                if not first_inter:
                    first_inter = each_set
                else:
                    second_inter = each_set
                    break
        if not first_inter and not second_inter:
            self.sets_list.append(temp_set)
        elif first_inter and second_inter:
            first_inter.update(temp_set, second_inter)
            self.sets_list.remove(second_inter)
        else:
            first_inter.update(temp_set)

        pprint(self.sets_list)

    def connected(self, a, b):
        for cur_set in self.sets_list:
            if cur_set.intersection({a, b}) == set([a, b]):
                print('True')
                return True
        print('False')
        return False

if __name__ == '__main__':
    uf = UnionFind()
    uf.union(1,2)
    uf.union(3,4)
    uf.union(2,3)
    uf.union(2,6)

    uf.connected(1, 6)