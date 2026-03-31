#### ▶ 例 3.2.10

求反正弦函数  $ \arcsin x $ 与反正切函数  $ \arctan x $ 的导数.

解 由于  $ y=\arcsin x $ 与  $ x=\sin y $ 互为反函数，根据定理 3.2.3，

 $$ \left(\arcsin x\right)^{\prime}=\frac{1}{\left(\sin y\right)^{\prime}}=\frac{1}{\cos y}=\frac{1}{\sqrt{1-\sin^{2}y}}=\frac{1}{\sqrt{1-x^{2}}}. $$ 

类似地，由于  $ y=\arctan x $ 与  $ x=\tan y $ 互为反函数，故

 $$ \left(\arctan x\right)^{\prime}=\frac{1}{\left(\tan x\right)^{\prime}}=\cos^{2}y=\frac{1}{1+\tan^{2}y}=\frac{1}{1+x^{2}}. $$ 

同理可得

 $$ \left(\operatorname{arccos}x\right)^{\prime}=\frac{-1}{\sqrt{1-x^{2}}}\ ;\quad\left(\operatorname{arccot}x\right)^{\prime}=\frac{-1}{1+x^{2}}. $$ 

▶ 例 3.2.11 ……

求函数  $ y=e^{x}+\arctan x $ 的反函数  $ x=x(y) $ 的导数.

解 函数  $ y=e^{x}+\arctan x $ 在 R 上严格单调递增且可导，且

 $$ y^{^{\prime}}=e^{x}+\frac{1}{x^{2}+1}=\frac{e^{x}\left(x^{2}+1\right)+1}{x^{2}+1}. $$ 

根据定理 3.2.3，其反函数  $ x = x(y) $ 可导并且

 $$ x^{\prime}(y)=\frac{1}{y^{\prime}(x)}=\frac{x^{2}+1}{\mathrm{e}^{x}(x^{2}+1)+1}, $$ 

其中右端表达式中的 x 理解为  $ x = x(y) $，因而右端表达式为 y 的复合函数。

我们将已经得到的一些常见函数，其中包括基本初等函数的导数列表如下：

(1) $ C^{\prime}=0(C $为任意常数 $;

(2) $ (x^{a})^{\prime}=\alpha x^{a-1} $;

(3) $ (a^{x})^{\prime}=a^{x}\ln a(a>0) $;  $ (e^{x})^{\prime}=e^{x} $;

(4) $ \left(\log_{a}x\right)^{\prime}=\frac{1}{x\ln a}(a>0,a\neq1) $;  $ \left(\ln|x|\right)^{\prime}=\frac{1}{x}(x\neq0) $;

(5) $ (\sin x)'=\cos x;(\cos x)'=-\sin x; $

(6)  $ (\tan x)' = \sec^2 x $;  $ (\cot x)' = -\csc^2 x $;

(7)  $ (\sec x)' = \tan x \sec x $;  $ (\csc x)' = -\cot x \csc x $;

(8) $ (\arcsin x)^{\prime}=\frac{1}{\sqrt{1-x^{2}}} $;  $ (\arccos x)^{\prime}=\frac{-1}{\sqrt{1-x^{2}}} $;

(9)  $ (\arctan x)' = \frac{1}{1 + x^2} $;  $ (\operatorname{arccot} x)' = \frac{-1}{1 + x^2} $;

(10) $ (\ln|x+\sqrt{x^{2}\pm a^{2}}|)^{\prime}=\frac{1}{\sqrt{x^{2}\pm a^{2}}} $