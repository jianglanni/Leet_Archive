#include <cstdio>
#include <unordered_map>

using namespace std;

class LRUCache {
public:
    unordered_map<int, int> m;
    unordered_map<int, void*> addr;  // *addr[key] == address of this node
    int capacity;
    int size = 0;

    class ListNode {
    public:
        int val;
        ListNode* prev;
        ListNode* next;
        ListNode() {}
        ListNode(int val) {
            this->val = val;
        }
        ListNode(int val, ListNode* prev, ListNode* next) {
            this->val = val;
            this->prev = prev;
            this->next = next;
        }
    };

    ListNode* head;
    ListNode* tail;
    LRUCache(int capacity) {
        this->capacity = capacity;
        head = new ListNode(-1);
        tail = new ListNode(-1, head, nullptr);
        head->next = tail;
    }

    void list_push(void* node_address) {
        ListNode* node = static_cast<ListNode*> (node_address);
        ListNode* original_tail = tail->prev;
        original_tail->next = node;
        node->prev = original_tail;
        node->next = tail;
        tail->prev = node;
    }

    void list_remove(void* node_address) {
        ListNode* node = static_cast<ListNode*> (node_address);
        node->next->prev = node->prev;
        node->prev->next = node->next;
        node->prev = nullptr;
        node->next = nullptr;
    }

    int get(int key) {
        if (addr.find(key) != addr.end() && addr.at(key) != nullptr) {
            list_remove(addr[key]);
            list_push(addr[key]);
            return m.at(key);
        }
        return -1;
    }

    void put(int key, int value) {
        m[key] = value;
        if (addr.find(key) == addr.end()) {
            addr.emplace(key, nullptr);
        }
        // Update an element in the cache
        if (addr[key] != nullptr) {
            list_remove(addr[key]);
            list_push(addr[key]);
            return;
        }
        // Condition: addr[key] = nullptr
        // Throwing a new element into the cache
        addr[key] = new ListNode(key);
        list_push(addr[key]);
        if (size < capacity) {
            ++size;  // Simply increment the size
        } else {
            // Pop the oldest element
            ListNode* victim = head->next;
            addr[victim->val] = nullptr;
            list_remove(victim);
            delete victim;
        }
    }

    ~LRUCache() {
        ListNode* n = head;
        while (true) {
            n = n->next;
            delete n->prev;
            if (n == tail)
                break;
        }
        delete tail;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
 
 int main() {
     // Test case
     LRUCache* s = new LRUCache(2);
     s->put(1, 0);
     s->put(2, 2);
     printf("%d ", s->get(1));
     s->put(3, 3);
     printf("%d ", s->get(2));
     s->put(4, 4);
     printf("%d ", s->get(1));
     printf("%d ", s->get(3));
     printf("%d ", s->get(4));
     printf("\n");
     delete s;
     return 0;
 }
