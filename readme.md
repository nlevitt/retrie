1. monkey

```
*monkey
```
```
'monkey'
```

2. money

```
    mon
   /   \
*key   *ey
```
```
'mon(key|ey)'
```

3. monk

```
     mon
    /   \
  *k    *ey
  /
*ey
```
```
'mon(k(ey)?|ey)'
```

4. monks

```
      mon
     /   \
   *k    *ey
  /  \
*ey  *s
```

```
'mon(k(ey|s)?|ey)'
```

5. monkeynut

```
         mon
        /   \
      *k    *ey
     /  \
   *ey  *s
   /
*nut
```

```
'mon(k(ey(nut)?|s)?|ey)'
```

6. monkeyface

```
         mon
        /   \
      *k    *ey
     /  \
   *ey  *s
   / \
*nut *face
```

```
'mon(k(ey(nut|face)?|s)?|ey)'
```

7. monkery

```
           mon
          /   \
        *k    *ey
       /  \
      e   *s
     / \
   *y  *ry
   / \
*nut *face
```

```
'mon(k(e(y(nut|face)?|ry)|s)?|ey)'
```

8. ape

```
           mon    *ape
          /   \
        *k    *ey
       /  \
      e   *s
     / \
   *y  *ry
   / \
*nut *face
```

```
'mon(k(e(y(nut|face)?|ry)|s)?|ey)|ape'
```
