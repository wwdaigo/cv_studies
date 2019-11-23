## Modeling projection

Pin-hole model approximation

![](assets/projection_model.svg)

**CoP**: Center of projection  
**PP**: Projection plan

Put the optical center (CoP) at the origin, which is also the origin of the camera coordinate system.
* The camera looks down the negative Z coordinates.
* The distance between the CoP and PP is **positive**.

## Projection equations

Compare the intersection with perspective projectiom of ray from (x,y,z) to COP.

Derived from using similar triangles.

![](assets/projection_model_triangles.svg)

![equation](https://latex.codecogs.com/gif.latex?(x,y,z)\rightarrow(-d\frac{x}{z},-d\frac{y}{z},-d))

To retrieve the image location, throw out the last coordinate:

![equation](https://latex.codecogs.com/gif.latex?(x',y')\rightarrow(-d\frac{x}{z},-d\frac{y}{z}))

Distant objects are smaller  
Zero is the center of the image 

## Homogeneous coordinates

Trick: add one more coordinate to the vector:

![equation](https://latex.codecogs.com/gif.latex?(x,y)\Rightarrow\quad\begin{bmatrix}x\\y\\1\end{bmatrix})

![equation](https://latex.codecogs.com/gif.latex?(x,y,z)\Rightarrow\quad\begin{bmatrix}x\\y\\z\\1\end{bmatrix})

### Convert from homogeneous coordinates

![equation](https://latex.codecogs.com/gif.latex?2D\quad\begin{bmatrix}x\\y\\w\end{bmatrix}\Rightarrow(x/w,y/w))

![equation](https://latex.codecogs.com/gif.latex?3D\quad\begin{bmatrix}x\\y\\z\\w\end{bmatrix}\Rightarrow(x/w,y/w,z/w))

## Perspective projection

Projection is a matrix multiply using homogeneous coordinates:

![equation](https://latex.codecogs.com/gif.latex?\quad\begin{bmatrix}1&0 &0&0\\0&1&0&0\\0&0&1/f&0\end{bmatrix}\quad\begin{bmatrix}x\\y\\z\\1\end{bmatrix}=\quad\begin{bmatrix}x\\y\\z/f\end{bmatrix}\Rightarrow(f\frac{x}{z},\frac{y}{z})\Rightarrow(u,v))

**f** is the focal length, the distance from the center of projection to the image.

### Scaling the projection matrix

![equation](https://latex.codecogs.com/gif.latex?\quad\begin{bmatrix}f&0 &0&0\\0&f&0&0\\0&0&1&0\end{bmatrix}\quad\begin{bmatrix}x\\y\\z\\1\end{bmatrix}=\quad\begin{bmatrix}fx\\fy\\z\end{bmatrix}\Rightarrow(f\frac{x}{z},\frac{y}{z}))

## Geometric properties of projections

* Points go to points
* Lines go to lines
* Polygons go to poygons

[img ex 3a-L2 lec 8]

## Parallel lines

Parallel lines in the world meet in the image.

Line in 3 space

![equation](https://latex.codecogs.com/gif.latex?x(t)=x_{0}+at)  
![equation](https://latex.codecogs.com/gif.latex?y(t)=y_{0}+bt)  
![equation](https://latex.codecogs.com/gif.latex?z(t)=z_{0}+ct)

Perspective projection of the line

![equation](https://latex.codecogs.com/gif.latex?x'(t)=f\frac{x}{z}=\frac{f(x_0+at)}{z_o+ct})

![equation](https://latex.codecogs.com/gif.latex?y'(t)=f\frac{y}{z}=\frac{f(y_0+bt)}{z_o+ct})

In the limit as ![equation](https://latex.codecogs.com/gif.latex?t\rightarrow\pm\infty), for ![equation](https://latex.codecogs.com/gif.latex?c\neq0)


![equation](https://latex.codecogs.com/gif.latex?x'(t)\rightarrow\frac{fa}{c},y'(t)\rightarrow\frac{fb}{c})

Parallel lines in the world will converge to a single point.

## Vanish points

Sets of parallel lines on the plane lead to colinear vanish points. This line is called the "horizon" for the plane.
(Show samples)

## Other types of projections

Orthographic projection

x,y,z => (x,y)

Weak perspective

(x,y,z) => (fx/z0, fy/z0)