# pydiff

Dependency-free helpers for comparing Python values and producing compact structured diffs.

## Features

- Recursive dictionary comparison
- Added, removed, and changed keys
- Stable list comparison
- JSON-friendly results

## Usage

```python
from pydiff import diff_dicts

result = diff_dicts({"name": "medu", "age": 20}, {"name": "medu", "age": 21})
print(result["changed"])
```

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

## Credits

https://guns.lol/meduu
