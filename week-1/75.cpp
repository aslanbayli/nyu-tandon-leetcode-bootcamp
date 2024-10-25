class Solution {
public:
    void sortColors(vector<int>& nums) {
        // counting sort
        int n = nums.size();
        int freq[3] = {0};
        int res[n];
        
        for (int i = 0; i < n; i++) {
            freq[nums[i]]++;
        }
        
        int idx = 0;
        for (int i = 0; i < 3; i++) {
            while (freq[i] != 0) {
                nums[idx] = i;
                freq[i]--;
                idx++;
            }
        }
       
    }
};
