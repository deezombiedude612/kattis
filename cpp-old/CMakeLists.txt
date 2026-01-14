cmake_minimum_required(VERSION 4.1)
project(cpp)

set(CMAKE_CXX_STANDARD 14)

include_directories(bits)

add_executable(cpp
        bits/stdc++.h
        fizzbuzz.cpp
        mjehuric.cpp)
