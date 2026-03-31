例如，数列 $ \left\{(-1)^{n}n\right\} $趋向于 $ \infty $，数列 $ \{2^{n}\} $与 $ \{-n\} $分别趋向于 $ +\infty $与 $ -\infty $。

#### 定理 1.4.2(Stolz 定理)

(1)设数列 $ \{b_{n}\} $严格单调递增且 $ b_{n}\to+\infty(n\to\infty) $. 如果 $ \lim_{n\to\infty}\frac{a_{n}}{b_{n}-b_{n-1}}=A $, 则 $ \lim_{n\to\infty}\frac{a_{n}}{b_{n}}=A $; (2)设数列 $ \{b_{n}\} $严格单调递减且 $ \lim_{n\to\infty}b_{n}=\lim_{n\to\infty}a_{n}=0 $. 如果 $ \lim_{n\to\infty}\frac{a_{n}-a_{n-1}}{b_{n}-b_{n-1}}=A $, 则 $ \lim_{n\to\infty}\frac{a_{n}}{b_{n}}=A $.

由于篇幅所限，我们略去这个定理的证明。

已知 $ \lim_{n\to\infty}x_n=A $，求证： $ \lim_{n\to\infty}\frac{x_1+x_2+\cdots+x_n}{n}=A. $

证明 在 Stolz 定理中取  $ a_{n}=x_{1}+x_{2}+\cdots+x_{n}, b_{n}=n $ 即得所要结论.

令  $ x_{n}=\frac{1}{\ln n}\left(1+\frac{1}{2}+\cdots+\frac{1}{n}\right) $，求  $ \lim_{n\to\infty}x_{n} $

解 在 Stolz 定理中令  $ a_{n}=1+\frac{1}{2}+\cdots+\frac{1}{n}, b_{n}=\ln n (n=1,2,\cdots) $，则有

 $$ \lim_{n\to\infty}\frac{a_{n+1}-a_{n}}{b_{n+1}-b_{n}}=\lim_{n\to\infty}\frac{\frac{1}{n+1}}{\ln(n+1)-\ln n}=1. $$ 

应用 Stolz 定理即得  $ \lim_{n\to\infty}x_n=\lim_{n\to\infty}\frac{a_n}{b_n}=1 $

令  $ c_{n}=\frac{1^{k}+2^{k}+\cdots+n^{k}}{n^{k+1}} $（其中 k 为自然数），求  $ \lim_{n\to\infty}c_{n} $

解 在 Stolz 定理中令  $ a_{n}=1^{k}+2^{k}+\cdots+n^{k}, b_{n}=n^{k+1} (n=1,2,\cdots) $，则有

 $ b_n - b_{n-1} = n^{k+1} - (n-1)^{k+1} = n^k + n^{k-1}(n-1) + \cdots + (n-1)^k, $

所以

 $$ \begin{aligned}\lim_{n\rightarrow\infty}\frac{a_{n}-a_{n-1}}{b_{n}-b_{n-1}}&=\lim_{n\rightarrow\infty}\frac{n^{k}}{n^{k}+n^{k-1}(n-1)+\cdots+(n-1)^{k}}\\&=\lim_{n\rightarrow\infty}\left[1+\frac{n-1}{n}+\cdots+\left(\frac{n-1}{n}\right)^{k}\right]^{-1}\\&=\frac{1}{k+1},\end{aligned} $$ 

应用 Stolz 定理即得