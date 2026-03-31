#### 定理 1.3.2（夹逼原理）

设数列  $ \{a_n\} $， $ \{b_n\} $ 和  $ \{x_n\} $ 满足条件： $ \exists n_0 \in \mathbb{N} $，使得当  $ n > n_0 $ 时有

 $$ a_{n}\leqslant x_{n}\leqslant b_{n}. $$ 

若 $ \lim_{n\to\infty}a_n=\lim_{n\to\infty}b_n=A $，则 $ \lim_{n\to\infty}x_n=A $。

证明 由于当  $ n > n_{0} $ 时

 $$ a_{n}-A\leqslant x_{n}-A\leqslant b_{n}-A, $$ 

从而

 $$ \left|x_{n}-A\right|\leqslant\max\left\{\left|a_{n}-A\right|,\left|b_{n}-A\right|\right\}. $$ 

另一方面， $ \lim_{n\to\infty}a_n=\lim_{n\to\infty}b_n=A $，故 $ \forall\varepsilon>0,\exists N_1\in\mathbb{N} $，使得当 $ n>N_1 $时，同时有

 $ |a_n-A|<\varepsilon,\quad|b_n-A|<\varepsilon. $

从而知，当  $ n > N = \max\{n_{0}, N_{1}\} $ 时，有  $ \left|x_{n} - A\right| < \varepsilon. $ 所以  $ \lim_{n \to \infty} x_{n} = A. $

#### ▶ 例 1.3.5

求 $ \lim_{n\to\infty}\left(\sqrt{n+3}-\sqrt{n-1}\right) $

解  $ \forall n \in \mathbb{N}^* $，有

 $$ 0\leqslant\sqrt{n+3}-\sqrt{n-1}=\frac{4}{\sqrt{n+3}+\sqrt{n-1}}<\frac{4}{\sqrt{n}}. $$ 

不难看出 $ \lim_{n\to\infty}\frac{4}{\sqrt{n}}=0 $。另外，由常数 $ a_{n}=0(n=1,2,\cdots) $组成的数列以0为极限。

于是由定理 1.3.2 就得到  $ \lim_{n\to\infty}\left(\sqrt{n+3}-\sqrt{n-1}\right)=0. $

设 a > 0，求证  $ \lim_{n \to \infty} \sqrt[n]{a} = 1 $.

证明 当  $ a \geqslant 1 $ 时， $ \forall n \geqslant a, 1 \leqslant \sqrt[n]{a} \leqslant \sqrt[n]{n} $. 又由例 1.2.3 知  $ \lim_{n \to \infty} \sqrt[n]{n} = 1 $，应用夹逼原理即得  $ \lim_{n \to \infty} \sqrt[n]{a} = 1 $. 当 0 < a < 1 时， $ \frac{1}{a} > 1 $，所以

 $$ \lim_{n\to\infty}\sqrt[n]{a}=\frac{1}{\lim\limits_{n\to\infty}\sqrt[n]{\frac{1}{a}}}=\frac{1}{1}=1. $$ 

#### ▶ 例 1.3.7

设 $ a_{1},a_{2},\cdots,a_{m} $是m个非负数，求证：

 $$ \lim_{n\to\infty}(a_{1}^{n}+a_{2}^{n}+\cdots+a_{m}^{n})^{\frac{1}{n}}=\max_{1\leq k\leq m}a_{k}. $$ 