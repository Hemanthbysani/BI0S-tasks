#include <stdio.h>
#define str_size 500
int main()
{
    char str1[str_size], str2[str_size];
    int flg=0;
    fgets(str1, sizeof str1, stdin);	
    fgets(str2, sizeof str2, stdin);		  
    int i=1;
    while(str1[i] == str2[i])
    {
        if(str1[i] == '\0' && str2[i] == '\0')
            break;
        i++;
    }
    if((str1[i+1] == '\0') && (str2[i+1]=='\0'))
        flg=0;
    else if ((str1[i+1] != '\0') && (str2[i+1]=='\0'))
        flg=1;
    else flg=2;
    if(flg == 0)
    {
        printf("Equal");
    }
    else if(flg == 1)
    {
       printf("Second");
    }
    else if(flg == 2)
    {
       printf("First");
    }
    return 0;
}