证明 （1）由于  $ \lim_{n\to\infty}a_n=A $，取  $ \varepsilon=\frac{1}{2}(A-B) $，则  $ \exists N_1\in\mathbb{N} $，使得当  $ n>N_1 $ 时，就有

 $$ a_{n}-A>-\varepsilon=\frac{1}{2}(B-A), $$ 

即

 $$ a_{n}>\frac{1}{2}(A+B). $$ 

同时 $ \lim_{n\to\infty}b_n=B $，故 $ \exists N_2\in\mathbb{N} $，使得当 $ n>N_2 $时，就有

 $$ b_{n}-B<\varepsilon=\frac{1}{2}(A-B), $$ 

即

 $$ b_{n}<\frac{1}{2}(A+B). $$ 

令  $ N = \max\{N_{1}, N_{2}\} $，则当 n > N 时，便有

 $$ b_{n}<\frac{1}{2}(A+B)<a_{n}. $$ 

(2) 假定 A < B，由(1)知， $ \exists N \in N $，使得当  $ n > N $ 时  $ b_{n} > a_{n} $。这与  $ a_{n} \geqslant b_{n} $ 相矛盾。故  $ A \geqslant B $。

定理 1.3.1（极限的四则运算）

设 $ \lim_{n\to\infty}a_n=A,\lim_{n\to\infty}b_n=B $，则

(1) 对任意实数 c，有  $ \lim_{n\to\infty}(ca_n)=c\cdot\lim_{n\to\infty}a_n=cA $;

(2)  $ \lim_{n\to\infty}(a_n\pm b_n)=\lim_{n\to\infty}a_n\pm\lim_{n\to\infty}b_n=A\pm B; $

(3)  $ \lim_{n\to\infty}(a_n\cdot b_n)=\lim_{n\to\infty}a_n\cdot\lim_{n\to\infty}b_n=AB; $

(4) 若  $ B \neq 0 $，则有  $ \lim_{n \to \infty} \frac{a_n}{b_n} = \frac{\lim a_n}{n \to \infty} = \frac{A}{\beta} $.

证明 （1）的证明留给读者作为练习. （2）在例 1.2.5 中已给出证明. 下面证明(3)和(4).

(3)  $ \{a_{n}\} $ 为收敛数列，由性质 3 知， $ \{a_{n}\} $ 有界，即  $ \exists M>0 $，使得  $ \forall n\in\mathbb{N}^{*} $，有  $ \left|a_{n}\right|\leqslant M $。又因为  $ A=\lim_{n\to\infty}a_{n} $， $ B=\lim_{n\to\infty}b_{n} $，由极限定义， $ \forall\varepsilon>0 $， $ \exists N\in\mathbb{N} $，使得当 n>N 时，同时有

 $$ \left|a_{n}-A\right|<\frac{\varepsilon}{2(1+\left|B\right|)},\quad\left|b_{n}-B\right|<\frac{\varepsilon}{2M}. $$ 