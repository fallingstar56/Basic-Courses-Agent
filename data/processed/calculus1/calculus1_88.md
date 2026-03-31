#### ▶ 例 3.2.3

设  $ f(x)=(x-x_{0})^{k}g(x) $，其中  $ k\in\mathbb{N}^{*} $， $ g(x) $ 在  $ x_{0} $ 点连续且  $ g(x_{0})\neq0 $，此时称点  $ x_{0} $ 为  $ f(x) $ 的 k 重零点。求证：若  $ g(x) $ 在点  $ x_{0} $ 的某个邻域内可导，那么点  $ x_{0} $ 为  $ f^{\prime}(x) $ 的 k-1 重零点。

证明

 $$ \begin{align*}f^{\prime}(x)&=k\left(x-x_{0}\right)^{k-1}g(x)+\left(x-x_{0}\right)^{k}g^{\prime}(x)\\&=\left(x-x_{0}\right)^{k-1}(kg(x)+\left(x-x_{0}\right)g^{\prime}(x)).\end{align*} $$ 

而  $ kg(x) + (x - x_{0})g'(x) $ 在点  $ x_{0} $ 的值为  $ kg(x_{0}) \neq 0 $，所以点  $ x_{0} $ 为  $ f'(x) $ 的 k - 1 重零点.

定理 3.2.2（复合函数求导数的链式法则）……

设  $ \varphi(x) $ 在点  $ x_{0} $ 可导， $ f(u) $ 在点  $ u_{0}=\varphi(x_{0}) $ 处可导。则复合函数  $ h(x)=f(\varphi(x)) $ 在点  $ x_{0} $ 可导，并且

 $$ h^{\prime}(x_{0})=f^{\prime}(\varphi(x_{0}))\varphi^{\prime}(x_{0}). $$ 

证明 令

 $$ g(u)=\left\{\begin{aligned}&\frac{f(u)-f(u_{0})}{u-u_{0}},&u\neq u_{0},\\ &f^{\prime}(u_{0}),&u=u_{0}.\end{aligned}\right. $$ 

注意到  $ u_{0}=\varphi(x_{0}) $，下面等式在点  $ x_{0} $ 的某个空心邻域内成立：

 $$ \frac{f(\varphi(x))-f(\varphi(x_{0}))}{x-x_{0}}=g(\varphi(x))\bullet\frac{\varphi(x)-\varphi(x_{0})}{x-x_{0}} $$ 

(当  $ \varphi(x)=\varphi(x_{0})=u_{0} $ 时等式两端都等于零). 又因为  $ \varphi(x) $ 在点  $ x_{0} $ 连续, 从而当  $ x \to x_{0} $ 时,  $ \varphi(x) \to \varphi(x_{0}) = u_{0} $. 再注意到  $ \lim_{x \to 0} g(u) = f'(u_{0}) = g(u_{0}) $, 即得

 $$ \begin{align*}h^{\prime}(x_{0})&=\lim_{x\to x_{0}}\frac{h(x)-h(x_{0})}{x-x_{0}}=\lim_{x\to x_{0}}\frac{f(\varphi(x))-f(\varphi(x_{0}))}{x-x_{0}}\\&=\lim_{x\to x_{0}}g(\varphi(x))\bullet\frac{\varphi(x)-\varphi(x_{0})}{x-x_{0}}=f^{\prime}(\varphi(x_{0}))\varphi^{\prime}(x_{0}).\end{align*} $$ 

注 由复合函数的求导法则立即可得复合函数的求微分法则. 设函数  $ u=\varphi(x) $ 在点  $ x_{0} $ 可微， $ y=f(u) $ 在点  $ u_{0}=\varphi(x_{0}) $ 处可微，则复合函数  $ y=f(\varphi(x)) $ 在点  $ x_{0} $ 处可微，并且

 $$ \mathrm{d}y=f^{\prime}(u_{0})\mathrm{d}u=f^{\prime}(\varphi(x_{0}))\varphi^{\prime}(x_{0})\mathrm{d}x. $$ 

从上式可以看到,无论 u 是 y 的自变量还是中间变量,y 的微分在形式上都可以写为

 $$ \mathrm{d}y=f^{\prime}(u)\mathrm{d}u. $$ 

因为当  $ u = \varphi(x) $ 时， $ du = \varphi'(x)dx $，代入上式便得到同样的表达式：

 $$ \mathrm{d}y=f^{\prime}(\varphi(x))\varphi^{\prime}(x)\mathrm{d}x=f^{\prime}(u)\mathrm{d}u. $$ 