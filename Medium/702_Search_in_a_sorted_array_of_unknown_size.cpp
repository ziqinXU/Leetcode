///first attempt 27.81%faster, 100%less memory
//Idea:use binary search algorithm to search the target, but since here the length is not given, we can enrich
//the range by *2 of the right side each time until target is inside
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
        while(reader.get(j)<target)//enrich the range until the target is inside
        {
            j=j*2;
        }
  
        int left=i,right=j;
        int mid;
        while(left<=right)//use binary search to find the target
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
