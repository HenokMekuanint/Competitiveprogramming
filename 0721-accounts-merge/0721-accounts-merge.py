class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent=defaultdict(int)
        for i in range(len(accounts)):
            parent[i]=i
        rank=[0 for i in range(len(accounts))]
        def find(x):
            root=x
            while root!=parent[root]:
                root=parent[root]
            
            while x!=root:
                temp=parent[x]
                parent[x]=root
                x=temp
            return root
            
        def union(x,y):
            parentX=find(x)
            parentY=find(y)
            if parentX==parentY:return
            
            if rank[parentY]==rank[parentY]:
                rank[parentX]+=1
            if rank[parentX]>rank[parentY]:
                parent[parentY]=parentX
            else:
                parent[parentX]=parentY
        email_to_account = defaultdict(int)
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                email_to_account[accounts[i][j]] = i
                # Perform union operation
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                union(i, email_to_account[accounts[i][j]])

        # Create result dictionary to group merged accounts
        merged_accounts = defaultdict(list)
        for i in range(len(accounts)):
            parent_index = find(i)
            merged_accounts[parent_index].extend(accounts[i][1:])

        # Format the accounts as required
        result = []
        for parent_index, emails in merged_accounts.items():
            account = [accounts[parent_index][0]]  # Add the name as the first element
            account.extend(sorted(list(set(emails))))  # Sort and append the emails
            result.append(account)

        return result