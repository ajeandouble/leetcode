#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <unistd.h>

using namespace	std;
class Solution {
public:
	int findPeakElement(vector<int>& arr) {
		print_vector(arr);
		int len = arr.size();
		int l = 0;
		int r = len - 1;        
		int mid;
		while (l <= r)
		{
			mid = l + (r - l) / 2;
			cout << "arr[" << l << "] = " << arr[l] << ' ';
			cout << "arr[" << mid << "] = " << arr[mid] << ' ';
			cout << "arr[" << r << "] = " << arr[r] << endl;
			if (mid + 1 < len
				&& mid
				&& arr[mid] > arr[mid + 1]
				&& arr[mid] > arr[mid - 1])
			{
				return mid;
			}
			else if (mid + 1 < len && arr[mid] < arr[mid + 1])
			{
				l = mid + 1;
			}
			else
			{
				r = mid - 1;
			}
		}
		return mid;
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
	int	arr[] = {5, 4, 3, 2, 1, 2, 3, 4, 5, 6};
	vector<int> v(arr, arr + (sizeof(arr) / sizeof(int)));
	int ans = s.findPeakElement(v);
	cout << ans << endl;
	return 0;
}
