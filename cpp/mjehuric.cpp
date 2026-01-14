//
// Created by Henry Heng on 15/01/2026.
// Bubble Sort Question
//

#include <iostream>
using namespace std;

void printArr(int* A, int len) {
    for (int i = 0; i < len; i++) {
        if (i)
            cout << ' ';
        cout << A[i];
    }
    cout << endl;
}

int main() {
    int n = 5;
    int A[n];
    for (int i = 0; i < n; i++)
        cin >> A[i];

    bool is_ascending = false;
    while (!is_ascending) {
        is_ascending = true;

        for (int i = 0; i < n - 1; i++) {
            if (A[i] > A[i + 1]) {
                is_ascending = false;
                swap(A[i], A[i + 1]);
                printArr(A, n);
            }
        }
    }

    return 0;
}
