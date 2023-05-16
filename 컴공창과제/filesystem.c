#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(void){


	FILE *fp = fopen("userData.csv", "a");
	int select_num = 0;
	char name[255];
	char age[255];
	char email[255];
	char cont[10];
	while(1){
		printf("1. 신규회원 저장\n");
		printf("2. 회원정보 수정\n");
		printf("3. 회원 삭제\n");
		printf("4. 모든 회원 리스트\n");
		printf("5. 종료\n");
		printf("입력하세요> ");
		scanf("%d",&select_num);


		while(1){
			if(select_num == 1){
				printf("이름: ");
				scanf("%s", name);
				fputs(strcat(name,","),fp);

				printf("나이: ");
				scanf("%s", age);
				fputs(strcat(age,","),fp);

				printf("이메일: ");
				scanf("%s", email);
				fputs(email,fp);

				fputs("\n",fp);

				printf("계속 입력할까요? (Y/N)");
				scanf("%s", cont);
				if(cont == "Y"){
					continue;
				}
				else{
					break;
				}
			}
			if(select_num == 2){
			}
			if(select_num == 3){
			}
			if(select_num == 4){
			}
			if(select_num == 5){
				return 0;
			}
		}
	}
	fprintf(fp, "test");
	fclose(fp);

	return 0;
}


