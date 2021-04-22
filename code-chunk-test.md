

# A collapsible section with markdown
<details>
  <summary>Click to expand!</summary>

```bash {cmd=true hide=TURE}
ls .
```
</details>

```javascript {cmd="node" hide=TRUE}
const date = Date.now()
console.log(date.toString())
```

```bash {cmd hide}
ls .
```

```gnuplot {cmd=true output="html"}
set terminal svg
set title "Simple Plots" font ",20"
set key left box
set samples 50
set style data points

plot [-10:10] sin(x),atan(x),cos(atan(x))
```