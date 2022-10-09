class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        dictionary=defaultdict(int)
        for i in arr:
            dictionary[i]+=1
        num=list(dictionary.keys())
        ans=0
        for i in num:
            for j in num:
                k=target-i-j
                if k in num:
                    freq1=dictionary[i]
                    freq2=dictionary[j]
                    freq3=dictionary[k]
                    if i==j and i==k:
                        ans+=freq1*(freq1-1)*(freq1-2)/6
                    elif i==j and i!=k:
                        ans+=(freq1)*(freq1-1)*freq3/2
                    elif i<j and j<k:
                        ans+=freq1*freq2*freq3
                ans=ans%1000000007
        return int(ans)
