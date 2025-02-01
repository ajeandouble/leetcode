#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <unistd.h>
#include <queue>

using namespace std;

struct ListNode
{
	int val;
	ListNode *next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
	ListNode *deleteDuplicates(ListNode *head)
	{
		if (head == nullptr)
			return nullptr;
		ListNode *prev = nullptr, *cur = head;
		head = nullptr;
		while (cur)
		{
			if (cur->next && cur->val == cur->next->val)
			{
				//cout << "if" << cur->val << endl;
				ListNode *dup = cur->next;
				while (dup && cur->val == dup->val)
				{
					dup = dup->next;
				}
				if (dup == nullptr && head == nullptr)
					return nullptr;
				if (dup == nullptr || dup->next == nullptr || dup->val != dup->next->val)
				{
					if (prev != nullptr)
						prev->next = dup;
					prev = dup;
				}
				cur = dup;
			}
			else
			{
				prev = cur;
				//cout << "else" << cur->val << endl;
				cur = cur->next;
			}
					if (head == nullptr)
						head = prev;
		}
		return head;
	}
};

int main()
{
	Solution s;
	ListNode f = ListNode(5, nullptr);
	ListNode e = ListNode(4, &f);
	ListNode d = ListNode(3, &e);
	ListNode c = ListNode(3, &d);
	ListNode b = ListNode(3, &c);
	ListNode a = ListNode(3, &b);
	ListNode head = ListNode(1, &a);
	ListNode *ptr = &head;
			while (ptr)
			{
				cout << "[" << ptr->val << "]"
					<< "\t";
				ptr = ptr->next;
	}	cout << endl;
	ptr = s.deleteDuplicates(&head);
			while (ptr)
			{
				cout << "[" << ptr->val << "]"
					<< "\t";
				ptr = ptr->next;
			}		cout << endl;
	return 0;
}
