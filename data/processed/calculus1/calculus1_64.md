 $ g(x) \neq u_{0} $ 是不能缺少的.

(1)

 $$ f(u)=\left\{\begin{aligned}&1,&u=0,\\ &0,&u\neq0,\end{aligned}\right.\quad g(x)=\left\{\begin{aligned}&1,&x=1,\\ &0,&x\neq1,\end{aligned}\right.\quad u_{0}=0,x_{0}=1; $$ 

(2)

 $$ f(u)=\left\{\begin{aligned}&1,&u=0,\\ &0,&u\neq0,\end{aligned}\right.\quad g(x)=\left\{\begin{aligned}&0,&x=0,\\ &x\sin\frac{1}{x},&x\neq0,\end{aligned}\right.\quad u_{0}=0,x_{0}=0. $$ 

11. 设  $ \lim_{u\to u_0^+}f(u)=A,\lim_{x\to x_0}g(x)=u_0 $ ，且  $ \exists\rho>0 $ ，使得当  $ x\in U(x_0,\rho) $ 时  $ g(x)>u_0 $ 。求证

 $$ \lim_{x\to x_{0}}f(g(x))=\lim_{y\to y_{0}^{+}}f(u)=A. $$ 

12. 设函数  $ f(a, +\infty) $ 内定义，则下列命题等价：

(1)  $ \lim_{x\to+\infty}f(x)=A; $

(2) $ \forall\varepsilon>0,\exists M>0 $，当 $ x_{2}>x_{1}>M $时，就有 $ \left|f(x_{2})-f(x_{1})\right|<\varepsilon; $

(3) 对于 $ (a,+\infty) $内任意一个趋向于 $ +\infty $的点列 $ \{x_{n}\} $，有 $ \lim_{n\to\infty}f(x_{n})=A $.

13. 设  $ f(x) $ 在  $ \mathbb{R} $ 上有定义，并满足  $ f(2x)=f(x) $，如果  $ \lim_{x\to0}f(x)=f(0) $，证明： $ f(x) $ 在  $ \mathbb{R} $ 上为常数.

14. 已知狄利克雷函数  $ D(x)=\left\{\begin{aligned}&1,&x\in\mathbb{Q}\\ &0,&x\notin\mathbb{Q}\end{aligned}\right. $，证明： $ \forall x_{0}\in\mathbb{R},\lim_{x\to x_{0}}D(x) $ 不存在.

15. 试举一个函数  $ f(x) $，它只在一点有极限，在其余点处都没有极限.

### 2.4 无穷小量与无穷大量

定义 2.4.1

(1) 若  $ \lim_{x\to x_{0}}f(x)=0 $，则称当  $ x\to x_{0} $ 时， $ f(x) $ 是无穷小量.

(2) 设  $ f(x) $ 在  $ x_{0} $ 的某个空心邻域内有定义. 若  $ \forall M>0, \exists \delta>0 $, 当  $ x \in U(x_{0}, \delta) $ 时, 就有  $ \left|f(x)\right| > M $, 则称当  $ x \to x_{0} $ 时  $ f(x) $ 为无穷大量, 记作  $ f(x) \to \infty (x \to x_{0}) $.

(3) 设  $  f(x)  $ 在  $ x_{0} $ 的某个空心邻域内有定义. 若  $ \forall M > 0, \exists \delta > 0 $, 当  $ x \in U(x_{0}, \delta) $ 时, 就有  $  f(x) > M(f(x) < -M)  $, 则称当  $ x \to x_{0} $ 时  $  f(x)  $ 为正（负）无穷大量, 记作  $  f(x) \to +\infty (-\infty) (x \to x_{0})  $.

对于其他几种极限过程： $ x \rightarrow x_{0}^{\pm}, x \rightarrow \infty $ 及  $ x \rightarrow \pm \infty $，同样可以定义无穷小量、无穷大量及正（负）无穷大量。读者可以尝试写出这些定义。