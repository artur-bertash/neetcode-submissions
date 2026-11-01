class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int counter{};
        for (int i{}; i < grid.size(); i++) {
            for (int j{}; j < grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    nullify(grid, i, j);
                    counter++;
                }
            }
        }
        return counter;
    }
    void nullify(vector<vector<char>> &grid, int i, int j) { 
        if (i < 0 || i >= grid.size() || j < 0 || j >= grid[0].size()) {
            return;
        }
        if (grid[i][j] == '0') { 
            return;
        }

        grid[i][j] = '0';
        nullify(grid, i + 1, j);
        nullify(grid, i, j + 1);
        nullify(grid, i - 1, j );
        nullify(grid, i , j- 1);
    }
};
