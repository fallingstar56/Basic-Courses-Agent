▶ 例 3.2.8

设  $ u(x) $,  $ v(x) $ 都在点 x 处可导，且  $ u(x) > 0 $,  $ f(x) = u(x)^{v(x)} $, 求  $ f'(x) $.

解

 $$ \begin{align*}f^{\prime}(x)&=(\mathrm{e}^{v(x)\ln u(x)})^{\prime}=\mathrm{e}^{v(x)\ln u(x)}(v(x)\ln u(x))^{\prime}\\&=u(x)^{v(x)}\Big(v^{\prime}(x)\ln u(x)+v(x)\frac{u^{\prime}(x)}{u(x)}\Big).\end{align*} $$ 

▶ 例 3.2.9 ……

设  $ f(x)=\left(\frac{x+1}{x-1}\right)^{1/2}(x^{2}(2x+3))^{1/3} $，求  $ f'(x) $.

 $$ \ln|f(x)|=\frac{1}{2}\left(\ln|x+1|-\ln|x-1|\right)+\frac{1}{3}\left(2\ln|x|+\ln|2x+3|\right). $$ 

将此等式左端看作 x 的复合函数，应用定理 3.2.2，对等式两端关于 x 求导，可得

 $$ \begin{aligned}\frac{f^{\prime}(x)}{f(x)}&=\frac{1}{2}\Big(\frac{1}{x+1}-\frac{1}{x-1}\Big)+\frac{1}{3}\Big(\frac{2}{x}+\frac{2}{(2x+3)}\Big)\\&=\frac{-1}{x^{2}-1}+\frac{2(x+1)}{x(2x+3)},\end{aligned} $$ 

 $$ f^{\prime}(x)=\left(\frac{x+1}{x-1}\right)^{1/2}(x^{2}(2x+3))^{1/3}\left(\frac{-1}{x^{2}-1}+\frac{2(x+1)}{x(2x+3)}\right). $$ 

类似于例 3.2.9 这样，对有多个因子连乘的函数求导时先取对数再两端求导常常会较为简便.

定理 3.2.3（反函数求导数法则）

设 f 在  $ (a,b) $ 内严格单调且连续， $ x_{0}\in(a,b) $， $ f^{\prime}(x_{0})\neq0 $，则反函数  $ x=f^{-1}(y) $ 在  $ y_{0}=f(x_{0}) $ 处可导，并且  $ (f^{-1})^{\prime}(y_{0})=\frac{-1}{f^{\prime}(x_{0})} $.

证明 在  $ y_{0} $ 附近任取  $ y, y = f(x) $，则  $ x = f^{-1}(y) $。由 f 严格单调及连续可知反函数  $ f^{-1} $ 亦连续且严格单调（定理 2.6.3），因此当  $ y \neq y_{0} $ 且  $ y \to y_{0} $ 时有  $ x \neq x_{0} $ 且  $ x \to x_{0} $，于是

 $$ \begin{aligned}\lim_{y\to y_{0}}\frac{f^{-1}(y)-f^{-1}(y_{0})}{y-y_{0}}&=\lim_{y\to y_{0}}\frac{x-x_{0}}{f(x)-f(x_{0})}\\&=\lim_{x\to x_{0}}\frac{1}{\frac{f(x)-f(x_{0})}{x-x_{0}}}=\frac{1}{f^{\prime}(x_{0})}.\end{aligned} $$ 

这一结论也可以写为

 $$ \frac{\mathrm{d}x}{\mathrm{d}y}=\frac{1}{\frac{\mathrm{d}y}{\mathrm{d}x}}. $$ 