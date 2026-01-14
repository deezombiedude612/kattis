//
// Created by Henry Heng on 15/01/2026.
//
#include <iostream>
using namespace std;

int main() {
    int X, Y, N;
    cin >> X >> Y >> N;

    for (int i = 1; i <= N; i++) {
        if (i != 1) cout << endl;
        if (i % X == 0 && i % Y == 0) cout << "Fizzbuzz";
        else if (i % X == 0) cout << "Fizz";
        else if (i % Y == 0) cout << "Buzz";
        else cout << i;
    }
    return 0;
}