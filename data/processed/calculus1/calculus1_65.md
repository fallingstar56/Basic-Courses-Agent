例如，设  $ f(x) $ 在  $ (a, +\infty) $ 内定义。若  $ \forall M > 0, \exists A \geqslant a $，当 x > A 时，就有  $ f(x) < -M $，则称当  $ x \to +\infty $ 时， $ f(x) $ 为负无穷大量，记作  $ f(x) \to -\infty (x \to +\infty) $。

(1) 当  $ x \to 0^{+} $ 时， $ f(x) = \ln x $ 为负无穷大量；当  $ x \to +\infty $ 时， $ f(x) = \ln x $ 为正无穷大量；当  $ x \to 1 $ 时， $ f(x) = \ln x $ 为无穷小量。

(2) 当  $ x \rightarrow +\infty $ 时， $ f(x) = \mathrm{e}^{x} $ 是正无穷大量；当  $ x \rightarrow -\infty $ 时， $ f(x) = \mathrm{e}^{x} $ 是无穷小量.

(3) 当  $ x \to \infty $ 时， $ f(x) = 1/x $ 是无穷小量；当  $ x \to 0^{+} $ 时， $ f(x) = 1/x $ 是正无穷大量；当  $ x \to 0^{-} $ 时， $ f(x) = 1/x $ 是负无穷大量。

(4) 当  $ x \to x_{0} $ 时，若  $ f(x) $ 为（正，负）无穷大量，则  $ \frac{1}{f(x)} $ 为无穷小量；反之，若  $ f(x) $ 为无穷小量，且  $ \exists \delta > 0 $，当  $ x \in U(x_{0}, \delta) $ 时， $ f(x) \neq 0 $，则  $ \frac{1}{f(x)} $ 为无穷大量.

不难看出，当  $ x \rightarrow 0 $ 时，x 与  $ x^{2} $ 都是无穷小量，但是它们趋向于 0 的速度却有差别；同样，当  $ x \rightarrow +\infty $ 时，x 和  $ e^{x} $ 都是正无穷大量，但趋向于无穷的快慢也是不同的。为了描述这一现象，我们引入下面的概念。

设当  $ x \rightarrow x_{0} $ 时， $ f(x) $ 与  $ g(x) $ 都是无穷小量.

(1) 若  $ \lim_{x\to x_{0}}\frac{f(x)}{g(x)}=0 $，则称当  $ x\to x_{0} $ 时  $ f(x) $ 是  $ g(x) $ 的高阶无穷小量，记作

 $$ f(x)=o(g(x))\quad(x\rightarrow x_{0}). $$ 

(2) 若  $ \lim_{x\to x_0}\frac{f(x)}{g(x)}=c\neq0 $，则称当  $ x\to x_0 $ 时， $ f(x) $ 与  $ g(x) $ 是同阶无穷小量.

特别地，若  $ \lim_{x\to x_0}\frac{f(x)}{g(x)}=1 $，则称当  $ x\to x_0 $ 时， $ f(x) $ 与  $ g(x) $ 是等价无穷小量，记作

 $$ f(x)\sim g(x)(x\rightarrow x_{0}). $$ 

(3) 若  $ \exists k \in \mathbb{N}^* $，使得  $ \lim_{x \to x_0} \frac{f(x)}{(x - x_0)^k} = c \neq 0 $，则称当  $ x \to x_0 $ 时， $ f(x) $ 是 k 阶无穷小量。

上面定义中的极限过程  $ x \rightarrow x_{0} $ 可以换成其他几种极限过程： $ x \rightarrow x_{0}^{\pm}, x \rightarrow \infty $ 及  $ x \rightarrow \pm \infty $.

注 对单侧极限过程  $ x \rightarrow x_{0}^{\pm} $，也可以考虑  $ \alpha > 0 $ 不是整数时的  $ \alpha $ 阶无穷小量：