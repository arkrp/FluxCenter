# FluxCenter
This repository contains the function fluxCenter! fluxCenter Computes the center of mass of an irregular polygon using its vertecies!

fluxCenter uses the divergence theorem to perform the integrations needed to find the center of mass! By measuring the flux of a fields across a set of line segments enclosing a space, flux obtains the total divergence in that space! The fields are chosen such that the divergences are 1, x, and y respectively. Therefore the total flux are are:

$\sum\text{flux}\_{f\_1}=\int_{A}^{}1\cdot dA$

$\sum\text{flux}\_{f\_2}=\int_{A}^{}x\cdot dA$

$\sum\text{flux}\_{f\_3}=\int_{A}^{}y\cdot dA$

Using these we can easily obtain the center of mass!

$c\_{mx}=\frac{\int_{A}^{}x\cdot dA}{\int_{A}^{}1\cdot dA}$

$c\_{my}=\frac{\int_{A}^{}y\cdot dA}{\int_{A}^{}1\cdot dA}$

The respective formulas for flux across each line segment are:

$\text{flux}\_{f\_1}(P\_1,P\_2)=\frac{1}{2}\cdot(P\_{1x}+P\_{2x})\cdot(P\_{1y}-P\_{2y})$

$\text{flux}\_{f\_2}(P\_1,P\_2)=\frac{1}{6}\cdot(P\_{1x}^2+P\_{2x}^2+P\_{1x}P\_{2x})\cdot(P\_{1y}-P\_{2y})$

$\text{flux}\_{f\_3}(P\_1,P\_2)=\frac{1}{6}\cdot(P\_{1y}^2+P\_{2y}^2+P\_{1y}P\_{2y})\cdot(P\_{2x}-P\_{1x})$

These formulas were derived from a line integral!

```math
\text{flux}_{\vec{v}}(P_1,P_2)=\int_0^1dt
```

Where in each $v$ is the field with the divergences of 1, x, or y !

```math
\vec{f_1}(\vec{u})=\begin{bmatrix}u_x\\0\end{bmatrix}
```

```math
\vec{f_2}(\vec{u})=\begin{bmatrix}\frac{u_x^2}{2}\\0\end{bmatrix}
```

```math
\vec{f_3}(\vec{u})=\begin{bmatrix}0\\\frac{u_y^2}{2}\end{bmatrix}
```


