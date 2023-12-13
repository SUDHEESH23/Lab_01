#include <stdio.h>

int sumOfNaturalNumbers(int n) {
    return n * (n + 1) / 2;
}

int main() {
    int n, sum;
    printf("Enter the value of n: ");
    scanf("%d", &n);

    sum = sumOfNaturalNumbers(n);
    printf("Sum of first %d natural numbers is: %d\n", n, sum);

    return 0;
}
