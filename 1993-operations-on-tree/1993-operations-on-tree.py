class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent=parent
        self.adj_list=defaultdict(list)
        self.locked=[0 for i in range(len(parent))]
        for i in range(len(parent)):
            self.adj_list[parent[i]].append(i)
    def lock(self, num: int, user: int) -> bool:
        if not self.locked[num]:
            self.locked[num]=user
            return True
        return False
    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num]==user:
            self.locked[num]=0
            return True
        return False    
    def upgrade(self, num: int, user: int) -> bool:
        one_locked_decendant=False
        all_unlocked_anscstor=True
        unlocked=False

        if not self.locked[num]:
            unlocked=True
        else:
            return False
        if num==0:
            no_locked_anscestor=True   
        parent=num
        while  parent!=0:
            parent=self.parent[parent]
            if self.locked[parent]>0:
                all_unlocked_anscstor=False
                break
        if all_unlocked_anscstor:
            queue=deque([num])
            while queue:
                node=queue.popleft()
                for neighbour in self.adj_list[node]:
                    if self.locked[neighbour]:
                        one_locked_decendant=True
                        self.locked[neighbour]=0
                        self.locked[num]=user
                    queue.append(neighbour)
        return one_locked_decendant and all_unlocked_anscstor and unlocked
            
            
            
            
            
        
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)