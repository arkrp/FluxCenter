# FluxCenter

Author: Hannah Nelson
Date: June 29th, 2023

This repository contains the function fluxCenter! fluxCenter Computes the center of mass of an irregular polygon using its vertecies!

## Usage

To make use of this algorithm create a list of 2d vectors contained in Vector2D.py . Call the function fluxCenter from fluxCenter.py with this list as a parameter! This function call will return the center of mass of the polygon specified by the vectors! The vectors are interpreted as positions of the verticies of the polygon!

## Principle of operation

fluxCenter uses the divergence theorem to perform the integrations needed to find the center of mass! By measuring the flux of a fields across a set of line segments enclosing a space, flux obtains the total divergence in that space! The fields are chosen such that the divergences are 1, x, and y respectively. Therefore the total flux are are:

$\sum\text{flux}\_{f\_1}=\int_{A}^{}1\cdot dA$

$\sum\text{flux}\_{f\_2}=\int_{A}^{}x\cdot dA$

$\sum\text{flux}\_{f\_3}=\int_{A}^{}y\cdot dA$

Using these we can easily obtain the center of mass!

$c\_{mx}=\frac{\int_{A}^{}x\cdot dA}{\int_{A}^{}1\cdot dA}$

$c\_{my}=\frac{\int_{A}^{}y\cdot dA}{\int_{A}^{}1\cdot dA}$
```math
c_{m}=\begin{bmatrix}c_{mx}\\c_{my}\end{bmatrix}
```
The respective formulas for flux across each line segment are:

$\text{flux}\_{f\_1}(P\_1,P\_2)=\frac{1}{2}\cdot(P\_{1x}+P\_{2x})\cdot(P\_{1y}-P\_{2y})$

$\text{flux}\_{f\_2}(P\_1,P\_2)=\frac{1}{6}\cdot(P\_{1x}^2+P\_{2x}^2+P\_{1x}P\_{2x})\cdot(P\_{1y}-P\_{2y})$

$\text{flux}\_{f\_3}(P\_1,P\_2)=\frac{1}{6}\cdot(P\_{1y}^2+P\_{2y}^2+P\_{1y}P\_{2y})\cdot(P\_{2x}-P\_{1x})$

These formulas were derived from a line integral!

```math
\text{flux}_{\vec{v}}(P_1,P_2)=\int_0^1\begin{bmatrix}P_{1y}-P_{2y}\\P_{2x}-P_{1x}\end{bmatrix}\cdot\vec{v}(\begin{bmatrix}P_{1x}-P_{1x}t+P_{2x}t\\P_{1y}-P_{1y}t+P_{2y}t\end{bmatrix})dt
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


