这一事实称为(一阶)微分形式的不变性.

求函数  $ f(x)=\left(\frac{x+1}{x-1}\right)^{\frac{3}{2}} $ 的导数.

解 令  $  g(u) = u^{\frac{3}{2}}  $,  $  h(x) = \frac{x+1}{x-1}  $, 则  $  f(x) = g(h(x))  $, 则

 $$ g^{\prime}(u)=\frac{3}{2}u^{\frac{1}{2}}, $$ 

 $$ h^{\prime}(x)=\frac{(x-1)(x+1)^{\prime}-(x+1)(x-1)^{\prime}}{(x-1)^{2}}=\frac{-2}{(x-1)^{2}}. $$ 

应用定理 3.2.2，可得

 $$ f^{\prime}(x)=g^{\prime}(h(x))\bullet h^{\prime}(x)=\frac{3}{2}\Big(\frac{x+1}{x-1}\Big)^{\frac{1}{2}}\frac{-2}{(x-1)^{2}}=-\frac{3(x+1)^{\frac{1}{2}}}{(x-1)^{\frac{5}{2}}}. $$ 

 $ y=\ln(\tan x^{2}) $，求 dy.

 $$ \begin{aligned}\mathrm{d}y&=\frac{1}{\tan x^{2}}\mathrm{d}(\tan x^{2})=\frac{1}{\tan x^{2}}\frac{1}{\cos^{2}(x^{2})}\mathrm{d}(x^{2})\\&=\frac{2x\mathrm{d}x}{\sin x^{2}\cos x^{2}}.\end{aligned} $$ 

▶ 例 3.2.6 ……

设  $ f(x)=\ln|x|(x\neq0) $，求  $ f'(x) $.

解 当 x>0 时， $ f(x)=\ln x $，故

 $$ f^{\prime}(x)=\frac{1}{x}. $$ 

当 x<0 时， $ f(x)=\ln(-x) $，将  $ f(x) $ 看作  $ \ln u $ 与 u=-x 的复合函数，应用定理 3.2.2 可得

 $$ f^{\prime}(x)=\frac{1}{-x}\bullet(-x)^{\prime}=\frac{1}{x}. $$ 

所以， $ \left(\ln|x|\right)^{\prime}=\frac{1}{x}\left(x\neq0\right) $

▶ 例 3.2.7 ……

设  $ f(x)=\ln\left|x+\sqrt{x^{2}+a^{2}}\right| $，求  $ f'(x) $.

 $$ f^{\prime}(x)=\frac{\left(x+\sqrt{x^{2}\pm a^{2}}\right)^{\prime}}{x+\sqrt{x^{2}\pm a^{2}}}=\frac{1+\frac{1}{2}\left(x^{2}\pm a^{2}\right)^{-\frac{1}{2}}\cdot2x}{x+\sqrt{x^{2}\pm a^{2}}}=\frac{1}{\sqrt{x^{2}\pm a^{2}}}. $$ 