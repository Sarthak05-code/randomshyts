#include <stdio.h>
#include <stdlib.h>

// Function to swap two numbers using pointers
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Bubble sort function using pointers
void bubbleSort(int *arr, int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (*(arr + j) > *(arr + j + 1))
            {
                swap(arr + j, arr + j + 1);
            }
        }
    }
}

// Function to print the array using pointers
void printArray(int *arr, int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", *(arr + i));
    }
    printf("\n");
}

int main()
{
    int n;

    // Ask user for number of elements
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    // Allocate memory for n elements
    int *arr = (int *)malloc(n * sizeof(int));

    // Check if memory was allocated successfully
    if (arr == NULL)
    {
        printf("Memory allocation failed\n");
        return 1;
    }

    // Take input from the user
    printf("Enter %d integers:\n", n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", arr + i); // Using pointer arithmetic
    }

    // Sort the array
    bubbleSort(arr, n);

    // Display the sorted array
    printf("Sorted array: ");
    printArray(arr, n);

    // Free the allocated memory
    free(arr);

    return 0;
}
