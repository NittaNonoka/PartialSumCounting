# PartialSumCounting
## 動的計画法（DP）
### 部分和数え上げ問題

n個の正の整数a[0], a[1], .., a[n-1]と正の整数Aが与えられる。

これらの整数から何個かの整数を選んで総和がAになるようにする方法が何通りあるかを求めよ。

ただし、答えがとても大きくなる可能性があるので、10000000009で割ったあまりで出力せよ。

【制約】
* 1≤n≤100
* 1≤a[i]≤1000
* 1≤A≤10000

【数値例】

1)
n = 5<br>
a = (7,5,3,1,8)<br>
A = 12<br>

    答え：2 ((7,5),(3,1,8)の２通り)

2)
n = 4<br>
a = (4,1,1,1)<br>
A =5

    答え：3((4,1),(4,1),(4,1)の３通り)
