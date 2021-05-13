#include <stdio.h>  
#define MAX_SIZE 1000
void sort(int n, int* ptr) 
{ 
    int i, j, t; 
    for (i = 0; i < n; i++) { 
        for (j = i + 1; j < n; j++) { 
            if (*(ptr + j) < *(ptr + i)) { 
                t = *(ptr + i); 
                *(ptr + i) = *(ptr + j); 
                *(ptr + j) = t; 
            } 
        } 
    } 
    for (i = 0; i < n; i++) 
        printf("%d\n", *(ptr + i)); 
} 
  
int main()
{
    int arr[MAX_SIZE]; 
    int i, N;
    scanf("%d", &N);
    for(i=0; i<N; i++)
    {
        scanf("%d", &arr[i]);
    }   
    sort(N, arr);
    return 0;
}