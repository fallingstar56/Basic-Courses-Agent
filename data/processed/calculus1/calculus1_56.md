 $$ \frac{1}{2}(A+B)>g(x). $$ 

(2) 假定 A < B，由(1)知，存在  $ \delta > 0 $，使得当  $ x \in U(x_{0}, \delta) $ 时，有  $ g(x) > f(x) $。这与题设相矛盾。故  $ A \geqslant B $。

若在性质 3 中取  $ g(x) \equiv 0 $，即得：

当 $ \lim_{x\to x_{0}}f(x)=A>0 $时，存在 $ \delta>0 $，使得 $ \forall x\in U(x_{0},\delta) $，有 $ f(x)>0 $。反之，若存在 $ \rho>0 $，使得当 $ x\in U(x_{0},\rho) $时， $ f(x)\geqslant0 $，则 $ A\geqslant0 $。

这个结论常称为极限的保号性.

#### 定理 2.3.1（四则运算）

设  $ \lim_{x\to x_{0}}f(x)=A,\lim_{x\to x_{0}}g(x)=B $ , 则

(1) 对任意实数  $ c, \lim_{x \to x_{0}} [cf(x)] = cA; $

(2)  $ \lim_{x\to x_0}[f(x)\pm g(x)]=A\pm B; $

(3)  $ \lim_{x \to x_0} [f(x) \cdot g(x)] = A \cdot B $;

(4) 当  $ B \neq 0 $ 时， $ \lim_{x \to x_{0}} \frac{f(x)}{g(x)} = \frac{A}{B} $.

#### 定理 2.3.2（夹逼原理）

设函数  $ f, g, h $ 在  $ U(x_{0}, \rho) $ 内定义，并且满足

 $$ f(x)\leqslant g(x)\leqslant h(x),\quad x\in U(x_{0},\rho). $$ 

如果  $ \lim_{x\to x_{0}}f(x)=\lim_{x\to x_{0}}h(x)=A $，则  $ \lim_{x\to x_{0}}g(x)=A $.

定理 2.3.1 与定理 2.3.2 的证明与数列情形完全类似，这里不再赘述.

#### 定理 2.3.3（复合函数极限）

设  $ \lim_{x\to x_{0}}g(x)=u_{0},\lim_{u\to u_{0}}f(u)=A $ ，且当  $ x\neq x_{0} $ 时  $ g(x)\neq u_{0} $ ，则有

 $$ \lim_{x\to x_{0}}f(g(x))=\lim_{x\to x_{0}}f(u)=A. $$ 

证明  $ \forall \varepsilon > 0 $ ，由于  $ \lim_{u \to u} f(u) = A $ ，存在  $ \delta_{1} > 0 $ ，当  $ u \in U(u_{0}, \delta_{1}) $ 时，有

 $$ \left|f(u)-A\right|<\varepsilon. $$ 

又由于 $ \lim_{x\to x_{0}}g(x)=u_{0} $，故对上述 $ \delta_{1}>0 $，存在 $ \delta>0 $，只要 $ x\in U(x_{0},\delta) $，就有

 $$ 0<\mid g(x)-u_{0}\mid<\delta_{1} $$ 

(注意当  $ x \neq x_{0} $ 时  $ g(x) \neq u_{0} $，从而)

 $$ \left|f(g(x))-A\right|<\varepsilon(\forall x\in U(x_{0},\hat{\delta})). $$ 