 🧭 Power BI | Microsoft Fabric | PySpark — Internal Learning Repository

This repository serves as a **central knowledge base** for our team’s learnings and experiments related to **Power BI**, **Microsoft Fabric automations**, and **PySpark**.
It captures our **hands-on implementations**, **reusable scripts**, and **frameworks** developed while building end-to-end data solutions.

---

## 🔍 Objective

To consolidate technical learnings, automation utilities, and best practices that streamline the development and deployment of Power BI and Fabric-based data solutions.
The repository supports:

* Consistent and scalable **report development**.
* Automated **dataset and pipeline management** using Fabric.
* Efficient **data transformation and validation** through PySpark.

---

## ⚙️ Key Focus Areas

### 1. **Power BI**

* DAX optimization and performance tuning.
* Semantic model structuring and relationship design.
* Report standardization via JSON theme templates.
* Implementation of Top-N visuals, field parameters, and calculation groups.
* Dynamic filtering, context handling, and automation-ready models.

### 2. **Fabric Automations**

* API-based automation for dataset refreshes, report deployment, and validation.
* Orchestration of model refresh pipelines and event-triggered processes.
* Integration with Power Automate, DevOps, and Teams for workflow monitoring.
* Scripts to track refresh status, pipeline failures, and data drift across environments.

### 3. **PySpark**

* Data ingestion, transformation, and aggregation using Spark DataFrames.
* Interfacing with Fabric Lakehouse and Delta tables.
* Validation and pre-processing pipelines prior to Power BI consumption.
* Performance optimization techniques and job orchestration patterns.

---

## 🧱 Repository Structure

```
├── powerbi/
│   ├── dax_measures/         # Optimized and reusable DAX scripts
│   ├── reports/              # Power BI report templates and configs
│   ├── themes/               # Custom JSON themes
│   └── docs/                 # Power BI documentation and guides
│
├── fabric_automations/
│   ├── pipelines/            # Fabric pipeline definitions
│   ├── scripts/              # API-based automation and validation scripts
│   └── notebooks/            # Fabric notebooks used for automation
│
├── pyspark/
│   ├── notebooks/            # Learning notebooks and transformations
│   ├── datasets/             # Sample datasets for practice
│   └── examples/             # Scenario-based PySpark scripts
│
└── README.md
```

---

## 🧩 Core Learnings Captured

* Power BI semantic model alignment with Fabric workspaces.
* Automated refresh pipeline monitoring and alerting.
* End-to-end model migration and validation between environments.
* Integration of PySpark data processing with Fabric Lakehouse.
* Techniques to maintain DAX consistency across multiple reports.

---

## 📈 Ongoing Initiatives

* Extending automation to include report publishing and parameterized refresh.
* Building a Fabric Notebook framework for Spark-based validation and logging.
* Developing Power BI–Fabric–PySpark integrated learning workflows.
* Continuous performance benchmarking for DAX and Spark workloads.

---

## 🧑‍💻 Usage Guidelines

* All code, measures, and notebooks are **for internal use and learning purposes**.
* Follow naming conventions and directory structure when adding new content.
* Use dedicated branches for experimental work before merging to main.
* Maintain version control for JSON themes, DAX libraries, and pipeline scripts.

---

## 🧠 Contributor Notes

* Contributions should include a brief README or markdown note explaining:

  * Purpose of the script or notebook.
  * Inputs, outputs, and dependencies.
  * Known issues or limitations.
* Peer review is recommended before merging to the main branch.

---

## 📋 License

This repository is restricted to internal educational and reference purposes.
Do not distribute or publish externally without prior approval.

