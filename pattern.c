#include <stdio.h>

void printStars(int n) {
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n - i - 1; j++) {
            printf(" ");
        }
        for (j = 0; j <= i; j++) {
            printf("* ");
        }
        printf("\n");
    }
}

int main() {
    int rows;
    printf("Enter the number of rows for the star pattern: ");
    scanf("%d", &rows);

    printStars(rows);

    return 0;
}
