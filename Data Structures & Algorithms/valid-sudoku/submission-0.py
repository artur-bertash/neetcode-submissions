class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)
        for row in range(n): 
            seen = set()
            for col in range(n):
                if board[row][col] in seen and board[row][col] != '.':
                    return False
                seen.add(board[row][col])
        
        for col in range(n):
            seen = set()
            for row in range(n):
                if board[row][col] in seen and board[row][col] != '.':
                    return False
                seen.add(board[row][col])
            
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                seen = set()
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] in seen and board[r][c] != '.':
                            return False
                        seen.add(board[r][c])
        return True