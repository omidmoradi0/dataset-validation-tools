# Dataset Validation Tools

A lightweight Python tool for checking the health and consistency of image datasets and their XML annotations.

The project validates dataset folder structure, image files, image/XML pairs, image dimensions, and Pascal VOC-style XML annotations.

## Features

### Image Validation

- Checks supported image files (`.jpg`, `.jpeg`, `.png`)
- Detects unreadable or corrupted images
- Checks image dimensions against an expected size
- Reports images with unsupported dimensions
- Detects images without corresponding XML annotation files

### XML Validation

- Detects empty XML files
- Detects XML files without corresponding images
- Validates XML syntax
- Validates Pascal VOC annotation structure
- Checks required fields such as:
  - `filename`
  - `size`
  - `width`
  - `height`
  - `depth`
  - `object`
  - `name`
  - `bndbox`
- Validates bounding box coordinates
- Detects bounding boxes outside image dimensions

### Report Generation

Validation results can be saved to a text file for later review.

Example:

```text
Image validation started
We have 2 images that have unsupported sizes
Unsupported image: test_dataset/train/1.jpg
Unsupported image: test_dataset/train/2.jpg

We have 1 image without an XML file
Image without XML: 3
```

## Project Structure

```text
dataset-validation-tools/
│
├── main.py
├── README.md
├── .gitignore
│
├── src/
│   ├── health_checker.py
│   ├── image_validator.py
│   └── xml_validator.py
│
└── test_dataset/
    ├── train/
    ├── validation/
    └── test/
```

## Dataset Structure

The tool expects the dataset to be divided into three folders:

```text
test_dataset/
├── train/
│   ├── image1.jpg
│   ├── image1.xml
│   ├── image2.jpg
│   └── image2.xml
│
├── validation/
│   ├── image1.jpg
│   └── image1.xml
│
└── test/
    ├── image1.jpg
    └── image1.xml
```

Each image should have a corresponding XML annotation with the same filename.

Example:

```text
1.jpg
1.xml
```

## XML Format

The project is designed to validate Pascal VOC-style XML annotations.

Example:

```xml
<annotation>
    <filename>1.jpg</filename>

    <size>
        <width>384</width>
        <height>79</height>
        <depth>3</depth>
    </size>

    <object>
        <name>3</name>

        <bndbox>
            <xmin>45</xmin>
            <ymin>9</ymin>
            <xmax>83</xmax>
            <ymax>67</ymax>
        </bndbox>
    </object>
</annotation>
```

## Installation

Clone the repository:

```bash
git clone https://github.com/omidmoradi0/dataset-validation-tools.git
cd dataset-validation-tools
```

Create a virtual environment:

```bash
python -m venv env
```

Activate it on Windows:

```bash
env\Scripts\activate
```

Install the required packages:

```bash
pip install opencv-python
```

## Usage

Configure the dataset path and expected image size in `main.py`:

```python
input_folder = "test_dataset"
output_file = "output.txt"
image_size = (224, 224)
```

Then run:

```bash
python main.py
```

The program checks the `train`, `validation`, and `test` folders and reports dataset validation problems.

## Main Components

`HealthChecker` coordinates validation across the dataset folders.

`ImageValidator` handles image-related checks such as dimensions, corrupted images, and missing XML annotations.

`XmlValidator` validates XML files, annotation structure, and bounding box coordinates.

## Technologies

- Python
- OpenCV
- XML ElementTree
- Git / GitHub

## Purpose

This project was created as a practical exercise in Python software development, including:

- Object-Oriented Programming
- File handling
- Exception handling
- Dataset validation
- XML parsing
- Modular project structure
- Git branching and version control