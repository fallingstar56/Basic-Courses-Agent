(1) f 在  $ [a, b] $ 上有界；

(2) f 在  $ [a,b] $ 上可以达到最大、最小值，即存在  $ \xi \in [a,b] $， $ \eta \in [a,b] $，使得

 $$ f(\xi)=\max_{a\leqslant x\leqslant b}\{f(x)\},\quad f(\eta)=\min_{a\leqslant x\leqslant b}f(x). $$ 

证明 （1）假定  $ \left|f(x)\right| $ 在  $ [a,b] $ 上无界，则每个自然数 n 都不是  $ \left|f(x)\right| $ 的上界，于是存在  $ x_{n}\in[a,b] $ 使得

 $$ \mid f(x_{n})\mid>n\quad(n=1,2,\cdots). $$ 

注意到点列 $ \{x_{n}\} $有界，由定理1.5.1知 $ \{x_{n}\} $必有收敛的子列 $ \{x_{n_{k}}\} $： $ x_{0}=\lim_{k\to\infty}x_{n_{k}} $，不难看到， $ x_{0}\in[a,b] $。由于函数f在点 $ x_{0} $连续，故

 $$ \lim_{k\to\infty}f(x_{n_{k}})=f(x_{0}). $$ 

由此知 $ \{f(x_{n_{k}})\} $是一个有界数列，这与 $ |f(x_{n})|>n(n=1,2,\cdots) $矛盾.所以f在 $ [a,b] $上有界.

(2) 由(1)知，f 在  $ \lfloor a, b \rfloor $ 上有界，从而有上确界  $ M = \sup_{a \leq x \leq b} \{ f(x) \} $. 根据上确界的性质， $ \forall n \in \mathbb{N}^* $， $ M - \frac{1}{n} $ 不再是 f 在  $ [a, b] $ 中的上界，即存在  $ x_n \in [a, b] $ 使得

 $$ M-\frac{1}{n}<f(x_{n})\leqslant M. $$ 

由此知 $ \lim_{n\to\infty}f(x_n)=M $。又因为点列 $ \{x_n\} $有界，从而 $ \{x_n\} $有收敛子列 $ \{x_{n_k}\} $： $ \xi=\lim_{k\to\infty}x_{n_k} $且 $ \xi\in[a,b] $。而f在点 $ \xi $处连续，从而

 $$ f(\xi)=\lim_{k\to\infty}f(x_{n_{k}})=\lim_{n\to\infty}f(x_{n})=M=\max_{a\leq x\leq b}\{f(x)\}, $$ 

同理可证存在  $ \eta\in[a,b] $ 使得  $ f(\eta)=\min_{a\leqslant x\leqslant b}f(x) $.

### 习题 2.6

1. 设  $ f \in C[a, b] $，如果 f 在  $ [a, b] $ 上任意一点都不等于零，证明：f 在  $ [a, b] $ 上不变号.

2. 设  $ a_{2m}<0 $，求证：实系数多项式  $ x^{2m}+a_{1}x^{2m-1}+\cdots+a_{2m-1}x+a_{2m} $ 至少有两个零点.

3. 设  $ f \in C[a, b], x_1, x_2, \cdots, x_n \in [a, b] $，求证： $ \exists \xi \in [a, b] $ 使得

 $$ f(\xi)=\frac{f(x_{1})+f(x_{2})+\cdots+f(x_{n})}{n}. $$ 

4. 设  $ f \in C[0,2a] $,  $ f(0) = f(2a) $. 求证： $ \exists \xi \in [0,a] $ 使得  $ f(\xi) = f(\xi + a) $.

5. 设 a<b<c，证明： $ f(x)=\frac{1}{x-a}+\frac{1}{x-b}+\frac{1}{x-c} $ 在区间  $ (a,c) $ 内恰有两个零点.