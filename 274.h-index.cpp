#include <vector>
using namespace std;
class Solution {
public:    
    // Space O(1)
    // Time O(nlogn)
    int hIndex(vector<int>& citations) {
        std::sort(citations.begin(), citations.end(), greater<int>());
        for(int i = 0; i < citations.size(); ++i){
            if(citations[i]<=i)
                return i;
        }
        return citations.size();
    }


    // Space O(n)
    // Time O(n)
    int hIndex_optimize(vector<int>& citations) {
        int n = citations.size();
        int * hist = new int[n+1]();
        
        for(int c: citations){
            if(c >= n)
                ++hist[n];
            else
                ++hist[c];
        }

        int cnt = 0;
        for(int i = n; i >=0; --i){
            cnt += hist[i];
            if(cnt >= i)
                return i;
        }
        return 0;
    }
};