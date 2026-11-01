class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxSoFar{};
        for (int i{}; i < grid.size(); i++){
            for (int j{}; j < grid[0].size(); j++) {
                if (grid[i][j] == 1) {
                    maxSoFar = max(maxSoFar, count(grid, i, j));
                }
            }
        }
        return maxSoFar;
        
    }

    int count(vector<vector<int>> &grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size()) {
            return 0;
        }
        if (grid[i][j] == 0) { 
            return 0;
        }
        grid[i][j] = 0;
        return 1 + count(grid, i + 1, j) + count(grid, i, j +1) + count(grid, i - 1, j) + count(grid, i, j -1);
    }
};