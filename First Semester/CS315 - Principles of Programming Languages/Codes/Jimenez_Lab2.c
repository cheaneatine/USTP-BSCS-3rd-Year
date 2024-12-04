#include <stdio.h>

// Function to calculate the greatest common divisor (GCD) of two numbers
int gcd(int a, int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

// Function to simplify a fraction
void simplify_fraction(int *numerator, int *denominator)
{
    int common_divisor = gcd(*numerator, *denominator);
    *numerator /= common_divisor;
    *denominator /= common_divisor;
}

// Function to add two fractions and display the result
void add_fractions(int num1, int denom1, int num2, int denom2)
{
    int result_num = num1 * denom2 + num2 * denom1;
    int result_denom = denom1 * denom2;

    simplify_fraction(&result_num, &result_denom);

    // Display the result in proper format
    if (result_num >= result_denom)
    {
        int whole_part = result_num / result_denom;
        int fractional_part = result_num % result_denom;

        if (fractional_part == 0)
        {
            printf("%d", whole_part);
        }
        else
        {
            printf("%d, %d/%d", whole_part, fractional_part, result_denom);
        }
    }
    else
    {
        printf("%d/%d", result_num, result_denom);
    }
}

int main()
{
    int test_cases;
    printf("Enter the number of test cases: ");
    scanf("%d", &test_cases);

    int numerators[test_cases][2];
    int denominators[test_cases][2];

    for (int i = 0; i < test_cases; i++)
    {
        printf("Enter the numerators and denominators of the two fractions for case #%d (separated by spaces): ", i + 1);
        scanf("%d %d %d %d", &numerators[i][0], &denominators[i][0], &numerators[i][1], &denominators[i][1]);
    }

    printf("\nResults:\n");
    for (int i = 0; i < test_cases; i++)
    {
        printf("Case #%d: ", i + 1);
        add_fractions(numerators[i][0], denominators[i][0], numerators[i][1], denominators[i][1]);
        printf("\n");
    }

    return 0;
}