# [Gold III] 알 수 없는 문장 - 1099 

[문제 링크](https://www.acmicpc.net/problem/1099) 

### 성능 요약

메모리: 111620 KB, 시간: 128 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 7월 9일 00:17:23

### 문제 설명

<p>형택이와 그의 친구들은 자꾸 다른 사람들이 대화를 엿듣는 것이 짜증났다. 따라서, 새로운 언어를 만들었다.</p>

<p>이 언어에는 단어가 N개 있다. 그리고 이 언어의 문장은 단어를 공백없이 붙여쓴 것이다. 이 문장에서 각 단어는 0번 또는 그 이상 나타날 수 있다. 이 언어가 형택스러운 이유는 (특별한 이유는) 단어에 쓰여 있는 문자의 순서를 바꿔도 되기 때문이다. 이때, 원래 단어의 위치와 다른 위치에 있는 문자의 개수 만큼이 그 순서를 바꾼 단어를 만드는 비용이다. 예를 들어, abc란 단어가 있을 때, abc는 비용 0으로 만들 수 있고, acb, cba, bac는 비용 2로 바꿀 수 있고, bca, cab는 비용 3으로 바꿀 수 있다.</p>

<p>따라서, 한 문장을 여러 가지 방법으로 해석할 수 있다. 이때 비용의 최솟값을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 문장이 주어진다. 문장의 길이는 최대 50이다. 둘째 줄에 단어의 개수 N이 주어지며, N은 50보다 작거나 같은 자연수이다. 셋째 줄부터 N개의 줄에 각 단어가 주어진다. 단어의 길이는 최대 50이다. 문장과 단어는 알파벳 소문자로만 이루어져 있다.</p>

### 출력 

 <p>첫째 줄에 문제의 정답을 출력한다. 만약 문장을 해석할 수 없다면 -1을 출력한다.</p>

