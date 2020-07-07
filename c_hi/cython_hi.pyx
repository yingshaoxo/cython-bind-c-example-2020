cimport cython_hi as the_c_lib # import cython_hi.pxd

def say_hi_to_yingshaoxo():
    the_c_lib.yingshaoxo()

def give_me_a_bytes_string(text):
    the_c_lib.take_a_bytes_string(text)

def give_me_a_string(text):
    text = text.encode('UTF-8')
    the_c_lib.take_another_bytes_string(text)

def give_me_a_list_of_string(a_list):
    a_list = [text.encode('UTF-8') for text in a_list]
    the_c_lib.take_an_string_array(a_list)
