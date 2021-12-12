#include        <stdio.h>
#include        <ctype.h>
#include        <stdlib.h>
#include        <string.h>
#include 	<math.h>


/*
 *  add_division_delim.c
 *
 *      purpose: add division delimeter ',' for positive int
 *      note1: as it was stated input should contain only digits, negative numbers ommited
 *      note2: input handling and validation taken from hello6.c
 */

#define STRSIZE         100

int main(){
       	char    inputstr[STRSIZE];
	printf("Enter integer: ");   /* prompt       */
	fgets(inputstr, STRSIZE, stdin );       /* input        */
	int is_all_digits();
        int div_count = 0;
        
	if ( is_all_digits( inputstr ) == 0 ){      /* digits?  */
	       	printf("This is not a number: %s", inputstr );
	} else {
		int i = ((int)strlen(inputstr)-2);
		int comma_quants = (int)floor(i/3);
		
		char output[i + comma_quants+2]; // +1 for length & +1 for termination char
		output[i + comma_quants+1] = '\0'; //adding explicitly terminating char
		 while(i!=-1){ //fill in output from last digit
	       		output[i + comma_quants] = inputstr[i];
			div_count += 1; //count numbers in division
			if (div_count == 3 ){
				comma_quants--; //insert ','  prior division
				output[i + comma_quants] = ',';
				div_count = 0; //start count new divison
			}
			i--;
		}
		printf("%s",  output);
		printf("\n");
	}
}






/* function copied from hello6 */
int
is_all_digits( char str[STRSIZE] )
/*
 * purpose: examine a string and see if all the chars are digits
 * returns: 1 if all chars before the newline are digits, 0 otherwise
 * bug?:    what if a string with no chars appears?
 */
{
        int pos;
        for(pos = 0; pos < (int)strlen(str)-1; pos++){

                if ( ! isdigit(str[pos]) )      /* if not a dig */
                        return 0;               /* get out now! */
        }

        return 1;                       /* no problems          */
}
