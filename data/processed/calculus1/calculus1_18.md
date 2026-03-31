(3)  $ \lim_{n\to\infty}\frac{\ln n}{n}=0. $

证明 (1)  $ \forall \varepsilon > 0 $,

 $$ \begin{aligned}&|\mathbf{e}^{a_{n}}-\mathbf{e}^{A}|<\varepsilon\\ \Leftrightarrow\quad|\mathbf{e}^{a_{n}-A}-1|<\varepsilon\mathbf{e}^{-A}\\ \Leftrightarrow\quad1-\varepsilon\mathbf{e}^{-A}<\mathbf{e}^{a_{n}-A}<1+\varepsilon\mathbf{e}^{-A}\\ \Leftrightarrow\quad\ln(1-\varepsilon\mathbf{e}^{-A})<a_{n}-A<\ln(1+\varepsilon\mathbf{e}^{-A}).\end{aligned} $$ 

不妨设  $ \varepsilon < \varepsilon^{A} $，令  $ \delta = \min \left\{ -\ln(1 - \varepsilon e^{-A}), \ln(1 + \varepsilon e^{-A}) \right\} $，则  $ \delta > 0 $。由于  $ \lim_{n \to \infty} a_n = A $，故  $ \exists N \in \mathbb{N} $，使得当  $ n > N $ 时，就有  $ \left| a_n - A \right| < \delta $。于是当  $ n > N $ 时，不等式（1）成立。从而有  $ \left| e^{a_n} - e^{A} \right| < \varepsilon $。由极限定义即得  $ \lim_{n \to \infty} e^{a_n} = e^{A} $。

(2) $ \forall\varepsilon>0 $，要使 $ \left|\ln a_{n}-\ln A\right|<\varepsilon $，只需

 $$ -\varepsilon<\ln\frac{a_{n}}{A}<\varepsilon, $$ 

亦即

 $$ A(\mathrm{e}^{-\varepsilon}-1)<a_{n}-A<A(\mathrm{e}^{\varepsilon}-1). $$ 

令  $ \delta = \min\{A(1 - e^{-t}), A(e^{t} - 1)\} $，显然  $ \delta > 0 $。由于  $ \lim_{n \to \infty} a_n = A $，故  $ \exists N \in \mathbb{N} $，使得当  $ n > N $ 时，就有  $ |a_n - A| < \delta $。于是当  $ n > N $ 时，不等式（2）成立。从而有  $ |\ln a_n - \ln A| < \varepsilon $。由极限定义即得  $ \lim_{n \to \infty} \ln a_n = \ln A $。

(3) 由例 1.2.3 知， $ \lim_{n\to\infty}\sqrt[n]{n}=1 $。再由(2)即得

 $$ \lim_{n\to\infty}\frac{\ln n}{n}=\lim_{n\to\infty}\ln n^{\frac{1}{n}}=\ln1=0. $$ 

▶ 例 1.2.5 ……

设 $ \lim_{n\to\infty}a_n=A,\lim_{n\to\infty}b_n=B $，求证： $ \lim_{n\to\infty}(a_n\pm b_n)=A\pm B. $

证明 因为  $ \lim_{n\to\infty}a_n=A $，由极限定义， $ \forall\varepsilon>0,\exists N_1\in\mathbb{N} $，使得当  $ n>N_1 $ 时，有

 $$ \left|a_{n}-A\right|<\frac{\varepsilon}{2}. $$ 

另一方面， $ \lim_{n\to\infty}b_n=B $，故对上述  $ \varepsilon,\exists N_2\in\mathbb{N} $，使得当  $ n>N_2 $ 时，有

 $$ |b_{n}-B|<\frac{\varepsilon}{2}. $$ 

进而知，当  $ n > N = \max\{N_{1}, N_{2}\} $ 时，便有

 $$ \left|\left(a_{n}\pm b_{n}\right)-\left(A\pm B\right)\right|\leqslant\left|a_{n}-A\right|+\left|b_{n}-B\right|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon. $$ 

再由极限定义，

 $$ \lim_{n\to\infty}(a_{n}\pm b_{n})=A\pm B. $$ 