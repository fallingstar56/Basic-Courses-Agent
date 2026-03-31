于是当 n > N 时便有

 $$ \begin{align*}\left|a_{n}b_{n}-AB\right|&\leqslant\left|a_{n}b_{n}-a_{n}B\right|+\left|a_{n}B-AB\right|\\&<M\frac{\varepsilon}{2M}+\frac{\varepsilon}{2(1+\left|B\right|)}\left|B\right|<\varepsilon.\end{align*} $$ 

由极限定义便知 $ \lim_{n\to\infty}a_n b_n=AB. $

（4）根据（3），要证（4）成立，只需证 $ \lim_{n\to\infty}\frac{1}{b_n}=\frac{1}{B} $，由于 $ B\neq0 $，由极限定义，对于 $ \varepsilon_{0}=\frac{|B|}{2} $， $ \exists N_{1}\in\mathbb{N} $，使得当 $ n>N_{1} $时，有 $ |b_{n}-B|<\frac{|B|}{2} $，因而当 $ n>N_{1} $时 $ |b_{n}|>\frac{|B|}{2} $，即 $ \left|\frac{1}{b_{n}}\right|<\frac{2}{|B|} $。不妨设 $ \forall n\in\mathbb{N}^* $， $ b_n\neq0 $。另一方面，再由 $ \lim_{n\to\infty}b_n=B $， $ \forall\varepsilon>0 $， $ \exists N_{2}\in\mathbb{N} $，使得当 $ n>N_{2} $时，有 $ |b_n-B|<\frac{|B|^{2}}{2} $。进而知，当 $ n>N=\max\{N_1,N_2\} $时，

 $$ \left|\frac{1}{b_{n}}-\frac{1}{B}\right|=\left|\frac{B-b_{n}}{Bb_{n}}\right|<\left|\frac{1}{B}\bullet\frac{2}{B}\right|\bullet\frac{\varepsilon\left|B\right|^{2}}{2}=\varepsilon. $$ 

即 $ \lim_{n\to\infty}\frac{1}{b_{n}}=\frac{1}{B} $

#### ▶ 例 1.3.3

求 $ \lim_{n\to\infty}\frac{n^{2}-n+1}{2n^{2}+3n-2} $

解 由于  $ \lim_{n\to\infty}\frac{1}{n}=0,\lim_{n\to\infty}\frac{1}{n^{2}}=0 $ ，应用定理 1.3.1 便得到

 $$ \lim_{n\to\infty}\frac{n^{2}-n+1}{2n^{2}+3n-2}=\lim_{n\to\infty}\frac{1-\frac{1}{n}+\frac{1}{n^{2}}}{2+\frac{3}{n}-\frac{2}{n^{2}}}=\frac{1-\lim_{n\to+\infty}\frac{1}{n}+\lim_{n\to+\infty}\frac{1}{n^{2}}}{2+3\lim_{n\to+\infty}\frac{1}{n}-2\lim_{n\to+\infty}\frac{1}{n^{2}}}=\frac{1}{2}. $$ 

#### ▶ 例 1.3.4

设 a, b 为实数，满足  $ 0 < |a| < 1, 0 < |b| < 1 $，求  $ \lim_{n \to +\infty} \frac{1 + a + a^2 + \cdots + a^n}{1 + b + b^2 + \cdots + b^n} $.

## 解 注意到

 $$ 1+a^{2}+a^{2}+\cdots+a^{n}=\frac{1-a^{n+1}}{1-a},1+b+b^{2}+\cdots+b^{n}=\frac{1-b^{n+1}}{1-b}, $$ 

所以

 $$ \lim_{n\to\infty}\frac{1+a+a^{2}+\cdots+a^{n}}{1+b+b^{2}+\cdots+b^{n}}=\lim_{n\to\infty}\frac{1-b}{1-a}\cdot\frac{1-a^{n+1}}{1-b^{n+1}}=\frac{1-b}{1-a}. $$ 