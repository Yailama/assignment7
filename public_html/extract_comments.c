#include        <stdio.h>
#include        <string.h>
/*
 * extract_comments.c
 *   purpose: leaves only comments of 2 posible styles in c program
 *     input: text
 *    output: text that contains only comments:
 *    errors: no error conditions
 *     usage: rmtags < input > output
 */


int is_match(char, char);
int is_ending(int, char, char);

int main()
{
	int ending;
	int i=0;
	char previous_char;
	char current_char;
	char c;
	int match;
	
	while( (c = getchar()) != EOF ){
		current_char = c;
		if(i==0){
			previous_char = c;
			i+=1;
		} else {
			if (match){
				if (i==1){
					putchar('/');
					i=2;	
				}
					putchar(current_char);
				
				ending = is_ending(match, previous_char, current_char);
				if (ending){
					putchar('\n');
					match = 0;
					i = 1;
				}
			}
		}
		if(match == 0){	
			match = is_match(previous_char, current_char);
		}
		previous_char = current_char;
	}

        return 0;
}


/*
 *   purpose: find whether 2 chars form comment start
 *     input: 2 characters
 *     return: index of found pattern: '1' for old style, '2' for new, '0' for none
 */
int
is_match(char char1, char char2){
	if(char1 == '/'){
		if(char2 == '*'){
			return 1;
		} else if (char2 == '/'){
			return 2;
		} else return 0;
	}
	return 0;
}

/*
 *   purpose: find whether 2 chars form comment end based on start pattern 
 *     input: int pattern code, 2 characters
 *     return: 1 if 2 chars correspond to found style comment end, 0 otherwise
 */
int
is_ending(int is_match, char char1, char char2){

	if(is_match){ //check generally so no supferflious operations ocurr for each char
		if ( (is_match == 2 && char2 == '\n') || (is_match == 1 && char1 == '*' && char2 == '/')){
			return 1;
		}
	}

	return 0; //if no pattern match, no ending. if there was no start, then there is no ending either
	}
