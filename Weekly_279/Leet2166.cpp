#include <cstdio>
#include <vector>
#include <string>

using namespace std;

class Bitset {
public:
    vector<bool> myset;
    int counter = 0;
    int size;
    Bitset(int size) {
        this->size = size;
        myset.resize(size, false);
    }

    void fix(int idx) {
        if (!myset[idx])
            ++counter;
        myset[idx] = true;
    }

    void unfix(int idx) {
        if (myset[idx])
            --counter;
        myset[idx] = false;
    }

    void flip() {
        counter = size - counter;
        myset.flip();
    }

    bool all() {
        return counter == size;
    }

    bool one() {
        return counter > 0;
    }

    int count() {
        return counter;
    }

    string toString() {
        string ret;
        ret.resize(size, '0');
        for (int i = 0; i < size; ++i)
            if (myset[i])
                ret[i] = '1';
        return ret;
    }
};

int main() {
    Bitset* bs = new Bitset(5); // bitset = "00000".
    bs->fix(3);     // the value at idx = 3 is updated to 1, so bitset = "00010".
    bs->fix(1);     // the value at idx = 1 is updated to 1, so bitset = "01010".
    bs->flip();     // the value of each bit is flipped, so bitset = "10101".
    printf("%d\n", bs->all());      // return False, as not all values of the bitset are 1.
    bs->unfix(0);   // the value at idx = 0 is updated to 0, so bitset = "00101".
    bs->flip();     // the value of each bit is flipped, so bitset = "11010".
    printf("%d\n", bs->one());      // return True, as there is at least 1 index with value 1.
    bs->unfix(0);   // the value at idx = 0 is updated to 0, so bitset = "01010".
    printf("%d\n", bs->count());    // return 2, as there are 2 bits with value 1.
    printf("%s\n", bs->toString().c_str()); // return "01010", which is the composition of bitset.
    delete bs;
    return 0;
}