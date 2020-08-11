当斐波那契（Leonardo Fibonacci）以兔子繁殖为例子研究下面这样一个序列时，他肯定想不到多年以后的我们仍然痴迷于这大名鼎鼎的斐波那契数列问题。

> 0、1、1、2、3、5、8、13、21、34

可以发现上面数列的第0项是0，第1项是1，第2项开始，每一项都等于前两项之和。数学上，斐波纳契数列以如下被以递归的方法定义：

> F（0）=0  
> F（1）=1  
> F（n）=F(n-1)+F(n-2)（n≥2，n∈N*）  

在现代物理、准晶体结构、化学等领域，斐波纳契数列都有直接的应用。那么如何求斐波那契数列的第 n 项呢？比较直观的方法就是用递归求解，如下：

    def fib(n):
        return n if n < 2 else fib(n-1) + fib(n-2)

计算 fib(5)时，过程如下。这种解法对于相似的子问题进行了重复的计算，运算时间是指数级增长的。

    fib(5)
    fib(4) + fib(3)
    (fib(3) + fib(2)) + (fib(2) + fib(1))
    ((fib(2) + fib(1)) + (fib(1) + fib(0))) + ((fib(1) + fib(0)) + fib(1))
    (((fib(1) + fib(0)) + fib(1)) + (fib(1) + fib(0))) + ((fib(1) + fib(0)) + fib(1))

现在让我们稍微换一种思路，先求出初始第0项、第1项的值，然后往后求第2项、第3项、...第n项的值。求每一项时只用做简单的加法即可，因此时间复杂度为 O(n)，并且只用保存每项前面两项的值，空间复杂度是 O(1)。实现如下：

    def fib(n):
        pre_1, pre_2, cur = 0, 1, n
        for i in xrange(1, n+1):
            cur = pre_1 + pre_2
            pre_1, pre_2 = cur, pre_1
        return cur

上面递归方法对子问题进行了大量的重复计算，而第二种方法通过保存子问题的求解结果，避免了重复计算子问题。仔细品味，这里第二种方法就是`动态规划`。

# 动态规划：递推求解

动态规划（Dynamic programming）是一种在数学、计算机科学和经济学中使用的，通过把原问题分解为相对简单的子问题的方式，来求解复杂问题的方法。动态规划背后的基本思想非常简单，若要解一个给定问题，我们需要解其不同部分（即子问题），再合并子问题的解以得出原问题的解（类似分治思想）。

## 适用场景

动态规划很强大，但并不是万能的，只能适用部分的问题。动态规划常常适用于具有`重复子问题`（overlapping subproblems）和`最优子结构`（optimal substructure）特点的问题，所耗时间往往远少于朴素解法。

重复子问题是指在用递归算法自顶向下对问题进行求解时，每次产生的子问题并不总是新问题，有些子问题会被重复计算多次。动态规划法利用了这种子问题的重复性质，对每一个子问题只计算一次，将其结果记忆化存储，以便下次需要同一个子问题解时直接查表，从而获得较高的效率。

最优子结构性质是指问题的最优解由相关子问题的最优解组合而成，一个问题的最优解所包含的子问题的解也是最优的。动态规划只能应用于有最优子结构的问题。

此外，动态规划还有`无后效性`。即子问题的解一旦确定，就不再改变，不受在这之后、包含它的更大的问题的求解决策影响。

## 如何规划

先定义两个术语：

* `问题状态`：问题在某一时刻的情况的抽象。
* `状态转移方程`：问题从当前状态到下一状态（通常更接近我们要求解的状态，即目标状态）所经历步骤的抽象。

动态规划是通过拆分问题，定义问题状态和状态之间的关系，使得问题能够以递推（或者说分治）的方式去解决。

设计动态规划算法的核心就是找到一个合适的状态转移方程，使我们能够从一个已知的初始状态经过状态转移方程到达目标状态。

3. 确定初始状态；

* 刻画最优解的结构特征（寻找最优子结构）
* 递归地定义最优解的值（确定状态转移方程）
* 计算最优解的值（有两种方法：带备忘录自顶向下法、自底向上法）
* 利用计算出的信息构造一个最优解（通常是将具体的最优解输出）


# 实现：程序的细节

动态规划实现通常可以采用以下两种策略：

* 自顶向下：将问题划分为若干子问题，求解这些子问题并保存结果以免重复计算，该方法将递归和缓存结合在一起。
* 自下而上：先行求解所有可能用到的子问题，然后用其构造更大问题的解。

“自顶向下”（top-down dynamic programming）方法有如下特点：

1. 能方便的得到递归公式，并用递归函数实现 
2. 保持了递归实现的代码结构，逻辑上容易理解。
3. 过程中只计算需要计算的子结果。
4. 当采用了caching技术时多次被调用时避免重复计算。

“自低向上”（bottom-up dynamic programming）方法的特点：

1. 需要设计数据结构来完成自底向上的计算过程。逻辑上相对不那么直观。 
2. 常常可以进行空间复杂度的优化。

# 例子：更好的理解

## [44. Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)

## [264 Ugly Number II](https://leetcode.com/problems/ugly-number-ii/)

> 把只含有因子 2、3和5的数称作丑数（Ugly Number），求按照从小到大的顺序第 1500 个丑数。例如6、8都是丑数，但14不是。习惯上把1当作是第一个丑数。


[具体实现](https://github.com/xuelangZF/LeetCode/blob/master/DynamicProgramming/264_UglyNumberII.py)

## 股票问题

121, 122, 123, 188, 309	


# 优化

115.Distinct Subsequences  
132 

# 更多阅读
[fibonacci数列为什么那么重要](https://www.zhihu.com/question/28062458)   
[Dynamic Programming：From Novice to Advanced](https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/)  
[什么是动态规划？动态规划的意义是什么？](https://www.zhihu.com/question/23995189/answer/35429905)   
[动态规划与状态机：最大子序列和问题的扩展](http://liam0205.me/2016/05/13/dynamic-programming-and-state-machine/)  
[hiho一下第113周《Fibonacci》题目分析](http://hihocoder.com/discuss/question/3634)  
