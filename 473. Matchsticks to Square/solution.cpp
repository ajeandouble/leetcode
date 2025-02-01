#include "../solution.hpp"

// class Solution {
// public:
//     bool found;
// 	int len;
    
// 	vector<vector<int>> sums;
// 	void	recursion(vector<int> terms, int total, int step)
// 	{
// 		if (step == 4)
// 		{
// 			if (terms.size())
// 			{
// 				if (terms[0] + terms[1] + terms[2] + terms[3] == len)
// 					sums.push_back(terms);
// 			}
// 			return ;
// 		}
// 		for (int i = total - 3 + step; i >= 1; --i)
// 		{
// 			vector<int> tmp_terms = terms;
// 			tmp_terms.push_back(i);
// 			recursion(tmp_terms, total - i, step + 1);
// 		}
// 	}
//     bool makesquare(vector<int>& matchsticks) {
// 		sort(matchsticks.begin(), matchsticks.end());

// 		this->len = matchsticks.size();
// 		cout << "yo";
// 		recursion({}, this-> len, 0);
// 		for (auto &s : sums)
// 		{
// 			cout << "yo" << endl << flush;
// 			cout << "\t"; print_vector(s); cout << endl;
// 			int index = 0;
// 			vector<int> a = vector<int>(matchsticks.begin(), matchsticks.begin() + s[0]);
// 			index += s[0];
// 			vector<int> b = vector<int>(matchsticks.begin() + index, matchsticks.begin() + index + s[1]);
// 			index += s[1];
// 			vector<int> c = vector<int>(matchsticks.begin() + index, matchsticks.begin() + index + s[2]);
// 			index += s[2];
// 			vector<int> d = vector<int>(matchsticks.begin() + index, matchsticks.begin() + index + s[3]);
// 			cout << "----\n";
// 			// print_vector(a); cout << ' ' << a.size() << "\n";
// 			// print_vector(b); cout << ' ' << b.size() << "\n";
// 			// print_vector(c); cout << ' ' << c.size() << "\n";
// 			// print_vector(d); cout << ' ' << d.size() << "\n";
// 			cout << "a sum=" << accumulate(a.begin(), a.end(), 0) << "\taccumulate<-" << endl;
// 			cout << "b sum=" << accumulate(b.begin(), b.end(), 0) << "\taccumulate<-" << endl;
// 			cout << "c sum=" << accumulate(c.begin(), c.end(), 0) << "\taccumulate<-" << endl;
// 			cout << "d sum=" << accumulate(d.begin(), d.end(), 0) << "\taccumulate<-" << endl;
// 			// return false;
// 			int a_sum = accumulate(a.begin(), a.end(), 0);
// 			int	b_sum = accumulate(b.begin(), b.end(), 0);	
// 			int	c_sum = accumulate(c.begin(), c.end(), 0);	
// 			int	d_sum = accumulate(d.begin(), d.end(), 0);
// 			if (a_sum == b_sum && a_sum == c_sum && a_sum == d_sum)
// 				return true;
// 			cout << "---" << endl;
// 		}
		
// 		return false;
//     }
// };


class Solution {
public:
    bool makesquare(vector<int>& matchsticks) {
        int n = matchsticks.size();
        if (n < 4)
            return false;
        int total = accumulate(matchsticks.begin(), matchsticks.end(), 0);
        cout << "total=" << total << endl;
        if (total % 4 != 0)
            return false ;
        sort(matchsticks.begin(), matchsticks.end());
		print_vector(matchsticks);
        int sum = 0;
        int i;
        for (i = 0; i < n - 3; ++i)
        {
			cout << i << ' ';
            sum += matchsticks[i];
            if (sum == total / 4)
                break ;
            else if (sum > total / 4)
            {
                return false ;
            }
        }
        for (sum = 0, ++i; i < n - 2; ++i)
        {
            sum += matchsticks[i];
            if (sum == total / 4)
                break ;
            else if (sum > total / 4)
            {
                return false ;
            }
            
        }
        for (sum = 0, ++i; i < n - 1; ++i)
        {
            sum += matchsticks[i];
            if (sum == total / 4)
                break ;
            else if (sum > total / 4)
            {
                return false ;
            }
            
        }
        for (sum = 0, ++i; i < n; ++i)
        {
            sum += matchsticks[i];
            if (sum == total / 4)
                break ;
            else if (sum > total / 4)
            {
                return false ;
            }      
        }
        return true ;
    }
};

int	main()
{
	Solution s;
	vector<int> v = {5,5,5,5,4,4,4,4,3,3,3,3};
	cout << (s.makesquare(v) ? "\ntrue" : "\nfalse") << endl;
}