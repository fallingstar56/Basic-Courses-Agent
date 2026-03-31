由极限定义，对  $ \varepsilon = 1 - \frac{1}{a} $， $ \exists N \in \mathbb{N} $，使得当  $ n > N $ 时，有

 $$ \frac{x_{n+1}}{x_{n}}-\frac{1}{a}<\varepsilon=1-\frac{1}{a}, $$ 

即当 n>N 时有  $ x_{n+1}<x_{n} $，从而  $ \{x_{n}\} $ 单调递减（从第  $ N+1 $ 项开始）且有下界 0。于是由定理 1.4.1 知  $ \lim_{n\to\infty}x_n $ 存在，设  $ \lim_{n\to\infty}x_n=A $，对等式

 $$ x_{n+1}=\frac{n+1}{na}x_{n} $$ 

两端取极限，即得  $ A=\frac{A}{a} $. 而 a>1，所以 A=0. 即  $ \lim_{n\to\infty}\frac{n}{a^n}=0 $.

设  $ c>0, a_{1}=\sqrt{c}, a_{n+1}=\sqrt{c+a_{n}} $ ( $ n\geqslant1 $). 试证明数列  $ \{a_{n}\} $ 收敛，并求其极限值.

证明  $ a_{2}=\sqrt{c+a_{1}}=\sqrt{c+\sqrt{c}}>\sqrt{c}=a_{1} $，假定  $ a_{n}>a_{n-1} $，则

 $$ a_{n+1}=\sqrt{c+a_{n}}>\sqrt{c+a_{n-1}}=a_{n}. $$ 

应用数学归纳法即得， $ \forall n\in\mathbb{N}^{*},a_{n+1}>a_{n} $，即数列 $ \{a_{n}\} $单调递增。另一方面，

 $$ a_{2}=\sqrt{c+\sqrt{c}}<\sqrt{c+2\sqrt{c}+1}=\sqrt{c}+1. $$ 

假定  $ a_{n}<\sqrt{c}+1 $，则

 $$ a_{n+1}=\sqrt{c+a_{n}}<\sqrt{c+\sqrt{c}+1}<\sqrt{c}+1. $$ 

再次应用数学归纳法可得， $ \forall n\in N^{*},a_{n}<\sqrt{c+1} $，即数列 $ \{a_{n}\} $有上界。于是由定理1.4.1知 $ \lim_{n\to\infty}a_{n} $存在，设 $ \lim_{n\to\infty}a_{n}=A $。

对等式  $ a_{n+1}=c+a_{n} $ 两端取极限，即得  $ A^{2}=c+A $ 。解此方程得  $ A=\frac{1}{2}\pm\sqrt{c+\frac{1}{4}} $ 。由保序性有  $ A\geqslant0 $ ，负根不合题意，故舍去，所以

 $$ \lim_{n\to\infty}a_{n}=\frac{1}{2}+\sqrt{c+\frac{1}{4}}. $$ 

下面我们考虑一类特殊形式的数列极限。首先引入无穷大数列的概念。

设  $ \{a_n\} $ 是一个数列。(1) 若对于任意的正数  $ M $， $ \exists N \in \mathbb{N} $，使得当  $ n > N $ 时，有  $ |a_n| > M $，则称数列  $ \{a_n\} $ 趋向于  $ \infty $，记为  $ a_n \to \infty $ ( $ n \to \infty $)。也称  $ \{a_n\} $ 是一个无穷大数列。(2) 若对于任意正数  $ M $， $ \exists N \in \mathbb{N} $，使得当  $ n > N $ 时，有  $ a_n > M $（或  $ a_n < -M $），则称数列  $ \{a_n\} $ 趋向于  $ +\infty $（或  $ -\infty $），记为  $ a_n \to +\infty $（或  $ a_n \to -\infty $）( $ n \to \infty $)。