# Enverge Placeholder

For development run:
```bash
cd /path/to/enverge_placeholder
pip uninstall enverge_placeholder -y
jlpm install
jlpm install:extension
pip install -e .
jupyter labextension develop . --overwrite
jlpm run watch
```