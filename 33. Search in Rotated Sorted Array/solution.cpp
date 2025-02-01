#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <unistd.h>


using namespace	std;
class Solution {
public:
    int search(vector<int>& nums, int target) {
        size_t	len = nums.size();
		if (len == 0)
			return - 1;
		int l = 0, r = len - 1;
			cout << "target=" << target << endl;
			print_vector(nums);
		int mid = l + (r - l) / 2;
		while (l < r)
		{
			mid = l + (r - l) / 2;
			cout << "nums[" << l << "] = " << nums[l] << ' ';
			cout << "nums[" << mid << "] = " << nums[mid] << ' ';
			cout << "nums[" << r << "] = " << nums[r] << endl;
			if (nums[mid] > nums[r])
			{
				l = mid + 1;
			}
			else
				r = mid;
		}
		cout << l << endl;
		cout << "nums[" << l << "]=" << nums[l] << endl;
		cout << "---" << endl;
		if (target >= nums[l] && target <= nums.back())
		{
			r = nums.size() - 1;
		}
		else
		{
			r = l;
			l = 0;
		}
		cout << "nums[" << l << "]=" << nums[l] << endl;
		cout << "nums[" << r << "]=" << nums[r] << endl;
		cout << "----" << endl;
		while (l < r)
		{
			mid = l + (r - l) / 2;
			cout << "nums[" << l << "] = " << nums[l] << ' ';
			cout << "nums[" << mid << "] = " << nums[mid] << ' ';
			cout << "nums[" << r << "] = " << nums[r] << endl;
			if (nums[mid] < target)
			{
				l = mid + 1;
			}
			else
				r = mid;
		}
		if (nums[l] == target)
			return l;
		return -1;
    }
	void	print_vector(vector<int> &v)
	{
		for (size_t i = 0; i < v.size(); ++i)	cout << v[i] << ' ';
		if (v.size()) cout << endl;
	}
};

int	main()
{
	Solution	s;
	int	arr[] = {5, 1, 3};
	vector<int> v(arr, arr + (sizeof(arr) / sizeof(int)));
	int ans = s.search(v, 3);
	cout << ans << endl;
	return 0;
}