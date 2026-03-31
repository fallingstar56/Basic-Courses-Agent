 $$ [a,b] 上连续，记作  $ f\in C[a,b]. $$ 

#### 定理 2.6.1（介值定理）

设  $ f \in C[a, b] $,  $ f(a) \neq f(b) $，则对介于  $ f(a) $ 与  $ f(b) $ 之间的每个数 c，都存在  $ \xi \in (a, b) $，使  $ f(\xi) = c $.

证明 （1）先考虑  $ f(a) $ 与  $ f(b) $ 不同号的情形. 不妨设  $ f(a)<0, f(b)>0 $ （在相反情形可以考虑 -f）.

令  $ E=\left\{x\in[a,b]\mid f(x)<0\right\} $，因为  $ f(a)<0 $，故  $ a\in E\neq\varnothing $，令  $ \xi=\sup E $，显然  $ \xi\in[a,b] $。下面证明  $ f(\xi)=0 $。

若  $ f(\xi)>0 $ ，由于 f 在点  $ \xi $ (左) 连续，由极限的保号性， $ \exists x_{0}<\xi $ 使得当  $ x_{0}<x\leqslant\xi $ 时  $ f(x)>0 $ 。这与  $ \xi=\sup E $ 矛盾。若  $ f(\xi)<0 $ ，由于  $ f(b)>0 $ ，故  $ \xi<b $ ，而 f 在点  $ \xi $ (右) 连续，由极限的保号性， $ \exists x_{1}\in(\xi,b) $ 使得当  $ \xi\leqslant x<x_{1} $ 时  $ f(x)<0 $ 从而  $ [a,x_{1}]\subseteq E $ 。这也和  $ \xi=\sup E $ 矛盾。所以  $ f(\xi)=0 $ 。再注意到  $ f(a)<0,f(b)>0 $ ，于是  $ \xi\in(a,b) $ 。

(2) 一般情况下，令  $ g(x)=f(x)-c $，则  $ g(a) $ 与  $ g(b) $ 异号，由(1)中讨论，存在  $ \xi\in(a,b) $，使得  $ g(\xi)=0 $，即  $ f(\xi)=c $。

#### ▶ 例 2.6.1

设 m>0 为奇数，则多项式  $ f(x)=x^{m}+a_{1}x^{m-1}+\cdots+a_{m-1}x+a_{m} $ 至少有一个实根，其中  $ a_{1}, a_{2}, \cdots, a_{m} $ 为实数.

证明 注意到当  $ x \to +\infty $ 时， $ f(x) \to +\infty $，而当  $ x \to -\infty $ 时  $ f(x) \to -\infty $，故存在正数 M，使得  $ f(-M) < 0 $，且  $ f(M) > 0 $。在  $ [-M, M] $ 上对 f 应用定理 2.6.1 便知在区间  $ (-M, M) $ 内  $ f(x) $ 至少有一个实根。

为叙述方便，用 $ \langle a,b\rangle $表示分别以a、b为左、右端点的开、闭或半开半闭区间.

#### ▶ 例 2.6.2

设 f 在  $ \langle a, b \rangle $ 上连续（即 f 在  $ (a, b) $ 内连续，并且当  $ \langle a, b \rangle $ 的某个端点在  $ \langle a, b \rangle $ 内时，f 在此端点处单侧连续），则 f 的值域 J 构成一个区间.

证明 要证 J 构成一个区间，只需证  $ \forall y_{1}, y_{2} \in J $，且  $ y_{1} < y_{2} $，有  $ [y_{1}, y_{2}] \subseteq J $ 即可.

由于 J 是 f 的值域，故  $ \exists x_{1}, x_{2} \in (a, b) $ 使得  $ f(x_{1}) = y_{1}, f(x_{2}) = y_{2} $. 而  $ \langle a, b \rangle $ 也是一个区间，所以  $ \left[x_{1}, x_{2}\right] \subseteq \langle a, b \rangle $ （或  $ \left[x_{2}, x_{1}\right] \subseteq \langle a, b \rangle $）。对 f 在  $ \left[x_{1}, x_{2}\right] $ 上应用介值定理即知， $ \left[y_{1}, y_{2}\right] $ 中每个点 y 都在 f 的值域内，即  $ \left[y_{1}, y_{2}\right] \subseteq J $，所以 J 构成一个区间。