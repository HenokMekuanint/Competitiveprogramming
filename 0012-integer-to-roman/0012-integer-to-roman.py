class Solution:
    def intToRoman(self, num: int) -> str:
        dictionary={
            "1":"I",
            "5":"V",
            "10":"X",
            "50":"L",
            "100":"C",
            "500":"D",
            "1000":"M",
            "4":"IV",
            "9":"IX",
            "40":"XL",
            "90":"XC",
            "400":"CD",
            "900":"CM"
              }
        target_num=str(num)
        ptr=len(target_num)-1
        ans=[]
        while ptr>-1:
            
            if target_num[ptr:] in dictionary:
                ans.append(dictionary[target_num[ptr:]])
                target_num=int(target_num)-int(target_num[ptr:])
                ptr-=1
                target_num=str(target_num)
            elif target_num[ptr]=="0":
                ptr-=1
            else:
                if len(target_num)-1-ptr==0:
                    ans.append("I")
                    target_num=int(target_num)-1
                    target_num=str(target_num)
                elif len(target_num)-1-ptr==1:
                    ans.append("X")
                    target_num=int(target_num)-10
                    target_num=str(target_num)
                elif len(target_num)-1-ptr==2:
                    ans.append("C")
                    target_num=int(target_num)-100
                    target_num=str(target_num)
                elif len(target_num)-1-ptr==3:
                    ans.append("M")
                    target_num=int(target_num)-1000
                    target_num=str(target_num)
        return "".join(reversed(ans))