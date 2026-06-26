class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let buy = 0;
        let sell = 0;
        let maxProfit = 0
        
        for(let i = 1; i < prices.length; i++){
            if(prices[i] > prices[sell]) sell = i;
            else if(prices[i] < prices[buy]){
                buy = i;
                if(buy >  sell) sell = buy;
            }
            maxProfit = Math.max(maxProfit, prices[sell] - prices [buy])
        }

        return maxProfit;

    }
}
