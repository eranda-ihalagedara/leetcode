#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = prices[0];
        int max_profit = 0;
        for (int pi:prices) { 
            if (pi -  min_price > max_profit)
                max_profit = pi - min_price;
            else if (pi < min_price)
                min_price = pi;
        }
        return max_profit;
    }
};