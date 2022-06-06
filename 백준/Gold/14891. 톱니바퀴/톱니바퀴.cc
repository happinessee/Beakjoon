#include <cstdio>
#include <time.h>
#include <vector>

using namespace std;

/* i3-7100u 2.4GHz CPU로 구동했습니다.

나의 알고리즘

회전 시킬 톱니바퀴 각각 벡터를 취해준다. -> 4개의 톱니바퀴 = 4개의 벡터

각 벡터는 8개의 정수형 데이터를 가지고 있다 (N극 : 0 , S극 : 1)

(1)톱니바퀴가 움직일 때 극 비교

극이 다르다면 (1)톱니바퀴와 연결된 곳의 (2)톱니바퀴 극 비교

극이 다르다면 (2)톱니바퀴와 연결된 곳의 (3)톱니바퀴 극 비교

생략.....

만약 움직인다면

(1)은 지정된 방향

(2)은 지정된 방향과 반대 방향

(3)은 지정된 방향

(4)은 지정된 방향과 반대 방향

그리고 움직인 방향에 따라 벡터의 데이터를 바꾸어준다.

12시에 있는 톱니의 극을 보고 점수를 합산해 출력한다.
*/

/*	처리되지 않은 예외가 있습니다. stack overflow 발생

벡터 배열 8개로 잘 할당되어 확인 완료

벡터 배열이 시계, 반시계 방향으로 바뀌는 것 확인 완료

moving메소드를 통해 number와 diretion변수 받아 맞는 톱니바퀴로 이동 완료

각 톱니바퀴이동 메소드로 이동해서 만약 극이 다르다면 옆의 톱니바퀴 메소드 호출 중 stack Overflow 예외 발생...

******* 찾은 예외 이유 *******

stack overflow 오류 -> 재귀함수로 계속 호출되어서 무제한으로 바퀴들이 호출되어버린다.

호출 방법을 바꾸어야 한다.		-> 함수 처음에 if(count)로 검사하고 count를 바로 올려줌으로써 다시 사용되지 못하게 만들었다.

****** 오류 ******

점수가 잘못 나온다.	왜??	예제 2번은 15점으로 잘 수행되므로 scoring 함수 문제 x

추측한 이유 : 다른 함수를 호출하면 그 함수는 더 이상 실행이 되지 않아서

printf("x번 톱니바퀴 실행")으로 확인해 보니 정상


******실제로 틀린 이유****** : 지문을 잘 못 읽었음.

제일 왼쪽부터 '톱니바퀴'가 1번부터 오른쪽으로 가며 번호가 늘어나는 것이었는데

'톱니'라고 이해함.

'톱니'는 12시 방향부터 1번째, 시계방향으로 가며 번호가 늘어난다.


*/

// 벡터 정의
vector<int> gear1;
vector<int> gear2;
vector<int> gear3;
vector<int> gear4;



// 전역변수로 각 gear의 카운트 정의
int count1 = 0;
int count2 = 0;
int count3 = 0;
int count4 = 0;

// 카운트를 정의한 이유는 한 톱니바퀴를 돌릴 때 그 톱니바퀴로 영향이 다시 오지 않게 하기 위함입니다.
// 예 1번이 2번에 영향 -> 2번이 1번과 3번을 다 검사해 1번이 돌려고 설정 -> 1번에 의해 2번이 다시 영향받음 

void movingGear1(int direction);
void movingGear2(int direction);
void movingGear3(int direction);
void movingGear4(int direction);


// 1번 톱니바퀴를 시계, 반 시계방향으로 이동시킨다.

void movingGear1(int direction) {
	if (count1 == 1) return;
	count1 += 1;
	if (gear1[2] != gear2[6]) {
			if (count2 == 0) movingGear2(-direction);	// 마주친 톱니바퀴의 극이 다르다면 movingGear(반대방향) 함수를 실행한다.
		}

	if (direction == 1) {								// 방향이 시계방향이라면
			
			gear1.insert(gear1.begin(), gear1[7]);			// 0번째에 마지막 함수를 넣어주고 마지막 함수를 제거해줌으로써 시계방향으로 돌려주고 데이터의 개수 8개를 유지한다.
			gear1.pop_back();
		}
	if (direction == -1) {								// 방향이 반시계방향이라면
			
			gear1.push_back(gear1[0]);						// 맨 뒤에 첫번째 원소를 넣어주고 첫번째 원소를 제거해줌으로써 반시계방향으로 돌려주고 데이터의 개수 8개를 유지한다.
			gear1.erase(gear1.begin());
		}
	
}
	

