# 🏊‍♂️ Problem: The Raft

## 📄 Problem Statement

In the middle of a lake floats a rectangular raft.
The sides of the raft are parallel to the coordinate axes:

* The **OX** axis points east,
* The **OY** axis points north.

The southwest corner of the raft has coordinates **(x₁, y₁)**,
and the northeast corner has coordinates **(x₂, y₂)**.

A swimmer is located at the point **(x, y)**.
You need to determine **in which direction** the swimmer should swim to reach the raft as quickly as possible.

---

## 💡 Input Format

The program receives **six integers**:

```
x1
y1
x2
y2
x
y
```

### Conditions:

* `x1 < x2`
* `y1 < y2`
* `x ≠ x1`, `x ≠ x2`, `y ≠ y1`, `y ≠ y2`
* The swimmer’s coordinates are **outside the raft**
* All values have an absolute value ≤ 100

---

## 📤 Output Format

The program must print **a single line** — the direction in which the swimmer should swim:

| Situation                        | Output |
| -------------------------------- | ------ |
| Swim toward the northern side    | `N`    |
| Swim toward the southern side    | `S`    |
| Swim toward the western side     | `W`    |
| Swim toward the eastern side     | `E`    |
| Swim toward the northwest corner | `NW`   |
| Swim toward the northeast corner | `NE`   |
| Swim toward the southwest corner | `SW`   |
| Swim toward the southeast corner | `SE`   |

---

## 🧠 Solution Logic

1. Determine whether the swimmer is **opposite one of the sides** of the raft or **outside both axes**:

   * If `x` is between `x1` and `x2` but `y` is outside — swim `N` or `S`.
   * If `y` is between `y1` and `y2` but `x` is outside — swim `W` or `E`.
   * If the swimmer is outside both ranges — swim toward one of the four corners (`NW`, `NE`, `SW`, `SE`).

2. Output **exactly one direction** (otherwise a *presentation error* will occur).

---

## 🧩 Example Input

```
0
0
4
3
5
5
```

## ✅ Example Output

```
NE
```

## 🕐 Constraints

* **Time:** ≤ 1 second
* **Memory:** ≤ 256 MB

