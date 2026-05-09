num = 10400

print(int(str(num[::-1])))

'''
#include <iostream>
using namespace std;

int main(){
    int num = 10400;
    int reversed_num = 0;

    // Reverse the number
    while(num > 0){
        int digit = num % 10; // Extract the last digit
        reversed_num = reversed_num * 10 + digit // Append the digit to the reversed number
        num /= 10;
    }

    // Print the reversed number
    cout << reversed_num << endl;

    return 0;
}
'''