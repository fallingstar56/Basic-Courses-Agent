证明 记  $ a = \max_{1 \leq k \leq m} a_{k} $，则

 $$ a\leqslant(a_{1}^{n}+a_{2}^{n}+\cdots+a_{m}^{n})^{\frac{1}{n}}\leqslant(m a^{n})^{\frac{1}{n}}=a m^{\frac{1}{n}}. $$ 

由例 1.3.6 知  $ \lim_{n\to\infty}m^{\frac{1}{n}}=1 $，应用夹逼原理即得所要结论.

### 习题 1.3

1. 讨论以下命题是否正确，如果不正确，请举反例.

(1) 数列  $ \{2x_{n}-y_{n}\} $ 与  $ \{3x_{n}+4y_{n}\} $ 都收敛，则数列  $ \{x_{n}\} $ 与  $ \{y_{n}\} $ 都收敛；

(2) 数列  $ \{x_{n}\} $ 收敛， $ \{y_{n}\} $ 发散，则  $ \{x_{n} + y_{n}\} $ 与  $ \{x_{n}y_{n}\} $ 均发散；

(3) 数列  $ \{x_{n}\} $、 $ \{y_{n}\} $ 均发散，则  $ \{x_{n}+y_{n}\} $ 与  $ \{x_{n}y_{n}\} $ 均发散；

(4) 数列  $ \{x_{n}\}, \{x_{n}y_{n}\} $ 都收敛，则  $ \{y_{n}\} $ 也收敛；

(5) 若  $ \lim_{n\to\infty}x_n=0 $，则对任何数列  $ \{y_n\} $，有  $ \lim_{n\to\infty}x_n y_n=0 $;

(6) 若  $ \lim_{n\to\infty}x_ny_n=0 $，则  $ \lim_{n\to\infty}x_n=0 $ 或  $ \lim_{n\to\infty}y_n=0 $.

2. 证明本节定理 1.3.1 的 (1).

3. 设  $ \lim_{n\to\infty}a_n=A, a, b\in\mathbb{R} $，满足： $ a<A<b $。证明： $ \exists N\in\mathbb{N}^* $，当  $ n>N $ 时，有  $ a<a_n<b $。

4. 求下列极限：

(1)  $ \lim_{n\to\infty}\frac{2n^{3}-2n^{2}-n-1}{3n^{3}+n^{2}+2} $;

(2)  $ \lim_{n\to\infty}\frac{2^n+(-1)^n}{2^{n-2}+(-1)^{n-1}} $

(3)  $ \lim_{n\to\infty}\frac{\sqrt{n}\cos n}{n+2} $;

(4)  $ \lim_{n\to\infty}\left(\sqrt{n^{2}-n+1}-\sqrt{n^{2}+n-2}\right) $;

(5)  $ \lim_{n\to\infty}\left(1+\frac{1}{n}\right)^{\frac{1}{n}} $;

(6)  $ \lim_{n\to\infty}\left(\frac{1}{1\cdot2}+\frac{1}{2\cdot3}+\cdots+\frac{1}{n(n+1)}\right) $;



(7)  $ \lim_{n\to\infty}\sqrt[n]{2+(-1)^n} $;

(8)  $ \lim_{n\to\infty}\left(\frac{1+2+\cdots+n}{n+2}-\frac{n}{2}\right) $;



(9)  $ \lim_{n\to\infty}\sum_{k=n}^{2n}\frac{1}{k^{2}} $;

 $$ \lim_{n\to\infty}\left(1-\frac{1}{2^{2}}\right)\left(1-\frac{1}{3^{2}}\right)\cdots\left(1-\frac{1}{n^{2}}\right) $$ 

(11)  $ \lim_{n\to\infty}\sqrt{2}\sqrt[4]{2}\sqrt[8]{2}\cdot\cdots\cdot\sqrt[2^{n}2} $; (12)  $ \lim_{n\to\infty}\left(\frac{1}{\sqrt{n^{2}+1}}+\frac{1}{\sqrt{n^{2}+2}}+\cdots+\frac{1}{\sqrt{n^{2}+n}}\right) $.

5. 设 k > 0, a > 1，证明： $ \lim_{n \to \infty} \frac{n^k}{a^n} = 0 $.

6. 设  $ x_{n} \leqslant A \leqslant y_{n} (n = 1, 2, 3, \cdots) $，并且  $ \lim_{n \to \infty} (x_{n} - y_{n}) = 0 $，求证： $ \lim_{n \to \infty} x_{n} = \lim_{n \to \infty} y_{n} = A $.

7. 设正数列  $ \{a_{n}\} $ 收敛于 A,  $ \alpha > 0 $. 求证： $ \lim_{n\to\infty}(a_n)^n = A^n $.