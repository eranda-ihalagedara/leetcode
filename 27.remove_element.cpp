class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n = nums.size()-1, i = n;

        while(i>=0){
            if(nums[i] == val){
                nums[i] = nums[n];
                n--;
            }
            i--;
        }
        return n+1;
    }
};