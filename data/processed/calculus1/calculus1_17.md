都小于 $ \varepsilon $.

设  $ 0 < |q| < 1 $，求证  $ \lim_{n \to \infty} q^n = 0 $.

证明 对任意正数  $ \varepsilon $，为了使  $ \left|q^{n}-0\right|=\left|q\right|^{n}<\varepsilon $，只要  $ n>\log_{|q|}\varepsilon $ 就可以了。于是可取自然数  $ N\geqslant\log_{|q|}\varepsilon $。当 n>N 时，就有  $ n>\log_{|q|}\varepsilon $，从而有

 $$ \left|q^{n}-0\right|=\left|q\right|^{n}<\varepsilon. $$ 

由极限定义便知 $ \lim_{n\to\infty}q^{n}=0 $

▶ 例 1.2.2 ……

设  $ a_{n}=\frac{2n^{2}+n+2}{n^{2}-3} $，证明  $ \lim_{n\to\infty}a_{n}=2 $.

证明 当  $ n \geqslant 8 $ 时，有

 $$ \left|a_{n}-2\right|=\frac{n+8}{n^{2}-3}\leqslant\frac{2n}{\frac{1}{2}n^{2}}=\frac{4}{n}. $$ 

由此知， $ \forall\varepsilon>0 $，可取自然数 $ N\geqslant\max\left\{8,\frac{4}{\varepsilon}\right\} $，当n>N时，

 $$ \left|a_{n}-2\right|\leqslant\frac{4}{n}<\varepsilon, $$ 

所以 $ \lim_{n\to\infty}a_n=2. $

证明  $ \lim_{n\to\infty}\sqrt[n]{n}=1. $

证明 记  $ a_{n}=\sqrt[n]{n}-1 $，则当  $ n\geqslant2 $ 时，

 $$ n=(1+a_{n})^{n}\geqslant\frac{1}{2}n(n-1)a_{n}^{2}\geqslant\frac{1}{4}n^{2}a_{n}^{2}, $$ 

从而  $ 0 < a_{n} \leqslant \frac{2}{\sqrt{n}} $. 所以  $ \forall \varepsilon > 0 $，取自然数  $ N \geqslant \max\left\{2, \frac{4}{\varepsilon^{2}}\right\} $，则当 n > N 时，有

 $$ 0<a_{n}\leqslant\frac{2}{\sqrt{n}}<\varepsilon. $$ 

由极限定义得 $ \lim_{n\to\infty}\sqrt[n]{n}=1 $

设 $ \lim_{n\to\infty}a_n=A $. 求证：

(1)  $ \lim_{n\to\infty}e^{a_n}=e^A $;

(2) 如果 A > 0,  $ a_{n} > 0 $, n = 1, 2,  $ \cdots $, 则  $ \lim_{n \to \infty} \ln a_{n} = \ln A $;