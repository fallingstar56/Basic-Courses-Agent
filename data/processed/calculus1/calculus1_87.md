#### 定理 3.2.1（导数的四则运算）

设 f, g 在点  $ x_{0} $ 处可导，则  $ cf(c $ 为任意常数 $ ) $， $ f+g $ 与  $ f\cdot g $ 都在点  $ x_{0} $ 处可导；如果  $ g(x_{0})\neq0 $，则  $ \frac{f}{g} $ 也在点  $ x_{0} $ 处可导，并且

(1) $ (f+g)'(x_{0})=f'(x_{0})+g'(x_{0}) $;

(2) $ (cf)'(x_{0})=cf'(x_{0}); $

(3) $ (fg)'(x_{0})=f'(x_{0})g(x_{0})+f(x_{0})g'(x_{0}); $

(4)  $ \left(\frac{f}{g}\right)'(x_{0})=\frac{f'(x_{0})g(x_{0})-f(x_{0})g'(x_{0})}{g^{2}(x_{0})} $.

证明 (1) 与 (2) 可由导数定义与极限的运算性质得到.

(3)

 $$ \begin{aligned}(fg)^{\prime}(x_{0})=&\lim_{h\to0}\frac{f(x_{0}+h)g\left(x_{0}+h\right)-f(x_{0})g(x_{0})}{h}\\=&\lim_{h\to0}\Biggl[g(x_{0}+h)\frac{f(x_{0}+h)-f(x_{0})}{h}\\&+f(x_{0})\frac{g(x_{0}+h)-g(x_{0})}{h}\Biggr]\\=&f^{\prime}(x_{0})g(x_{0})+f(x_{0})g^{\prime}(x_{0}).\end{aligned} $$ 

(4) 可以类似于(3)证得，留给读者作为课后练习.

▶ 例 3.2.1 ……

设  $ f(x)=\frac{\ln x}{x}+\mathrm{e}^{x}\sin x $，求  $ f'(x) $.

解 根据定理 3.2.1，

 $$ f^{\prime}(x)=\left(\frac{\ln x}{x}\right)^{\prime}+(e^{x}\sin x)^{\prime}=\frac{1-\ln x}{x^{2}}+e^{x}\sin x+e^{x}\cos x. $$ 

求正切函数  $ \tan x $ 与正割函数  $ \sec x = \frac{1}{\cos x} $ 的导数.

解

 $$ \begin{aligned}\left(\tan x\right)^{\prime}&=\left(\frac{\sin x}{\cos x}\right)^{\prime}=\frac{\left(\sin x\right)^{\prime}\cos x-\left(\cos x\right)^{\prime}\sin x}{\cos^{2}x}\\&=\frac{\cos^{2}x+\sin^{2}x}{\cos^{2}x}=\frac{1}{\cos^{2}x}\quad;\end{aligned} $$ 

 $$ \left(\sec x\right)^{\prime}=\left(\frac{1}{\cos x}\right)^{\prime}=\frac{\sin x}{\cos^{2}x}=\sec x\tan x. $$ 

类似地，可求得余切函数  $ \cot x $ 与余割函数  $ \csc x = \frac{1}{\sin x} $ 的导数为

 $$ \left(\cot x\right)^{\prime}=\frac{-1}{\sin^{2}x};\quad\left(\csc x\right)^{\prime}=-\csc x\cot x. $$ 