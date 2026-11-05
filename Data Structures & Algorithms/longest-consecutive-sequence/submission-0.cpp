class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
         std::unordered_set<int> hashSet(nums.begin(), nums.end());
       int max_length = 0;
       for (auto num : nums) {
        int copy = num;
        if (hashSet.find(copy - 1) != hashSet.end()) {
            int counter = 0;
            
            while(hashSet.find(copy) != hashSet.end()) {
                copy++;
                counter++;
            }
        max_length = std::max(max_length, counter);
        counter = 0;
        }
        
        
       }
       return max_length + 1;
    }
};
