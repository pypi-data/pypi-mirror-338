# PanMetrics: A Comprehensive Metric Library for Machine Learning Tasks

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

PanMetrics is a comprehensive Python library that provides a wide range of evaluation metrics for various machine learning tasks including regression, classification, clustering, segmentation, and image-to-image translation.

## Features

- **Unified interface** for metrics across different ML tasks
- **Comprehensive collection** of evaluation metrics
- **Easy integration** with existing ML workflows
- **Consistent API** across all metric types

## Installation

You can install PanMetrics using pip:

```bash
pip install panmetrics
```

## Usage

### Regression Metrics

```python
from panmetrics.regression import mean_absolute_error, r_squared

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

print(metrics.mean_absolute_error(y_true, y_pred))
print(metrics.r_squared(y_true, y_pred))
```

Available regression metrics:
- Mean Absolute Error (`mean_absolute_error`)
- Mean Squared Error (`mean_squared_error`)
- Mean Absolute Percentage Error (`mean_absolute_percentage_error`)
- Mean Squared Log Error (`mean_squared_log_error`)
- Mean Bias Deviation (`mean_bias_deviation`)
- Median Absolute Error (`median_absolute_error`)
- Symmetric Mean Absolute Percentage Error (`symmetric_mean_absolute_percentage_error`)
- Relative Squared Error (`relative_squared_error`)
- R-squared (`r_squared`)
- Explained Variance (`explained_variance`)
- Huber Loss (`huber_loss`)
- Log Cosh Loss (`log_cosh_loss`)
- Max Error (`max_error`)
- Mean Tweedie Deviance (`mean_tweedie_deviance`)
- Mean Pinball Loss (`mean_pinball_loss`)

### Classification Metrics

```python
from panmetrics.classification import accuracy_score, f1_score

y_true = [0, 1, 0, 1]
y_pred = [0, 1, 1, 0]

print(metrics.accuracy_score(y_true, y_pred))
print(metrics.f1_score(y_true, y_pred))
```

Available classification metrics:
- Accuracy (`accuracy_score`)
- Precision (`precision_score`)
- Recall (`recall_score`)
- F1 Score (`f1_score`)
- Balanced Accuracy (`balanced_accuracy`)
- Matthews Correlation Coefficient (`matthews_correlation_coefficient`)
- Cohen's Kappa (`cohens_kappa`)
- FBeta Score (`fbeta_score`)
- Jaccard Score (`jaccard_score`)

### Clustering Metrics

```python
from panmetrics.clustering import adjusted_rand_score, silhouette_score

labels_true = [0, 0, 1, 1]
labels_pred = [1, 1, 0, 0]

print(metrics.adjusted_rand_score(labels_true, labels_pred))
print(metrics.silhouette_score(labels_true, labels_pred))
```

Available clustering metrics:
- Rand Score (`rand_score`)
- Adjusted Rand Score (`adjusted_rand_score`)
- Mutual Information Score (`mutual_info_score`)
- Normalized Mutual Information Score (`normalized_mutual_info_score`)
- Silhouette Score (`silhouette_score`)
- Calinski-Harabasz Score (`calinski_harabasz_score`)
- Davies-Bouldin Score (`davies_bouldin_score`)
- Homogeneity Score (`homogeneity_score`)
- Completeness Score (`completeness_score`)
- V-Measure Score (`v_measure_score`)
- Fowlkes-Mallows Score (`fowlkes_mallows_score`)

### Segmentation Metrics

```python
from panmetrics.segmentation import dice_score, iou_score

y_true = [[0, 1, 1], [1, 0, 0]]
y_pred = [[0, 1, 0], [1, 0, 1]]

print(metrics.dice_score(y_true, y_pred))
print(metrics.iou_score(y_true, y_pred))
```

Available segmentation metrics:
- Dice Score (`dice_score`)
- IoU Score (`iou_score`)
- Sensitivity (`sensitivity`)
- Specificity (`specificity`)
- Precision (`precision`)
- Hausdorff Distance (`hausdorff_distance`)

### Image-to-Image Translation Metrics

```python
from panmetrics.imagetoimage import psnr, ssim

img1 = ...  # numpy array of image 1
img2 = ...  # numpy array of image 2

print(metrics.psnr(img1, img2))
print(metrics.ssim(img1, img2))
```

Available image-to-image metrics:
- PSNR (`psnr`)
- SSIM (`ssim`)

## Contributing

We welcome contributions to PanMetrics! Please see our [Contribution Guidelines](CONTRIBUTING.md) for more information.

## License

PanMetrics is released under the MIT License. See [LICENSE](LICENSE) for details.

## Citation

<!-- If you use PanMetrics in your research, please consider citing it:

```bibtex
@software{PanMetrics,
  author = {Your Name},
  title = {panmetrics: A Unified Python Library for Standardized Metric Evaluation and Robust Data Validation in Machine Learning},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/yourusername/panmetrics}}
}
``` -->

## Support

For questions, issues, or feature requests, please open an issue on our [GitHub repository].