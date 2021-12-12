#include        <stdio.h>

/*
 * rmtags.c
 *   purpose: filter data deleting all "[A-Z]=" patterns
 *     input: text
 *    output: text without tags of form "[A-Z]="
 *    errors: no error conditions
 *     usage: rmtags < input > output
 */

int main()
{
        int c;
	int put = 0;
        while( (c = getchar()) != EOF )
        {
		if (put){
			putchar(c);		/*send to output if condition met*/
		}

		/* recalculate condition for next chat */
	
                if ( c == '=' ){
			put = 1;
		} else if (c == ';' ||  c == '\n' || c == '\t'){
			put = 0;
		}
        }
        return 0;
}
