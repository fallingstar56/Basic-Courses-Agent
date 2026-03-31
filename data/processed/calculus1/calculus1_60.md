可以找到  $ x_{\delta} \in U(x_{0}, \delta) $，满足  $ \left|f(x_{\delta}) - A\right| \geqslant \varepsilon_{0} $。于是，分别取  $ \delta = \rho, \frac{\rho}{2}, \cdots, \frac{\rho}{n}, \cdots $，可以相应地得到点列  $ \{x_{n}\} $ 满足： $ x_{n} \in U\left(x_{0}, \frac{\rho}{n}\right) \subseteq U(x_{0}, \rho) $ 并且  $ \left|f(x_{n}) - A\right| \geqslant \varepsilon_{0} (n = 1, 2, \cdots) $。

注意到  $ 0 < |x_{n} - x_{0}| < \frac{\rho}{n} $ (n = 1, 2, …)，从而  $ \{x_{n}\} $ 收敛于  $ x_{0} $。由定理条件知应有  $ \lim_{n \to \infty} f(x_{n}) = A $，这与  $ |f(x_{n}) - A| \geqslant \varepsilon_{0} $ (n = 1, 2, …) 相矛盾。于是  $ \lim_{x \to x_{0}} f(x) = A $ 成立。

(3)  $ \Rightarrow $ (1) 设  $ \lim_{x\to x_0}f(x)=A $，则  $ \forall\varepsilon>0,\exists\delta>0 $，当  $ x\in U(x_0,\delta) $ 时，就有  $ \left|f(x)-A\right|<\frac{\varepsilon}{2} $。于是当  $ x_1,x_2\in U(x_0,\delta) $ 时，就有

 $$ \left|f(x_{1})-f(x_{2})\right|\leqslant\left|f(x_{1})-A\right|+\left|A-f(x_{2})\right|<\varepsilon. $$ 

注 将定理 2.3.4 中的极限过程  $ x \rightarrow x_{0} $ 换成其他五种极限过程的任一种，结论仍然成立. 例如：

设函数 f 在  $ (a, +\infty) $ 内定义，则下列命题等价：

(1) $ \forall\varepsilon>0,\exists M>0 $，当 $ x_{2}>x_{1}>M $时，就有 $ \left|f(x_{2})-f(x_{1})\right|<\varepsilon; $

(2)  $ \exists A \in \mathbb{R} $，对于 $ (a, +\infty) $内任意一个趋向于 $ +\infty $的点列 $ \{x_n\} $，有 $ \lim_{n \to \infty} f(x_n) = A $;

(3)  $ \lim_{x\to+\infty}f(x)=A. $

读者可以尝试写出这些定理并给出证明.

▶ 例 2.3.6 ……

证明 $ \lim_{x\to0}\sin\frac{1}{x} $不存在.

证明 对于下面两个收敛于 0 的点列

 $$ x_{n}=\frac{1}{2n\pi},\quad y_{n}=\frac{1}{2n\pi+\frac{\pi}{2}}\quad(n\in\mathbb{N}), $$ 

有

 $$ \lim_{n\to+\infty}f(x_{n})=\lim_{n\to+\infty}\sin(2n\pi)=0, $$ 

 $$ \lim_{n\to+\infty}f(y_{n})=\lim_{n\to+\infty}\sin\left(2n\pi+\frac{\pi}{2}\right)=1, $$ 

于是由定理 2.3.4 可推出  $ \lim f(x) $ 不存在.

由图 2.3.2 可以看出，当  $ x \rightarrow 0 $ 时，曲线  $ y = \sin \frac{1}{x} $ 在 -1 和 1 之间震荡，不趋于任何数.