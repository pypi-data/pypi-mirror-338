# probly: Uncertainty Representation and Quantification for Machine Learning
<div align="center">

[![PyPI version](https://badge.fury.io/py/probly.svg)](https://badge.fury.io/py/probly)
[![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![PePy](https://static.pepy.tech/badge/probly?style=flat-square)](https://pepy.tech/project/probly)
[![PyPI status](https://img.shields.io/pypi/status/probly.svg?color=blue)](https://pypi.org/project/probly)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)
![Last Commit](https://img.shields.io/github/last-commit/pwhofman/probly)
</div>

## 🛠️ Install
`probly` is intended to work with **Python 3.10 and above**. Installation can be done via `pip`:

```sh
pip install probly
```

## ⭐ Quickstart

`probly` makes it very easy to make models uncertainty-aware and perform several downstream tasks:

```python
import probly
import torch.nn.functional as F

net = ... # get neural network
model = probly.representation.Dropout(net) # make neural network a Dropout model
train(model) # train model as usual

data = ... # get data
preds = model.predict_representation(data) # predict an uncertainty representation
eu = probly.quantification.classification.mutual_information(preds) # compute model's epistemic uncertainty

data_ood = ... # get out of distribution data
preds_ood = model.predict_representation(data_ood)
eu_ood = probly.quantification.classification.mutual_information(preds_ood)
auroc = probly.tasks.out_of_distribution_detection(eu, eu_ood) # compute the AUROC score for out of distribution detection
```

## 📜 License
This project is licensed under the [MIT License](https://github.com/pwhofman/probly/blob/main/LICENSE).

---
Built with ❤️ by the probly team.
