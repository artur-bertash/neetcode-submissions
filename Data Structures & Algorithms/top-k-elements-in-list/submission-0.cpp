class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>> freq_vec(nums.size() + 1);
        unordered_map<int, int> freq;

        for (int i{}; i < nums.size(); i++) {
            freq[nums[i]]++;
        }
        
        for (auto [key, val] : freq) {
            freq_vec[val].push_back(key);
        }
        vector<int> res;
        for (int i = freq_vec.size() - 1; k > 0 ; i--) {
            for (auto el : freq_vec[i]) {
                
                res.push_back(el);
                k--;
            }
            
        }
        return res;
    }
};
