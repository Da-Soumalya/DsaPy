num = 1441

if num == int(str(num)[::-1]):
    print("Palindrome Number")
else:
    print("Not Palindrome Number")

'''
#include <iostream>
using namespace std;

bool isPalindrome(int num){
    // Negative numbers are not palindromes
    if (num < 0) return false;

    int original_num = num;
    int reversed_num = 0;

    // Reverse the Number
    while(num > 0){
        int digit = num % 10; // Extract the last digit
        reversed_num = reversed_num*10 + digit; // Append the digit to the reversed number
        num /= 10; // Remove the last digit
    }

    // Check if the reversed number is equal to the original number
    return reversed_num == original_num;
}

int main(){
    int num = 1441;

    if(isPalindrome(num)){
        cout << "Palindrome number" << endl;
    } else {
        cout << "Not Palindrome number" << endl;
    }

    return 0;
}
'''