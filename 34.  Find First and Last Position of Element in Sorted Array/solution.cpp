#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <unistd.h>

using namespace	std;

class Solution {
public:
	vector<int> searchRange(vector<int>& nums, int target) {
		size_t len = nums.size();
		int left = 0;
		int right = len - 1;
		vector<int> ans(2);
		ans[0] = -1;
		ans[1] = -1;
		int  mid = (right - left) / 2;
		cout << "target=" << target << endl;
		while (left <= right)
		{
			mid = left + (right - left) / 2;
			cout << "nums[" << left << "] = " << nums[left] << ' ';
			cout << "nums[" << mid << "] = " << nums[mid] << ' ';
			cout << "nums[" << right << "] = " << nums[right] << endl;
			sleep(1);
			if (nums[mid] == target)
				break ;
			if (nums[mid] < target)
			{
				left = mid + 1;
			}
			else
			{
				right = mid - 1;
			}
		}
		if (nums[mid] == target)
		{
			int	tmp_mid = mid;
			while (tmp_mid - 1 >= 0 && nums[tmp_mid - 1] == target)
				--tmp_mid;
			ans[0] = tmp_mid;
			while (mid+1 < len && nums[mid+1] == target)
				++mid;
			ans[1] = mid;
		}
		return ans;
	}
};

int	main()
{
	Solution	s;
	int	arr[] = {1, 2, 3};
	vector<int> v(arr, arr + (sizeof(arr) / sizeof(int)));
	vector<int> ans = s.searchRange(v, 2);
	cout << ans[0] << ' ' << ans[1] << endl;
}