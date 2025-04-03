# samcell-napari

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/samcell-napari)](https://pypi.org/project/samcell-napari/)

A napari plugin for cell segmentation using the Segment Anything Model (SAM) foundation model.

![SAMCell Segmentation Example](https://github.com/saahilsanganeriya/samcell-napari/raw/main/docs/images/example.png)

## Description

SAMCell-napari provides an intuitive interface for segmenting cells in microscopy images using deep learning. It leverages the power of the Segment Anything Model (SAM) adapted specifically for biological cell segmentation, providing accurate results with minimal tuning.

### Key Features:
- Simple, user-friendly interface within napari
- Compatible with SAMCell models
- Adjustable segmentation parameters for fine-tuning
- Real-time visualization of results
- Distance map visualization for analyzing cell proximity
- Full integration with napari's layer system

## Installation

You can install `samcell-napari` via [pip]:

```bash
pip install samcell-napari
```

To install latest development version:

```bash
pip install git+https://github.com/saahilsanganeriya/samcell-napari.git
```

## Usage

1. Start napari
   ```bash
   napari
   ```

2. Load your image in napari

3. Open the SAMCell plugin:
   ```
   Plugins > samcell-napari > SAMCell Segmentation
   ```

4. Provide the path to your SAMCell model file (pytorch_model.bin)
   - You can download pre-trained models from the [official SAMCell release page](https://github.com/NathanMalta/SAMCell/releases/tag/v1)

5. Adjust parameters if needed:
   - Cell peak threshold: Higher values detect fewer cells (default: 0.5)
   - Cell fill threshold: Lower values create larger cells (default: 0.05)
   - Crop size: Size of image crops for processing (default: 256)

6. Click "Run Segmentation"

7. View the segmentation results in napari as a Labels layer

## Requirements

- Python 3.8 or higher
- napari 0.4.14 or higher
- PyTorch 1.9 or higher
- CUDA-capable GPU recommended for faster processing

## Model Compatibility

The plugin is compatible with SAMCell model files (pytorch_model.bin). Pre-trained models can be downloaded from the [official SAMCell release page](https://github.com/NathanMalta/SAMCell/releases/tag/v1).

Recommended models include:
- SAMCell1.0-Cellpose-cyto: Trained on the Cellpose cytoplasm dataset
- SAMCell1.0-livecell: Trained on the LiveCELL dataset

These models are part of the release assets for the paper "SAMCell: Generalized Label-Free Biological Cell Segmentation with Segment Anything".

## How It Works

SAMCell operates using a sliding window approach to process large images:

1. The image is divided into overlapping crops
2. Each crop is processed through a SAM-based model
3. A distance map is created, representing cell centers and boundaries
4. The distance map is processed to extract individual cell masks
5. Results are stitched back together and shown in napari

## Contributing

Contributions are very welcome! Please feel free to submit a Pull Request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Citation

If you use this plugin in your research, please cite:

```
@article{samcell2023,
  title={SAMCell: Generalized Label-Free Biological Cell Segmentation with Segment Anything},
  author={...},
  journal={...},
  year={2023}
}
``` 