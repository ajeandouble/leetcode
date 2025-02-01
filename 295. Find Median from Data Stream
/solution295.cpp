#include <iostream>
#include <queue>

using namespace std;

class MedianFinder {
private:
    priority_queue<int> q;

public:
    MedianFinder() {

    }

    void addNum(int num) {
		q.push(num);
    }

    double findMedian() {
		cout << q[1] << endl;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
int	main() {
	MedianFinder mf;
	mf.addNum(1);
	mf.addNum(2);
	mf.addNum(1);
	mf.findMedian();
}