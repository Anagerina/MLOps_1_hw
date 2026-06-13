## Пайплайн полностью настроен и работает
---
#### Вывод при успешной валидации (accuracy_min: 0.6):

```bash
Accuracy 0.837 > Accuracy_min 0.6
```
#### Вывод при проваленной валидации (accuracy_min: 0.99):

```bash
Accuracy 0.837 <= Accuracy_min 0.99

ERROR: failed to reproduce 'validate_model': failed to run: python src/validate_model.py, exited with 1
```"
