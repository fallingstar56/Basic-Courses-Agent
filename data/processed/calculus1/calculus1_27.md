 $$ \begin{aligned}a_{n}&=\left(1+\frac{1}{n}\right)^{n}=1+\sum_{k=1}^{n}C_{n}^{k}\frac{1}{n^{k}}\\&=1+\sum_{k=1}^{n}\frac{n(n-1)\cdots(n-k+1)}{k!}\cdot\frac{1}{n^{k}}\\&=1+\sum_{k=1}^{n}\frac{1}{k!}\Big(1-\frac{1}{n}\Big)\Big(1-\frac{2}{n}\Big)\cdots\Big(1-\frac{k-1}{n}\Big)\\&\leqslant1+\sum_{k=1}^{n+1}\frac{1}{k!}\Big(1-\frac{1}{n+1}\Big)\Big(1-\frac{2}{n+1}\Big)\cdots\Big(1-\frac{k-1}{n+1}\Big)\\&=\Big(1+\frac{1}{n+1}\Big)^{n+1}=a_{n+1}.\\ \end{aligned} $$ 

另一方面，

 $$ \begin{align*}a_{n}&=1+\sum_{k=1}^{n}\frac{1}{k!}\Big(1-\frac{1}{n}\Big)\Big(1-\frac{2}{n}\Big)\cdots\Big(1-\frac{k-1}{n}\Big)\leqslant1+\sum_{k=1}^{n}\frac{1}{k!}\\&\leqslant1+1+\sum_{k=2}^{n}\frac{1}{k(k-1)}=2+\sum_{k=2}^{n}\Big(\frac{1}{k-1}-\frac{1}{k}\Big)<3.\end{align*} $$ 

所以数列 $ \{a_{n}\} $又是有界的，于是由定理1.4.1即得数列 $ \{a_{n}\} $收敛.

记  $ e=\lim_{n\to\infty}\left(1+\frac{1}{n}\right)^{-} $，从例 1.4.1 的证明中可知 e 是一个介于 2 和 3 之间的正实数，它就是我们在中学数学中看到的自然对数的底数。可以证明：e 是一个无理数，它的近似值为  $ e\approx2.71828 $。

令  $ a_{n}=\sum_{k=1}^{n}\frac{1}{k^{2}}(n=1,2,\cdots) $，求证： $ \lim_{n\to\infty}a_{n} $ 存在.

证明  $ \{a_{n}\} $ 显然单调递增，因此，要证  $ \{a_{n}\} $ 收敛，只需证  $ \{a_{n}\} $ 有上界.

注意到  $ \forall n \in N^* $

 $$ 0<a_{n}=\sum_{k=1}^{n}\frac{1}{k^{2}}=1+\sum_{k=2}^{n}\frac{1}{k^{2}}\leqslant1+\sum_{k=2}^{n}\left(\frac{1}{k-1}-\frac{1}{k}\right)=2-\frac{1}{n}<2, $$ 

即  $ \{a_{n}\} $ 有界，于是由定理 1.4.1 推出极限  $ \lim_{n\to\infty}a_{n} $ 存在.

设 a > 1，求证  $ \lim_{n \to \infty} \frac{n}{a^n} = 0 $.

证明 记  $ x_{n}=\frac{n}{a^{n}} $ ，则

 $$ \frac{x_{n+1}}{x_{n}}=\frac{1}{a}\frac{n+1}{n}\rightarrow\frac{1}{a}<1\quad(n\rightarrow\infty). $$ 