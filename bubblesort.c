

#include <stdio.h>
#include <stdlib.h>

#define ARRAY_SIZE 50

void bubbleSort(int arr[], int n) {
    int i, j, temp;
    for (i = 0; i < n-1; i++) {
        for (j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main()
{
	int arr[ARRAY_SIZE];
	
	for(int i=0; i<ARRAY_SIZE; i++)
		arr[i] = rand();
	
	
	bubbleSort(arr, ARRAY_SIZE);
	printf("Sorted array: \n");
	for (int i = 0; i < ARRAY_SIZE; i++)
		printf("%d ", arr[i]);
	printf("\n");
	return 0;
}
