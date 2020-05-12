/**
 * // This is the ArrayReader's API interface.
 * // You should not implement it, or speculate about its implementation
 * class ArrayReader {
 *   public:
 *     int get(int index);
 * };
 */

class Solution {
public:
    int search(const ArrayReader& reader, int target) {
        int i=0,j=1;
        while(reader.get(j)<target)
        {
            j=j*2;
        }
  
        int left=i,right=j;
        int mid;
        while(left<=right)
        {
            mid=(left+right)/2;
           
            if(reader.get(mid)==target)
            {
            
                return mid;
            }
            
            if(reader.get(mid)<target)
            {
                
                left=mid+1;
               
            }
            if(reader.get(mid)>target)
            {
                right=mid-1;
               
            }
            
        }
        return -1;
    }
};
