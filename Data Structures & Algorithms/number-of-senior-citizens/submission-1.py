class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for str in details:
            val = int(str[11:13])
            if val >60:
                count+=1;
             
        return count   

          
        