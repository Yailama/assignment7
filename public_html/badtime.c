#include        <stdio.h>
#include        <string.h>
#include 	<ctype.h>

/*
 * badtime.c
 *
 *      purpose find rows with incorrectly specified time
 *      method  read in a line, check for each digit and delimeter
 *      note1    This program assumes that it runs on complete data;
 *      	since there is 'incomplete.c' it would bs redundant
 *      	to check field presence again
 *      note2   file processing line by line taken from incomplete.c
 */

#define LINELEN 512                     /* oughta be enough             */
int
main()
{
        char    linebuf[LINELEN];       /* array to hold each line      */
	int badtime();

        while ( fgets( linebuf, LINELEN, stdin ) )
        {
	       	if(badtime(linebuf)){
			fputs( linebuf, stdout );
		}
        }
	return 0;
}

/*returns boolean (1) if time wrong formatting 
 *
 */

int
badtime(char dataline[])
{
        char * pattern = "TI=";
        char * match_pointer;
        int match_index;
	int tmp_int;
	match_pointer = strstr(dataline, pattern);
	if(match_pointer != NULL){
		match_index = match_pointer - dataline;
		
		//check hour
		if(isdigit(dataline[match_index+3]) == 0){
			return 1;
		} else {
		  tmp_int = dataline[match_index+3]- '0';
		 //first digit of hour cannot be > 2			  
		  if (tmp_int>2){
			  return 1;
		  } else if (tmp_int == 2 ){ 
		  	//if first hour digit >0; second cannot exceed 5
			if(isdigit(dataline[match_index+4]) == 0){
                        return 1;
		       	} else {
				tmp_int = dataline[match_index+4]- '0';
					if (tmp_int>5){
						return 1;
					}
			}
		  }
		}
		
		//check delimeter
		if(dataline[match_index+5]!=':'){
			return 1;
		}

		//first digit of minutes cannot exceed 5
		 if(isdigit(dataline[match_index+6]) == 0){
                        return 1;
                } else {
                  tmp_int = dataline[match_index+6]- '0';
                  if (tmp_int>5){
			  return 1;
		  }
		}

		//last digit is not limited by value
		if(isdigit(dataline[match_index+7]) == 0){
			return 1;
		}

	return 0;

		} else {
			return 1;
		}
}
