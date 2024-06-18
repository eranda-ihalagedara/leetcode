class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int major_elem = nums[0], major_count = 0;
        for(int &num: nums){
            if(major_count == 0) major_elem = num;
            if(major_elem == num) ++major_count;
            else --major_count;
        }
        return major_elem;
    }
};