# ci-practica

Proyecto pequeño para ver la integración continua en GitHub Actions. Cada push ejecuta las pruebas en un computador limpio (`.github/workflows/ci.yml`).

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -v
ruff check .
```

En la pestaña **Actions**, abre la última ejecución y busca en el paso «Ejecutar pruebas» cuántas pruebas corrieron.
