class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n= len(arr)
        newArr = [0]*n
        for i in range(n):
            rightmax = -1
            for j in range(i+1, n):
                rightmax = max(rightmax,arr[j])
            newArr[i]=rightmax
        return newArr

