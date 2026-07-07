from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_row = defaultdict(set)
        hash_col = defaultdict(set)
        hash_3x3 = defaultdict(set)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                else:
                    key = (i // 3, j // 3)
                    if (val in hash_row[i] or
                        val in hash_col[j] or 
                        val in hash_3x3[key]):
                        return False
                    hash_row[i].add(val)
                    hash_col[j].add(val)
                    hash_3x3[key].add(val)
                
        return True



                
            
        


            
      
            


            
