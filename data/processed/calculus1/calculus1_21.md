设 $ \{a_{n}\} $是一个数列， $ 0<n_{1}<n_{2}<\cdots<n_{k}<\cdots $是一列自然数，称数列 $ \{a_{n_{k}}\} $为 $ \{a_{n}\} $的子列.

例如， $ \{2n\} $ 与  $ \{2n-1\} $ 都是自然数列 N 的子列.

若数列 $ \{a_{n}\} $收敛于A，则它的任何子列都收敛于A.

证明 设  $ \{a_{n_{k}}\} $ 为  $ \{a_{n}\} $ 的一个子列. 由于  $ \{a_{n}\} $ 收敛于 A,  $ \forall \varepsilon > 0 $,  $ \exists N \in \mathbb{N} $, 使得当 n > N 时, 有  $ \left|a_{n} - A\right| < \varepsilon $. 而  $ n_{k} \geqslant k $, 故当 k > N 时, 便有  $ \left|a_{n_{k}} - A\right| < \varepsilon $. 即  $ \{a_{n_{k}}\} $ 收敛于 A.

证明数列 $ \left\{(-1)^{n}\right\} $发散.

证明 记  $ a_{n}=(-1)^{n} $，则  $ a_{2n}=1, a_{2n-1}=-1 $。即数列  $ \left\{(-1)^{n}\right\} $ 有两个子列分别收敛于 1 和 -1。由性质 3 便知，数列  $ \left\{(-1)^{n}\right\} $ 发散。

上例说明，有界数列不一定收敛。然而我们有以下性质。

收敛数列一定有界，即存在正数 M，使得  $ \left|a_{n}\right|\leqslant M(n=1,2,\cdots) $

证明 设  $ \{a_{n}\} $ 收敛于 A. 取  $ \varepsilon=1 $，由极限定义， $ \exists N\in\mathbb{N} $，使得当  $ n\geq N $ 时， $ \left|a_{n}-A\right|<1 $。取  $ M=\max\left\{\left|a_{1}\right|,\left|a_{2}\right|,\cdots,\left|a_{N}\right|,\left|A\right|+1\right\} $，易见  $ \forall n\in\mathbb{N}^{*} $，有  $ \left|a_{n}\right|\leqslant M $。

例 1.3.2 ……

设 $ \lim_{n\to\infty}a_n=A $，证明： $ \lim_{n\to\infty}a_n^2=A^2 $。

证明 由于  $ \lim_{n\to\infty}a_n=A $，根据性质 4，存在正数 M，使得  $ \left|a_{n}\right|\leqslant M(n=1,2,\cdots) $.

另一方面， $ \forall\varepsilon>0,\exists N\in\mathbb{N} $，使得当 $ n>N $时，有 $ \left|a_{n}-A\right|<\frac{\varepsilon}{M+\left|A\right|} $。于是当 $ n>N $时

 $ |a_{n}^{2}-A^{2}|=|a_{n}+A|\cdot|a_{n}-A|\leqslant(M+|A|)|a_{n}-A|<\varepsilon. $

所以 $ \lim_{n\to\infty}a_{n}^{2}=A^{2} $

性质 5(极限的保序性)

设数列  $ \{a_{n}\} $ 收敛于 A，数列  $ \{b_{n}\} $ 收敛于 B。(1) 若 A > B，则  $ \exists N \in \mathbb{N} $，使得当 n > N 时，就有  $ a_{n} > b_{n} $；(2) 若  $ \exists N \in \mathbb{N} $，使得当 n > N 时，就有  $ a_{n} \geqslant b_{n} $，则  $ A \geqslant B $。