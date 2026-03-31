6. 设  $ \lim_{n\to\infty}a_n=A $，利用极限的定义证明：

(1)  $ \lim_{n\to\infty}\frac{a_n}{n}=0 $;

(2)  $ \lim_{n\to\infty}|a_n|=|A| $;

(3)  $ \lim_{n\to\infty}\sqrt{a_n}=\sqrt{A}(A>0) $;

(4)  $ \lim_{n\to\infty}\frac{a_{n+1}}{a_{n}}=1\ (A\neq0) $.

7. 已知  $ \lim_{n\to\infty}a_n=A $，证明：

(1) $ \lim_{n\to\infty}|a_n|=|A| $，反之何时成立？

(2) $ \lim_{n\to\infty}\frac{a_{1}+a_{2}+\cdots+a_{n}}{n}=A $，反之成立吗？

### 1.3 收敛数列的性质

若数列 $ \{a_{n}\} $收敛，则它的极限是唯一的。

证明 假定  $ \lim_{n\to\infty}a_n=A $，同时又有  $ \lim_{n\to\infty}a_n=B.\quad\forall\varepsilon>0 $，由极限定义， $ \exists N_1\in\mathbb{N} $，使得当  $ n>N_1 $ 时，就有  $ \left|a_n-A\right|<\varepsilon/2 $。同时  $ \exists N_2\in\mathbb{N} $，使得当  $ n>N_2 $ 时，就有  $ \left|a_n-B\right|<\varepsilon/2 $。进而知，当  $ n>N=\max\{N_1,N_2\} $ 时，便有

 $$ \left|A-B\right|\leqslant\left|A-a_{n}\right|+\left|a_{n}-B\right|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon. $$ 

而  $ \varepsilon>0 $ 可以是任意正数，从而必有  $ \left|A-B\right|\leqslant0 $，即 A=B.

## 性质 2

在一个收敛数列 $ \{a_{n}\} $中任意添加、删去有限项，或者任意改变有限项的值，不会改变该数列的收敛性与极限值.

证明 设数列  $ \{a_{n}\} $ 的前 k 项  $ a_{1}, a_{2}, \cdots, a_{k} $ 被改变为  $ b_{1}, b_{2}, \cdots, b_{m} $，而 k 项以后的所有项保持不变。记  $ b_{m+i} = a_{k+i}, i = 1, 2, \cdots $，即  $ \{b_{n}\} $ 为数列  $ \{a_{n}\} $ 改变后所得到的数列。

若数列  $ \{a_{n}\} $ 有极限 A，则  $ \forall \varepsilon > 0, \exists N \in \mathbb{N} $ （不妨设  $ N \geqslant k $），使得当 n > N 时，就有

 $$ \left|a_{n}-A\right|<\varepsilon. $$ 

由于 $ b_{m+i}=a_{k+i} $，并且

 $$ k+i>N\Leftrightarrow m+i>m+N-k=N_{1}, $$ 

从而当  $ n > N_{1} $ 时，就有  $ \left|b_{n} - A\right| < \varepsilon $，即  $ \{b_{n}\} $ 收敛于 A.

另一方面，数列 $ \{a_{n}\} $也可看作 $ \{b_{n}\} $改变后所得到的数列，所以，若 $ \{b_{n}\} $收敛，则 $ \{a_{n}\} $收敛。从而若 $ \{a_{n}\} $发散，则 $ \{b_{n}\} $必发散。