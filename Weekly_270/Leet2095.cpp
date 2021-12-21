class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        if (head->next == nullptr)
            return nullptr;
        ListNode* p = head;
        int counter = 0;
        while (p != nullptr) {
            p = p->next;
            counter++;
        }
        int target = (counter/2);
        counter = 1;
        ListNode* parent = head;
        ListNode* cur = head->next;
        while (counter < target) {
            parent = cur;
            cur = cur->next;
            ++counter;
        }
        parent->next = cur->next;
        return head;
    }
};

