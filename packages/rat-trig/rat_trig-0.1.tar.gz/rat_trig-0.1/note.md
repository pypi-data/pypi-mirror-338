```bash
pip install --upgrade pyscaffold[all]
putup --markdown --no-tox rat-trig -d "Rational Trigonometry"
cd rat-trig
rg "Rational Trigonometry"

pip install -e .
pytest
pytest --cov-report html
cd docs
pip install -r .\requirements.txt
make html
```
