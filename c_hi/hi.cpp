#include <hi.hpp>
#include <cstdio>
#include <string>
#include <vector>

void yingshaoxo() {
    printf("cpp: 'hi, yingshaoxo!'\n");
}

void take_a_bytes_string(const char text[]) {
    printf("%s\n", text);
}

void take_another_bytes_string(std::string text) {
    printf("%s\n", text.c_str());
}

void take_an_string_array(std::vector<std::string> text_array) {
    for(auto text: text_array){
        printf("%s\n", text.c_str());
    }
}
