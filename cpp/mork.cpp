//
// Created by Henry Heng on 15/01/2026.
//
#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    if (m == 0 || m == n && m == 2) cout << "Jebb";
    else cout << "Neibb";

    return 0;
}