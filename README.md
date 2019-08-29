# Example of packages with different requirements

```bash
pip install deepseismic[imaging, interpretation]
```
Installs everything so the following should complete without error
```python
from deepseismic import interpretation
from deepseismic import imaging
```

```bash
pip install deepseismic[interpretation]
```
Installs only common requirements and requirements for interpretation
```python
from deepseismic import interpretation
```
So the above should work fine but
```python
from deepseismic import imaging
```
Will throw an error with regards to progressbar dependency