// 2번 톱니바퀴 함수
void movingGear2(int direction) {
	if (count2 == 1) return;
	count2 += 1;
		if (gear2[2] != gear3[6]) {
			if (count3 == 0) movingGear3(-direction);
		}

		if (gear2[6] != gear1[2]) {
			if (count1 == 0) movingGear1(-direction);
		}

		if (direction == 1) {
			

			gear2.insert(gear2.begin(), gear2[7]);
			gear2.pop_back();
		}
		if (direction == -1) {
			

			gear2.push_back(gear2[0]);
			gear2.erase(gear2.begin());
		}

	
		
}

// 3번 톱니바퀴 함수
void movingGear3(int direction) {
	if (count3 == 1) return;
	count3 += 3;
		
		if (gear3[2] != gear4[6]) {
			if(count4 == 0) movingGear4(-direction);
		}

		if (gear3[6] != gear2[2]) {
			if (count2 == 0) movingGear2(-direction);
		}

		if (direction == 1) {
			
			gear3.insert(gear3.begin(), gear3[7]);
			gear3.pop_back();
		}
		if (direction == -1) {

			gear3.push_back(gear3[0]);
			gear3.erase(gear3.begin());
		}

	

		
}

// 4번 톱니바퀴 함수
void movingGear4(int direction) {
	if (count4 == 1) return;
	count4 += 1;
	
		if (gear4[6] != gear3[2]) {
			if (count3 == 0)
				movingGear3(-direction);
		}
		if (direction == 1) {
			

			gear4.insert(gear4.begin(), gear4[7]);
			gear4.pop_back();
		}
		if (direction == -1) {
			

			gear4.push_back(gear4[0]);
			gear4.erase(gear4.begin());
		}

	
		

}
// number와 direct를 매개변수로 받아 이동시킬 톱니바퀴 번호와 방향을 정해준다.
void moving(int number, int direct) {

	if (number == 1) movingGear1(direct);
	else if (number == 2) movingGear2(direct);
	else if (number == 3) movingGear3(direct);
	else if (number == 4) movingGear4(direct);

}
// 12시 방향에 있는 톱니의 극이 S인지 확인해 맞다면 SCORE을 추가해준다.
void scoring() {
	
	int score = 0;

	if (gear1[0] == 1) score += 1;		
	if (gear2[0] == 1) score += 2;
	if (gear3[0] == 1) score += 4;
	if (gear4[0] == 1) score += 8;

	printf("%d",score);
}


// 1. 톱니바퀴 1 ~ 4까지의 톱니 극을 입력받는다.
// 2. 회전 횟수를 입력받는다. (n)
// 3. 움직일 톱니바퀴의 number와 방향을 입력받는다.
// 4. moving 메소드를 실행해 톱니바퀴를 움직이게 한다.
// 5. scoring 메소드를 실행해 score를 구해준다.
int main() {


	int temp[8];
	
	for (int i = 0; i < 4; i++) {					// 톱니바퀴의 극(상태)를 0과 1로 입력받는다.
		for (int j = 0; j < 8; j++) {				// 한 줄마다 한 개의 벡터가 입력받는다.

			scanf("%1d", &temp[j]);				// 한 번에 하나의 숫자만 입력받을 수 있게 하기 위해 %1d를 사용했다.

			if (i == 0) {
				
				gear1.push_back(temp[j]);
			}

			if (i == 1) {

				gear2.push_back(temp[j]);
			}

			if (i == 2) {

				gear3.push_back(temp[j]);
			}

			if (i == 3) {

				gear4.push_back(temp[j]);
			}

		}
	}

	int n;
	scanf("%d", &n);				// 회전 횟수 (1 ~ 10)

	int number;
	int direction;
	for (int i = 0; i < n; i++) {

		scanf("%d %d", &number, &direction);		// gear의 number와 direction 방향(1: 시계, -1: 반시계)을 입력받는다.
		moving(number, direction);
		
		// 한번 실행 되었으니 count 다시 초기화
		count1 = 0;	
		count2 = 0;
		count3 = 0;
		count4 = 0;

	}

	//clock_t start = clock();		// 시간 측정
	scoring();
	
	//clock_t end = clock();
	//printf("\n실행시간: %lf초\n", (double)(end - start) / CLOCKS_PER_SEC);
	return 0;
}