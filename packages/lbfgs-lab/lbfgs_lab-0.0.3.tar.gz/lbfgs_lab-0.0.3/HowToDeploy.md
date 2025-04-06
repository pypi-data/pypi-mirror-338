# How to Deploy

```bash
python3 -m build --sdist
tar -tf dist/lbfgs_lab-0.0.2.tar.gz # check the content
python3 -m twine upload --repository pypi dist/*
```
