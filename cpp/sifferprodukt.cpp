//
// Created by Henry Heng on 15/01/2026.
//
#include <iostream>
using namespace std;

int main() {
    int x;
    cin >> x;

    while (!(x >= 1 && x < 10)) {
        int product = 1;

        while (x >= 1) {
            int last_digit = x % 10;
            if (last_digit != 0) product *= last_digit;
            x /= 10;
        }

        x = product;
    }

    cout << x;

    return 0;
}