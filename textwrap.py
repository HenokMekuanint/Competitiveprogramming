import textwrap

def wrap(string, max_width):
    no_group=len(string)//max_width
    rem_char=len(string)%max_width
    right=left=0
    ans=""
    for i in range(no_group):
        while right-left+1<=max_width:
            ans+=string[right]
            right+=1
        ans+="\n"
        left=right
    ans+=string[len(string)-rem_char:]
    return ans

if __name__ == '__main__':
