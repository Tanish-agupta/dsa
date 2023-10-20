#include "biginteger.h"

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
struct node {
    int data;
    struct node *next;
};
struct node* createnode(int data) {
    struct node* current = (struct node*)malloc(sizeof(struct node));
    Temp->data = data;
    Temp->next = NULL;
    return Temp;
}
void insertAtFront(struct node** head, int data) {
    struct node* Temp = createnode(data);
    Temp->next = *head;
    *head = Temp;
}

void insertatend(struct node** head, int data) {
    struct node* Temp = (struct node*)malloc(sizeof(struct node));
    Temp->data = data;
    Temp->next = NULL;

    if (*head == NULL) {
        *head = Temp;
    } else {
        struct node* current = *head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = Temp;
    }
}
struct node* addBigIntegers(struct node* num1, struct node* num2) {
    struct node* result = NULL;
    int carry = 0;

    while (num1 || num2 || carry) {
        int x = (num1) ? num1->data : 0;
        int y = (num2) ? num2->data : 0;
        int sum = x + y + carry;
        carry = sum / 10;
        sum = sum % 10;
        insertAtFront(&result, sum);

        if (num1) num1 = num1->next;
        if (num2) num2 = num2->next;
    }

    return result;
}
void print(struct node* node) {
    if (!node) {
        printf("0");
        return;
    }

    while (node) {
        printf("%d", node->data);
        node = node->next;
    }
    printf("\n");
}

void freeList(struct node* head) {
    while (head) {
        struct node* temp = head;
        head = head->next;
        free(temp);
    }
}

struct node* subtractBigIntegers(struct node* num1, struct node* num2) {
    struct node* result = NULL;
    int borrow = 0;

    while (num1 != NULL || num2 != NULL) {
        int val1 = (num1 != NULL) ? num1->data : 0;
        int val2 = (num2 != NULL) ? num2->data : 0;
        
        int diff = val1 - val2 - borrow;

        if (diff < 0) {
            diff += 10;
            borrow = 1;
        } else {
            borrow = 0;
        }

        insertAtFront(&result, diff);

        if (num1 != NULL) num1 = num1->next;
        if (num2 != NULL) num2 = num2->next;
    }
    while (result != NULL && result->data == 0) {
        struct node* temp = result;
        result = result->next;
        free(temp);
    }

    return result;
}


void  divideNumbers(char input[], int divisor) {
    struct node* dividend = NULL;
   int i;

    for (i = 0; input[i] != '\0'; i++) {
        insertion(&dividend, input[i] - '0');
    }

    if (divisor == 0) {
        printf("Division by zero is not allowed.\n");
        return;
    }

    struct node* quotient = NULL;
    int carry = 0;

    while (dividend != NULL) {
        int currentDigit = dividend->data + carry * 10;
        carry = currentDigit % divisor;
        currentDigit /= divisor;
        insertion(&quotient, currentDigit);
        dividend = dividend->next;
    }

    if (quotient == NULL) {
        insertion(&quotient, 0);
    }
    if (quotient != NULL) {
        printf("Quotient: ");
        print(quotient);
    }
    while (Dividend != NULL) {
        struct node* temp = Dividend;
        Dividend = Dividend->next;
        free(temp);
    }
    while (quotient != NULL) {
        struct node* temp = quotient;
        quotient = quotient->next;
        free(temp);
    }
}

int main() {
	int i,n1,n2;
    struct node* num1 = NULL;
    struct node* num2 = NULL;
    struct node* result;
    
    int divisor;
    int choice;
    while(1){
    	printf("1. add big integer\n");
    	printf("2. subtract big integer\n");
    	printf("3. divide big integer\n");
    	printf("4. exit\n");
    	printf("enter your choice\n");
    	scanf("%d",&choice);
    	printf("enter size of number\n");
    scanf("%d%d",&n1,&n2);
     char str1[n1], str2[n2];
    	switch(choice){
    		case 1:
    			

    printf("Enter first big number: ");
    scanf("%s", str1);

    printf("Enter second big number: ");
    scanf("%s", str2);
     for (i = 0; i<=strlen(str1) - 1; i++) {
        insertAtFront(&num1, str1[i] - '0');
    }

    for (i = 0; i <= strlen(str2) - 1; i++) {
        insertAtFront(&num2, str2[i] - '0');
    }
    			 result = addBigIntegers(num1, num2);
    			printf("Sum: ");
    print(result);
    			break;
    		case 2:
    			
    printf("Enter first big number: ");
    scanf("%s", str1);

    printf("Enter second big number: ");
    scanf("%s", str2);
     for (i = 0; i<=strlen(str1) - 1; i++) {
        insertAtFront(&num1, str1[i] - '0');
    }

    for (i = 0; i <= strlen(str2) - 1; i++) {
        insertAtFront(&num2, str2[i] - '0');
    }
    			 result = subtractBigIntegers(num1, num2);
				printf("Result of subtraction: ");
    print(result);
    break;
    case 3:
    printf(" above printed size  not for division  ignore the size above\n");	
    printf("Enter the Dividend as a linked list of digits : ");
    
    char Dividend[100];
    scanf("%s", Dividend);
    printf("Enter the divisor: ");
    scanf("%d", &divisor);
    divideNumbers(Dividend, Divisor);
    break;
    
    case 4:
    	return 0;
    	default:
    		printf("wrong choice\n");
		}
	}
    freeList(num1);
    freeList(num2);
    freeList(result);
     return 0;
}






