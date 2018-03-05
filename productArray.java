class Solution {
    public int[] buildLeftProductArray(int[] nums) {
        int[] leftArray = new int[nums.length];
        leftArray[0] = 1;
        
        for(int i = 1; i < nums.length; i++) {
            leftArray[i] = leftArray[i-1] * nums[i-1];
        }
        
        return leftArray;
    }
    
    public int[] buildRightProductArray(int[] nums) {
        int[] rightArray = new int[nums.length];
        rightArray[nums.length-1] = 1;
        
        for(int i = nums.length - 2; i >= 0; i--) {
            rightArray[i] = rightArray[i+1] * nums[i+1];
        }
        
        return rightArray;
    }
    
    public int[] productExceptSelf(int[] nums) {
        if(nums.length <= 0) return new int[0];
        
        int[] leftArray = buildLeftProductArray(nums);
        int[] rightArray = buildRightProductArray(nums);
        
        int[] solutionArray = new int[nums.length];
        for(int i = 0; i < nums.length; i++) {
            solutionArray[i] = leftArray[i] * rightArray[i];
        }
        
        return solutionArray;
    }
}
