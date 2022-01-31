#include<iostream>
#include<cstring>
int main() {
	int test;
	std::cin >> test;
	std::string q[1500];
	for (int k = 0; k < test; k++) {
		int num = 0;
		int p;
		char s[21];
		char j[10000];
		std::cin >> p >> s;
		for (int y = 0; y <= 20; y++) {
			for (int b=0; b < p; b++) {
				j[num] = s[y];
				num++;
			}
		}
		q[k] = j;
	}
	for (int k = 0; k < test; k++) {
		std::cout << q[k] << std::endl;;
	}
}