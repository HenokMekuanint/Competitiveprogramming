class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        """
        ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
        
        domain="900 google.mail.com"
        arr=[900,"google.mail.com"]
        """
        dicti=defaultdict(int)
        ans=[]
        for domain in cpdomains:
            arr=domain.split()
            maindomain=arr[1]
            temp=[]
            for i in range(len(maindomain)-1,-1,-1):
                if maindomain[i]==".":
                    dicti["".join(temp)]+=int(arr[0])
                    temp.insert(0,maindomain[i])
                elif i==0:
                    temp.insert(0,maindomain[i])
                    dicti["".join(temp)]+=int(arr[0])
                else:
                    temp.insert(0,maindomain[i])
        for dom in dicti:
            ans.append(str(dicti[dom])+" "+dom)
        return ans