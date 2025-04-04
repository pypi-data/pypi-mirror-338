# WebEngage CSV Splitter

## Overview

WebEngage CSV Splitter is an internal tool designed to **split large CSV files** into smaller parts. It ensures that a master spreadsheet containing extensive data is divided into multiple files while maintaining data integrity.

## How It Works

- Splits **CSV files into multiple smaller files** in real-time.
- Allows users to define the **number of splits** for the master file.
- The process takes approximately **5-10 minutes** depending on the file size.
- The split files are saved in the **splits folder**, with filenames appended by an **iteration number**.

## Installation

To install the package, run:

```sh
pip install webengage-csv-split
```

## Usage

Run the following command to split a CSV file:

```sh
we --split <filename.csv> <no. of iteration>
```

Replace `<filename.csv>` with the actual file name and `<num_splits>` with the number of parts you want to split the file into.

## Legal Notice

This tool is an **internal property** of **WebEngage** and is strictly for **auditing purposes**. It is owned by **Nipun Patel (Copyright)** and any misuse, unauthorized distribution, or external sharing will lead to **legal consequences**.

---

© WebEngage. All rights reserved.
