#include <stdio.h>
#include <stdlib.h>

unsigned long rule_30(char l, char c, char r) {
    return (unsigned long)(l ^ (c | r));
}
char get_bit(unsigned long x, char len, char index) {
    return (x & (((unsigned long) 1) << (len - index))) >> (len - index);
}
unsigned long next_ulong(unsigned long x, char len) {
    unsigned long out = rule_30(get_bit(x, len, len-1), get_bit(x, len, len), get_bit(x, len, 1));
    for (char i = 2; i < len; i++)
            out += rule_30(get_bit(x, len, i-1), get_bit(x, len, i), get_bit(x, len, i+1)) << (len-i);
    return out + (rule_30(get_bit(x, len, len), get_bit(x, len, 1), get_bit(x, len, 2)) << (len-1));
}
char get_red(unsigned long color) {
    return (char) ((color & (unsigned long)0xff0000) >> 16);
}
char get_green(unsigned long color) {
    return (char) ((color & (unsigned long)0x00ff00) >> 8);
}
char get_blue(unsigned long color) {
    return (char) ((color & (unsigned long)0x0000ff));
}

unsigned long get_col(unsigned long hex, char col) { // 2 for red, 1 for green, 0 for blue
  return ((hex & (unsigned long)(0x0000ff << (unsigned long)(8*col))) >> 8*col);
}

int main()
{
    unsigned long m = 0xfda272;
    for (int i = 0; i < 100; ++i)
    {
        m = next_ulong(m, 24);
        printf("%lu %lu %lu %lu %d %d %d\n", m, get_col(m, 2), get_col(m, 1), get_col(m, 0), get_red(m), get_green(m), get_blue(m));  
    }
    
    return 0;
}