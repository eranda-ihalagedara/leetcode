class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k%n;
        
        if(k==0) return;
        int knums[k];
        
        for(int i=0; i<k; ++i){
            knums[i] = nums[i];
            nums[i] = nums[n-k+i];
        }
        
        int t;
        for(int i=k; i<n; ++i){
            t = nums[i];
            nums[i] = knums[i%k];
            knums[i%k] = t;
        }


    }
};


class Solution {
public:
    void reverse(vector<int>& nums, int i, int j){
        int t;
        while(i<j){
            t = nums[i];
            nums[i]=nums[j];
            nums[j]=t;
            ++i;
            --j;
        }
    }
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k%n;
        
        if(k==0) return;
        
        reverse(nums, 0, n-k-1);
        reverse(nums, n-k, n-1);
        reverse(nums, 0, n-1);

    }
};