#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* indices = malloc(sizeof(int) * 2);
    if (numsSize == 2) {
        if (nums[0] + nums[1] == target) {
            indices[0] = 0;
            indices[1] = 1;
        }
    }
    for (int m = 0; m < numsSize; m++) {
        for (int k = m + 1; k < numsSize; k++) {
            int res = nums[m] + nums[k];
            if (res == target && m != k) {
                indices[0] = m;
                indices[1] = k;
                break;
            }
        }
    }
    return (indices);
}

int main() {
	int m = 2;
	int arr[4] = {2,7,11,15};
	int *indices = twoSum(arr, 4, 22, &m);
	printf("array: [%d, %d]\n", indices[0], indices[1]);
	return 0;
}
