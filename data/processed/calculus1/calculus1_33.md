有大于 N 的自然数 n, m，都有

 $$ \left|x_{n}-x_{m}\right|<\frac{\varepsilon}{2}. $$ 

另一方面，由于子列 $ \{x_{n_{j}}\} $收敛于A，故对上述 $ \varepsilon $，存在 $ K\in\mathbb{N}^{*} $，只要 $ j\geqslant K $，就有

 $$ \left|x_{n_{j}}-A\right|<\frac{\varepsilon}{2}. $$ 

不妨设 K > N，这时必有  $ n_{K} > N $。结合(1)与(2)式即得，对任意的 n > N，

 $$ \left|x_{n}-A\right|\leqslant\left|x_{n}-x_{n_{K}}\right|+\left|x_{n_{K}}-A\right|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon. $$ 

所以 $ \lim_{n\to\infty}x_n=A. $

柯西收敛原理指出，在实数系中柯西列必收敛，这称为实数系的完备性。在许多情况下，用柯西收敛原则判定数列的收敛性在理论上是非常重要的。

设  $ x_{n}=\sum_{k=1}^{n}\frac{1}{k}(n=1,2,\cdots) $，证明：数列  $ \{x_{n}\} $ 发散.

证明 对任意的  $ n \in \mathbb{N}^* $，有

 $$ \left|x_{2n}-x_{n}\right|=\frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{2n}>\frac{n}{2n}=\frac{1}{2}, $$ 

于是对正数  $ \varepsilon_{0}=\frac{1}{2} $，不论  $ N\in N^{*} $ 有多大，只要 n>N，就有

 $$ \left|x_{2n}-x_{n}\right|>\frac{1}{2}, $$ 

所以 $ \{x_{n}\} $不是柯西列，因而发散.

设  $ x_{n}=\sum_{k=1}^{n}\frac{(-1)^{k}}{k^{2}}(n=1,2,\cdots) $，证明：数列  $ \{x_{n}\} $ 收敛.

证明  $ \forall n \in \mathbb{N}^* $ 及  $ p \in \mathbb{N} $，

 $$ \left|x_{n+p}-x_{n}\right|=\left|\sum_{k=n+1}^{n+p}\frac{(-1)^{k}}{k^{2}}\right|\leqslant\sum_{k=n+1}^{n+p}\frac{1}{k^{2}}\leqslant\sum_{k=n+1}^{n+p}\left(\frac{1}{k-1}-\frac{1}{k}\right)\leqslant\frac{1}{n}, $$ 

所以， $ \forall\varepsilon>0 $，取 $ N\geqslant\varepsilon^{-1} $，则当 $ n>N $时， $ \forall p\in\mathbb{N} $，有 $ \left|x_{n+p}-x_{n}\right|<\varepsilon $。即 $ \{x_{n}\} $为柯西列从而收敛。

▶ 例 1.5.3

设数列  $ \{x_{n}\} $ 满足条件  $ \sum_{k=1}^{\infty}|x_{k+1}-x_{k}|\leqslant M(n=1,2,\cdots) $，其中 M 为常数.

证明数列 $ \{x_{n}\} $收敛.