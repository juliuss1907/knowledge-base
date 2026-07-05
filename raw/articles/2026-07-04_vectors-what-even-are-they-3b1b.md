---
type: raw
source_type: article
source_url: https://www.3blue1brown.com/lessons/vectors
source_name: 3Blue1Brown
author: Grant Sanderson (3Blue1Brown)
title: "Vectors, what even are they? — Linear Algebra Chapter 1"
date_ingested: 2026-07-04
date_published: 2016-08-06
tags: [ai, research]
status: processed
compiled_at: 2026-07-05
compiled_to: "[[src_vectors-what-even-are-they-3b1b]]"
---

# Vectors, what even are they? — Linear Algebra Chapter 1

**Author:** Grant Sanderson (3Blue1Brown)
**Source:** 3Blue1Brown
**Published:** 2016-08-06

---

> "The introduction of numbers as coordinates is an act of violence." — Hermann Weyl

## Three Interpretations of Vectors

### Physics Perspective
Vectors are arrows pointing in space. Defined by length and direction — can be moved around and still be the same vector. 2D in a plane, 3D in space.

### CS Perspective
Vectors are ordered lists of numbers. E.g., model houses as `[square_footage, price]`. Order matters. A two-dimensional vector simply means the list has length 2.

### Mathematician's Perspective
A vector can be anything where there's a sensible notion of adding two vectors and multiplying a vector by a number. Abstract but important — hints that addition and scalar multiplication play a central role throughout linear algebra.

## Coordinate Systems

- x-axis (horizontal) and y-axis (vertical), intersection = origin = center of space and root of all vectors
- Coordinates give instructions to get from tail (origin) to tip: first number = walk along x-axis (right=+, left=-), second = walk parallel to y-axis (up=+, down=-)
- Every pair of numbers ↔ exactly one vector (bijection)
- 3D adds z-axis perpendicular to x and y; every triplet ↔ exactly one vector

## Vector Operations

### Addition
Move second vector's tail to first vector's tip. Sum = new vector from first tail to second tip.

Reasoning: each vector represents a movement — step along first, then step along second = same effect as one step along the sum. Extension of number line addition: 2+5 = move 2 right, then 5 right = same as 7 right.

Numerically: match terms, add each together:
`[x₁, y₁] + [x₂, y₂] = [x₁+x₂, y₁+y₂]`

### Scalar Multiplication
- Multiply by 2 → stretch 2x
- Multiply by ⅓ → squish to ⅓ length
- Multiply by -1.5 → flip direction + stretch 1.5x

Called "scaling", numbers acting this way are "scalars." Numerically: multiply each coordinate by the scalar:
`2 * [x, y] = [2x, 2y]`

## Conclusion

The power of linear algebra comes not from either view (arrows vs lists), but from the ability to translate between them:
- Data analysts: visualize lists of numbers geometrically
- Physicists/CG programmers: describe and manipulate space using crunchable numbers

Every linear algebra topic revolves around vector addition and scalar multiplication.
