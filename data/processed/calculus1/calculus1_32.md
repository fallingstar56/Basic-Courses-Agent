得  $ \xi=\lim_{n\to\infty}a_n $ 存在且  $ \forall n\in\mathbb{N}^* $,  $ a_n\leqslant\xi $. 再由(2)，

 $$ b_{n}-a_{n}=2^{-n}(b-a)\rightarrow0\quad(n\rightarrow\infty), $$ 

所以， $ \lim_{n\to\infty}b_n=\lim_{n\to\infty}a_n=\xi. $ 而  $ \{b_n\} $ 单调递减，故  $ \forall n\in\mathbb{N}^* $， $ a_n\leqslant\xi\leqslant b_n $。

由于每个区间  $ [a_{n}, b_{n}] $ 中都包含有  $ \{x_{n}\} $ 中的无穷多项，先在  $ [a_{1}, b_{1}] $ 中取  $ x_{n_{1}} $，再在  $ [a_{2}, b_{2}] $ 中取  $ x_{n_{2}} $，使得  $ n_{2} > n_{1} $，然后在  $ [a_{3}, b_{3}] $ 中取  $ x_{n_{3}} $，使得  $ n_{3} > n_{2} $，……，如此作下去，即得  $ \{x_{n}\} $ 的子列  $ \{x_{n_{j}}\} $ 满足  $ x_{n_{j}} \in [a_{j}, b_{j}] $ ( $ j = 1, 2, \cdots $)，再由夹逼定理可得

 $$ \lim_{j\to\infty}x_{n_{j}}=\lim_{j\to\infty}a_{j}=\lim_{j\to\infty}b_{j}=\xi. $$ 

即子列  $ \{x_{n}\} $ 收敛于  $ \xi $.

在介绍下一个基本定理之前，先引入柯西列的概念。

定义 1.5.1

称数列 $ \{x_{n}\} $为柯西列（或基本列），如果 $ \forall\varepsilon>0,\exists N\in\mathbb{N} $，使得对所有大于N的自然数n,m，都有

 $$ \left|x_{n}-x_{m}\right|<\varepsilon, $$ 

注 在上面定义中，不妨设  $ m \geqslant n $，m 可写为  $ m = n + p $， $ p \in \mathbb{N} $。从而  $ \{x_n\} $ 为柯西列也可以表述为：

 $ \forall \varepsilon > 0, \exists N \in \mathbb{N} $，当  $ n > N $ 时， $ \forall p \in \mathbb{N} $，有  $ \left|x_{n+p} - x_n\right| < \varepsilon $。

定理 1.5.2（柯西收敛原理）

数列 $ \{x_{n}\} $收敛的充分必要条件是 $ \{x_{n}\} $为柯西列.

证明 必要性：设数列  $ \{x_{n}\} $ 收敛， $ A=\lim_{n\to\infty}x_{n} $，则  $ \forall\varepsilon>0,\exists N\in\mathbb{N} $，使得当 n>N 时就有

 $$ \left|x_{n}-A\right|<\frac{\varepsilon}{2}. $$ 

于是，对任意大于 N 的自然数 n, m，都有

 $$ \left|x_{m}-x_{n}\right|\leqslant\left|x_{m}-A\right|+\left|x_{n}-A\right|<\varepsilon, $$ 

因此 $ \{x_{n}\} $为柯西列.

充分性：设  $ \{x_{n}\} $ 为柯西列，首先证明， $ \{x_{n}\} $ 有界。取  $ \varepsilon=1 $，由柯西列定义， $ \exists N\in\mathbb{N} $，使得当  $ n\geq N $ 时就有

 $$ \left|x_{n}-x_{N+1}\right|<1. $$ 

令  $ M = \max\{|x_1|, |x_2|, \cdots, |x_N|, |x_{N+1}| + 1\} $，易见  $ \forall n \in \mathbb{N}^* $，有  $ |x_n| \leqslant M $。即  $ \{x_n\} $ 有界。于是，由定理 1.5.1 推出，存在  $ \{x_n\} $ 的收敛子列  $ \{x_{n_j}\} : \lim_{j \to \infty} x_{n_j} = A $。下面证明： $ \lim_{n \to \infty} x_n = A $。事实上，由于  $ \{x_n\} $ 是柯西列，故  $ \forall \varepsilon > 0, \exists N \in \mathbb{N} $，使得所