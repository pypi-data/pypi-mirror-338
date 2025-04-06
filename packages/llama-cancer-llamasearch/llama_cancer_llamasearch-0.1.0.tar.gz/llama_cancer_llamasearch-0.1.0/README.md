# LlamaCancer

![LlamaCancer Logo](docs/images/llamacancer_logo.png)

[![PyPI version](https://img.shields.io/pypi/v/llamacancer.svg)](https://pypi.org/project/llamacancer/)
[![Python Versions](https://img.shields.io/pypi/pyversions/llamacancer.svg)](https://pypi.org/project/llamacancer/)
[![License](https://img.shields.io/github/license/llamagroup/llamacancer.svg)](https://github.com/llamagroup/llamacancer/blob/main/LICENSE)

LlamaCancer is a comprehensive Python framework for analyzing biomarker associations in oncology clinical trials. It provides a streamlined workflow for biomarker analysis, including data loading, processing, statistical analysis, and visualization.

## Features

- **Flexible data loading**: Support for various data formats and structures
- **Automated biomarker dichotomization**: Convert continuous biomarkers to categorical (high/low) groups using multiple methods
- **Comprehensive statistical analysis**: Log-rank tests, Cox proportional hazards models, Fisher's exact tests, and more
- **Publication-quality visualizations**: Kaplan-Meier plots, forest plots, volcano plots, and more
- **Configuration-based workflow**: Define analysis parameters in reusable configuration files
- **Extensive documentation**: Comprehensive user guide, API reference, and tutorials

## Installation

```bash
# Install from PyPI
pip install llamacancer

# Install from source
git clone https://github.com/llamagroup/llamacancer.git
cd llamacancer
pip install -e .
```

## Quick Start

```python
import llamacancer as lc
from llamacancer.config import load_config
from llamacancer.io import load_clinical_data, load_biomarker_data, merge_clinical_biomarkers
from llamacancer.analysis import run_biomarker_associations

# Load configuration
config = load_config("configs/default_analysis_config.py")

# Load and merge data
clinical_df = load_clinical_data(config)
biomarker_df = load_biomarker_data(config)
merged_df = merge_clinical_biomarkers(clinical_df, biomarker_df)

# Run biomarker association analysis
results = run_biomarker_associations(merged_df, config)

# Display significant biomarkers
print(f"Significant biomarkers: {results['summary']['significant_biomarkers']}")
```

## Example Workflow

1. **Define your configuration**:
   ```python
   # configs/my_analysis_config.py
   from ml_collections import config_dict

   def get_config():
       config = config_dict.ConfigDict()
       config.project_name = "My Biomarker Analysis"
       config.data_dir = "data/"
       config.biomarkers_to_analyze = ["B_cell_GES", "CD19_Expression_Level"]
       # ... more configuration options
       return config
   ```

2. **Prepare your data**:
   - Clinical data CSV with patient identifiers, treatment arms, endpoints
   - Biomarker data CSV with patient identifiers and biomarker measurements

3. **Run the analysis from command line**:
   ```bash
   llamacancer --config configs/my_analysis_config.py
   ```

4. **Or run interactively in a notebook**:
   ```
   jupyter notebook notebooks/1_biomarker_association_workflow.ipynb
   ```

## Documentation

For detailed documentation, visit our [Documentation Site](https://llamasearch.ai or check the `docs/` directory.

- [User Guide](docs/README.md): Instructions for installation, configuration, and usage
- [API Reference](docs/api/): Detailed documentation of modules, classes, and functions
- [Examples](notebooks/): Jupyter notebooks demonstrating LlamaCancer workflows
- [Tutorials](docs/tutorials/): Step-by-step tutorials for common tasks

## Example Results

![Kaplan-Meier Plot](docs/images/kaplan_meier_example.png)

*Kaplan-Meier plot showing event-free survival stratified by B-cell gene expression signature.*

![Forest Plot](docs/images/forest_plot_example.png)

*Forest plot showing hazard ratios for multiple biomarkers.*

## Citation

If you use LlamaCancer in your research, please cite:

```
LlamaGroup. (2023). LlamaCancer: A framework for biomarker association analysis in oncology clinical trials.
GitHub repository: https://github.com/llamagroup/llamacancer
```

## License

LlamaCancer is released under the MIT License. See the [LICENSE](LICENSE) file for details. 