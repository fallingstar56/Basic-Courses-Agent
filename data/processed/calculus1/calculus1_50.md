注 定义 2.2.1 的关键在于描述当自变量 x 越来越逼近  $ x_{0} $ (但永远不等于  $ x_{0} $) 的过程中，函数值  $ f(x) $ 的变化趋势。所以，函数 f 在点  $ x_{0} $ 的极限是否存在，与函数 f 在  $ x_{0} $ 点是否有定义及 f 在  $ x_{0} $ 点取什么值无关。

如果限制自变量 x 只能在  $ x_{0} $ 的一侧变化，就得到“单侧极限”的概念。

(1) 设函数  $ f $ 在  $ (x_0, x_0 + \rho) $ 内定义， $ \rho > 0 $， $ A \in \mathbb{R} $。如果  $ \forall \varepsilon > 0 $， $ \exists \delta > 0 $，当  $ x \in (x_0, x_0 + \delta) $ 时，就有  $ |f(x) - A| < \varepsilon $，则称  $ A $ 为  $ f(x) $ 在点  $ x_0 $ 的右极限。或者说当  $ x $ 趋向于  $ x_0^+ $ 时， $ f(x) $ 趋向于  $ A $。记作  $ \lim_{x \to x_0^+} f(x) = A $，或  $ f(x) \to A(x \to x_0^+) $。

(2) 设函数  $  f  $ 在  $  (x_0 - \rho, x_0) (\rho > 0)  $ 内定义， $  A \in \mathbb{R}  $。若  $  \forall \varepsilon > 0  $， $  \exists \delta > 0  $，当  $  x \in (x_0 - \delta, x_0)  $ 时，有  $  |f(x) - A| < \varepsilon  $，则称  $  A  $ 为  $  f(x)  $ 在  $  x_0  $ 点的左极限。记作  $  \lim_{x \to x_0^-} f(x) = A  $，或  $  f(x) \to A(x \to x_0^-)  $。

由上述定义不难验证：

命题 2.2.1

设函数 f 在点  $ x_{0} $ 的某个空心邻域  $ U(x_{0}, \rho) $ 内定义. 则  $ \lim_{x \to x_{0}} f(x) = A $ 的充分必要条件是： $ \lim_{x \to x_{0}^{+}} f(x) = A $ 并且  $ \lim_{x \to x_{0}^{-}} f(x) = A $.

事实上，必要性显然，下证充分性。由于  $ \lim_{x\to x_0^{+}}f(x)=A $ 且  $ \lim_{x\to x_0^{-}}f(x)=A $， $ \forall\varepsilon>0,\exists\delta_1>0 $ 当  $ x\in(x_0,x_0+\delta_1) $ 时，有  $ \left|f(x)-A\right|<\varepsilon $。同时， $ \exists\delta_2>0 $ 当  $ x\in(x_0-\delta_2,x_0) $ 时，有  $ \left|f(x)-A\right|<\varepsilon $。若记  $ \delta=\min\{\delta_1,\delta_2\} $，则当  $ x\in U(x_0,\delta) $ 时，有  $ \left|f(x)-A\right|<\varepsilon $。由定义可得  $ \lim f(x)=A $。

▶ 例 2.2.1 ……

设  $ x_{0} \in \mathbb{R} $ 为一固定点，求证： $ \lim \cos x = \cos x_{0} $

证明 注意到

 $$ \begin{aligned}\left|\cos x-\cos x_{0}\right|&=\left|2\sin\frac{x+x_{0}}{2}\sin\frac{x-x_{0}}{2}\right|\\&\leqslant\left|x-x_{0}\right|,\end{aligned} $$ 

于是  $ \forall \varepsilon > 0 $，可取  $ \delta = \varepsilon $。只要  $ 0 < |x - x_{0}| < \delta $，就有

 $$ \left|\cos x-\cos x_{0}\right|<\left|x-x_{0}\right|<\varepsilon, $$ 

由极限定义知  $ \lim_{x\to x_{0}}\cos x=\cos x_{0} $

类似地有， $ \lim_{x\to x_{0}}\sin x=\sin x_{0} $