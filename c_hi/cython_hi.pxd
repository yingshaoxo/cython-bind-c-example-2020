from libcpp.string cimport string
from libcpp.vector cimport vector

cdef extern from 'hi.cpp':
    void yingshaoxo();
    void take_a_bytes_string(const char text[]);
    void take_another_bytes_string(string text);
    void take_an_string_array(vector[string] text_array);
