#include <cstdio>
#include <vector>

using namespace std;

class NumArray {
public:
    class Node {
    public:
        Node(int lbound, int rbound, int he) {
            this->lbound = lbound;
            this->rbound = rbound;
            this->he = he;
            this->left = nullptr;
            this->right = nullptr;
        }
        int lbound;
        int rbound;
        int he;
        Node* left;
        Node* right;
	~Node() {
	    if (left != nullptr)
	        delete left;
	    if (right != nullptr)
		delete right;
	}
    };
    Node* root;
    NumArray(vector<int>& nums) {
        root = build_tree(nums, 0, nums.size()-1);
    }
    
    Node* build_tree(vector<int>& nums, int left, int right) {
        if (left == right) {
            return new Node(left, left, nums[left]);
        }
        int left_last = (left+right) / 2;
        Node* node = new Node(left, right, 0);
        node->left = build_tree(nums, left, left_last);
        node->right = build_tree(nums, left_last+1, right);
        node->he = node->left->he + node->right->he;
        return node;
    }
    
    void update(int index, int val) {
        recur_update(root, index, val);
    }
    
    void recur_update(Node* node, int index, int val) {
        if (node->lbound == node->rbound && node->lbound == index) {
            node->he = val;
            return;
        }
        int left_last = (node->lbound + node->rbound) / 2;
        if (index <= left_last)
            recur_update(node->left, index, val);
        else
            recur_update(node->right, index, val);
        node->he = node->left->he + node->right->he;
    }
    
    int sumRange(int left, int right) {
        return recur_sum(root, left, right);
    }
    
    int recur_sum(Node* node, int left, int right) {
        if (left == node->lbound && right == node->rbound) {
            return node->he;
        }
        int left_last = (node->lbound + node->rbound) / 2;
        if (right <= left_last) {
            return recur_sum(node->left, left, right);
        } else if (left > left_last) {
            return recur_sum(node->right, left, right);
        }
        return recur_sum(node->left, left, left_last) + recur_sum(node->right, left_last+1, right);
    }
    ~NumArray() {
	delete root;
    }
};

int main() {
    // Test case
    vector<int> nums = {1, 3, 5};
    NumArray* s = new NumArray(nums);
    printf("%d ", s->sumRange(0, 2));
    s->update(1, 2);
    printf("%d ", s->sumRange(0, 2));
    printf("\n");
    delete s;
    return 0;
}
