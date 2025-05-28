# 🧠 NSL-KDD QML: Quantum Machine Learning with NSL-KDD

A full preprocessing + Quantum ML pipeline for the [NSL-KDD dataset](https://www.unb.ca/cic/datasets/nsl.html) tailored for use with Quantum Support Vector Machines (QSVM), Quantum Convolutional Neural Networks (QCNN), and Variational Hybrid models. Built to run on both simulators and local environments with 16–32 GB RAM.

---

## 📁 Project Structure

```bash
nsl-kdd-qml/
├── data/                      # Raw NSL-KDD files (.txt)
├── output/                    # Preprocessed CSVs
├── utils/                     # Python preprocessing utilities
│   └── preprocess.py
├── notebooks/                 # Jupyter Notebooks for demo and debugging
│   └── NSL_KDD_Preprocessing_QML.ipynb
├── qsvm_pipeline.py           # Optional: CLI-based execution
├── requirements.txt
└── README.md
```

---

✅ Key Features
	•	Prepares train + test CSVs from raw .txt files
	•	One-hot encodes protocol_type, service, flag
	•	Converts labels to binary (normal = 0, attack = 1)
	•	Scales all numerical values to [0, 1]
	•	Easily integrates with Qiskit & PennyLane backends
	•	Minimal memory overhead, but works great on 24 GB+ systems

---

🚀 How to Run Locally

1. Clone this repo

git clone https://github.com/omumrania/nsl-kdd-qml.git
cd nsl-kdd-qml

2. Setup virtual environment

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

3. Preprocess the Dataset

Launch the notebook:

jupyter notebook notebooks/NSL_KDD_Preprocessing_QML.ipynb

Or run a Python script (CLI-friendly):

python qsvm_pipeline.py --train --test


---

🧪 Sample Output Files
	•	nsl_kdd_preprocessed_train.csv
	•	nsl_kdd_preprocessed_test.csv

These are ready to be used with:
	•	qiskit_machine_learning.kernels.QuantumKernel
	•	SVC(kernel=custom_kernel)

---

👨‍🔬 Author

Om Umrania
PhD Researcher – Quantum Intrusion Detection
📧 [omumrania2020@gmail.com](mailto:omumrania2020@gmail.com)

---

📝 License

This project is licensed under the MIT License.
