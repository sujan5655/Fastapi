## Pagination in Python

### Example Data

```python
data = ["Aarav", "Diya", "Rohan", "Ananya", "Kabir"]
```

| Index | Name   |
| ----- | ------ |
| 0     | Aarav  |
| 1     | Diya   |
| 2     | Rohan  |
| 3     | Ananya |
| 4     | Kabir  |

### Pagination Settings

```python
page = 2
limit = 2
```

- `page` = Current page number
- `limit` = Number of records displayed per page

### Step 1: Calculate Start

Formula:

```python
start = (page - 1) * limit
```

Calculation:

```python
start = (2 - 1) * 2
start = 1 * 2
start = 2
```

### Step 2: Calculate End

Formula:

```python
end = start + limit
```

Calculation:

```python
end = 2 + 2
end = 4
```

### Step 3: Get Paginated Data

Formula:

```python
paginated_data = data[start:end]
```

Calculation:

```python
paginated_data = data[2:4]
```

**Output:**

```python
["Rohan", "Ananya"]
```

### Complete Code

```python
data = ["Aarav", "Diya", "Rohan", "Ananya", "Kabir"]

page = 2
limit = 2

start = (page - 1) * limit
end = start + limit

paginated_data = data[start:end]

print(paginated_data)
```

**Output:**

```text
['Rohan', 'Ananya']
```

### Page-wise Data Distribution

| Page   | Start Index | End Index | Data          |
| ------ | ----------: | --------: | ------------- |
| Page 1 |           0 |         2 | Aarav, Diya   |
| Page 2 |           2 |         4 | Rohan, Ananya |
| Page 3 |           4 |         6 | Kabir         |

### Important Formulas

```python
start = (page - 1) * limit
end = start + limit

data[start:end]
```

**Remember:**

- `start` determines where pagination begins.
- `end` determines where pagination stops (exclusive).
- Python slicing `data[start:end]` does not include the end index.
