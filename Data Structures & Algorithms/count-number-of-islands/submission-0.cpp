class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        for (int i{}; i < grid.size(); i++) {
            for (int{}; j < grid[0].size(); j++) {
                if (grid[i][j] == 1) {

                }
            }
        }
    }
    void nullify(vector<vector<char>> &grid, int i, int j) { 
        if (i < 0 || i > grid.size()) {
            return
        }
        if (i < 0 || i > grid[0].size()) { 
            return
        }
        grid[i][j] = 0;
        nullify(grid, i + 1, j);
        nullify(grid, i + 1, j);
        nullify(grid, i + 1, j);
    }
};
