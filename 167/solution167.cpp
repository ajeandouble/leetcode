#include <vector>
#include <iostream>

using namespace std;

class Solution
{
public:
	vector<int> twoSum(vector<int> &numbers, int target)
	{
		int i1 = 0;
		int i2 = 1;
		size_t N = numbers.size();
		while (i1 < N)
		{
			i2 = i1 + 1;
			cout << i1 << "\t" << i2 << endl;
			while (i2 < N && numbers[i1] + numbers[i2] < target)
			{
				i2++;
				cout << "\t" << i2 << endl;
			}
			if (i2 < N && numbers[i1] + numbers[i2] == target)
				return {i1 + 1, i2 + 1};
			i1++;
		}
		return {i1 + 1, i2 + 1};
	}
};

int	main() {
	Solution s;
	vector<int> lst = {1, 3, 4, 4};
	for(int c: s.twoSum(lst, 8)) {
		cout << c << " ";
	}

	return 0;
}