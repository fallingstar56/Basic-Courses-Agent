设 f 是  $ \langle a, b \rangle $ 上的单调函数，则 f 在  $ \langle a, b \rangle $ 上连续当且仅当 f 的值域 J 构成一个区间.

证明 若 f 在  $ \langle a, b \rangle $ 上连续，由例 2.6.2 便知 J 构成一个区间.

反之，设 J 构成一个区间。不妨设 f 单增，由于单调函数在其定义域上每一点处的单侧极限存在，若 f 在  $ \langle a, b \rangle $ 中点  $ x_{0} $ 处间断，则  $ \lim_{x \to x_{0}^{+}} f(x) - f(x_{0}) > 0 $ 与  $ f(x_{0}) - \lim_{x \to x_{0}^{-}} f(x) > 0 $ 两者中至少有一个成立。不妨设前者成立，则当  $ x > x_{0} $ 时， $ f(x) \geqslant \lim_{x \to x_{0}^{-}} f(x) $，当  $ x < x_{0} $ 时， $ f(x) \leqslant f(x_{0}) $，从而， $ \forall y \in (f(x_{0}), \lim_{x \to x_{0}^{+}} f(x)) $，不存在  $ x \in [a, b] $，使得  $ f(x) = y $。这与 f 的值域 J 是一个区间相矛盾。于是 f 在  $ \langle a, b \rangle $ 上每一点处连续。

设  $ f $ 是  $ \langle a, b \rangle $ 上严格单调的连续函数。则  $ f $ 的值域为一个区间  $ \langle c, d \rangle $，并且  $ f $ 的反函数  $ f^{-1} $ 在  $ \langle c, d \rangle $ 上连续。

证明 由于 f 在  $ \langle a, b \rangle $ 上连续且严格单调，由定理 2.6.2 知 f 的值域为一个区间  $ \langle c, d \rangle $。进而知，f 的反函数  $ f^{-1} $ 在  $ \langle c, d \rangle $ 上定义且与 f 具有相同的严格单调性。由于  $ f^{-1} $ 的值域就是区间  $ \langle a, b \rangle $，再应用定理 2.6.2 可得  $ f^{-1} $ 是  $ \langle c, d \rangle $ 上的连续函数。

在例 2.5.1 与例 2.5.4 中已经看到，基本初等函数  $ \sin x, \cos x, a^{x}, \log_{a}x = \frac{\ln x}{\ln a} $，以及  $ x^{a} $ 在它们各自的定义域内都是连续的.

再由定理 2.5.1,  $ \tan x = \frac{\sin x}{\cos x} $ 与  $ \cot x = \frac{\cos x}{\sin x} $ 也在各自的定义域内连续。进而定理 2.6.3 告诉我们反三角函数  $ \arcsin x, \arccos x, \arctan x, \arccot x $ 在其定义域内也是连续的。即所有的基本初等函数在它们各自的定义域内都是连续的。

由于所有初等函数都是由基本初等函数通过有限次四则运算与复合运算而成的，应用定理2.5.1，定理2.5.2即得以下定理.

定理 2.6.4

初等函数在其定义区间上连续.

作为本章结尾，我们给出闭区间上连续函数的有界性定理与最大最小值定理。

定理 2.6.5

设  $ f \in C[a, b] $，则