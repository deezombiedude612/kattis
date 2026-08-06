//
// Created by Henry Heng on 06/08/2026.
//
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

int main() {
  // retrieve string input
  string x;
  cin >> x;

  stringstream ss(x);
  string token;
  vector<string> tokens;

  while (getline(ss, token, '.')) {
    tokens.push_back(token);
  }

  cout << '.' << tokens[tokens.size() - 1] << endl;

  return 0;
}