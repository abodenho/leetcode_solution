#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

        int i = 0;
        int j = 0;

        int total_size = nums1.size() + nums2.size();

        int previous = 0;
        int current = 0;

        for (int k = 0; k <= total_size / 2; ++k) {

            previous = current;

            if (i >= nums1.size()) {
                current = nums2[j++];
            } else if (j >= nums2.size()) {
                current = nums1[i++];
            } else if (nums1[i] <= nums2[j]) {
                current = nums1[i++];
            } else {
                current = nums2[j++];
            }
        }

        if (total_size % 2 != 0) {
            return current;
        }

        return (previous + current) / 2.0;
    }
};