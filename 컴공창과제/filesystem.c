#include <stdio.h>
#include <stdlib.h>


int main(void){


	FILE *fp = fopen("userData.csv", "w");
	int select_num = 0;
	char name[255];
	while(1){
		printf("1. 신규회원 저장\n");
		printf("2. 회원정보 수정\n");
		printf("3. 회원 삭제\n");
		printf("4. 모든 회원 리스트\n");
		printf("5. 종료\n");
		printf("입력하세요> ");
		scanf("%d",&select_num);


		switch(select_num){
			case 1:
				printf("이름: ");
				fscanf(fp, "%s", name);
				break;
			case 2:
				printf("2");
				break;
			case 3:
				printf("3");
				break;
			case 4:
				printf("4");
				break;
			case 5:
				printf("5");
				return 0;
		}
	}
	fprintf(fp, "test");
	fclose(fp);

	return 0;
}


