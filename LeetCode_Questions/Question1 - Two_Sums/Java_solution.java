public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        int ans[] = new int[2];
        for(int i=0; i<nums.length; i++){
            int temp = target-nums[i];
            if(hm.containsKey(temp)){
                ans[0] = hm.get(temp);
                ans[1] = i;
                return ans;
            }
            else{
                hm.put(nums[i],i);
            }
        }
        return ans;
        }
