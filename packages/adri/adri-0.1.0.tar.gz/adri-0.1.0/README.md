<![CDATA[
# Agent Data Readiness Index (ADRI)

ADRI is the industry’s first open standard for evaluating data quality for agentic AI systems. It provides a comprehensive, five-dimensional assessment of data sources by measuring Validity, Completeness, Freshness, Consistency, and Plausibility.

## Installation

Install ADRI from PyPI:

```bash
pip install adri
```

> Note: If "adri" is already taken on PyPI, consider using an alternative package name (e.g., `agent-data-readiness-index`).

## Quick Start

Run an assessment on your data source with:

```bash
adri assess --source your_data.csv --output report
```

Then, view the generated report with:

```bash
adri report view report.json
```

## Features

- **Five-Dimensional Assessment:** Evaluates data sources across Validity, Completeness, Freshness, Consistency, and Plausibility.
- **Agent-Centric Evaluation:** Clearly communicates data quality attributes to AI agents.
- **Benchmarking:** Compare your scores against industry assessments.
- **Rich Reporting:** Generates outputs in both JSON and HTML formats.
- **Extensibility:** Designed to integrate with multiple data sources and environments.

## Documentation

For detailed information, please refer to our [GitHub Wiki](https://github.com/verodat/agent-data-readiness-index/wiki) and additional documentation in the repository.

## Contributing

We welcome contributions! To contribute:
1. Fork the repository on GitHub.
2. Run your assessments using ADRI.
3. Submit your HTML report to the `docs/reports/` directory.
4. Update the repository index and create a pull request.

For more details, see the [Contributing Guide](https://github.com/verodat/agent-data-readiness-index#contributing-to-the-benchmark).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
]]>
