#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <unistd.h>
#include <queue>

using namespace	std;

class Solution {
public:
   public:
	
	bool search(vector<int> &nums, int target) {
        int	len = nums.size();
		if (len == 0)
			return -1;
		int l = 0, r = len - 1;
		while (l <= r)
		{
			int mid = l + (r - l) / 2;
			cout << "nums[" << l << "] = " << nums[l] << ' ';
			cout << "nums[" << mid << "] = " << nums[mid] << ' ';
			cout << "nums[" << r << "] = " << nums[r] << endl << flush;
			while (l < r && nums[l] == nums[l + 1]) ++l;
			while (l < r && nums[r] == nums[r - 1]) --r;
			mid = l + (r - l) / 2;
			cout << ".nums[" << l << "] = " << nums[l] << ' ';
			cout << "nums[" << mid << "] = " << nums[mid] << ' ';
			cout << "nums[" << r << "] = " << nums[r] << endl << flush;
			if (nums[mid] == target)
				return true;
			if (nums[mid] >= nums[l])
			{
				if (target >= nums[l] && target < nums[mid])
					r = mid - 1;
				else
					l = mid + 1;
			}
			else
			{
				if (target <= nums[r] && target > nums[mid])
					l = mid + 1;
				else
					r = mid - 1;
			}
		}
		return false;
	}
};

int	main()
{
	Solution	s;
	int	arr[] = {1,0,1,1,1};
	vector<int> v(arr, arr + (sizeof(arr) / sizeof(int)));
	cout << (s.search(v, 0) ? "true" : "false") << endl;
	
	string str;
	str[5]= 'a';
	cout << str << endl;
	return 0;

}