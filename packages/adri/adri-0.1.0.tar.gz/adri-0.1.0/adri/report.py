"""
Assessment report generation and handling for the Agent Data Readiness Index.

This module provides the AssessmentReport class that encapsulates the results
of an ADRI assessment and provides methods to save, load, and visualize reports.
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Union

import matplotlib.pyplot as plt
import pandas as pd
from jinja2 import Environment, FileSystemLoader

logger = logging.getLogger(__name__)


class AssessmentReport:
    """Encapsulates the results of an ADRI assessment."""

    def __init__(
        self,
        source_name: str,
        source_type: str,
        source_metadata: Dict[str, Any],
        assessment_time: Optional[datetime] = None,
    ):
        """
        Initialize an assessment report.

        Args:
            source_name: Name of the assessed data source
            source_type: Type of data source (file, database, api, etc.)
            source_metadata: Metadata about the data source
            assessment_time: When the assessment was performed
        """
        self.source_name = source_name
        self.source_type = source_type
        self.source_metadata = source_metadata
        self.assessment_time = assessment_time or datetime.now()
        
        # These will be populated by populate_from_dimension_results
        self.overall_score = 0
        self.readiness_level = ""
        self.dimension_results = {}
        self.summary_findings = []
        self.summary_recommendations = []

    def populate_from_dimension_results(self, dimension_results: Dict[str, Dict[str, Any]]):
        """
        Populate the report with results from dimension assessments.

        Args:
            dimension_results: Dictionary of results for each dimension
        """
        self.dimension_results = dimension_results
        
        # Calculate overall score (simple average for now)
        dimension_scores = [d["score"] for d in dimension_results.values()]
        self.overall_score = sum(dimension_scores) / len(dimension_scores)
        
        # Determine readiness level
        self.readiness_level = self._calculate_readiness_level(self.overall_score)
        
        # Gather key findings and recommendations
        for dim_name, results in dimension_results.items():
            # Add most critical findings (for now, just take the first 2)
            for finding in results["findings"][:2]:
                self.summary_findings.append(f"[{dim_name.title()}] {finding}")
            
            # Add most important recommendations (for now, just take the first)
            for recommendation in results["recommendations"][:1]:
                self.summary_recommendations.append(f"[{dim_name.title()}] {recommendation}")

    def _calculate_readiness_level(self, score: float) -> str:
        """
        Calculate the readiness level based on overall score.

        Args:
            score: Overall assessment score (0-100)

        Returns:
            str: Readiness level description
        """
        if score >= 80:
            return "Advanced - Ready for critical agentic applications"
        elif score >= 60:
            return "Proficient - Suitable for most production agent uses"
        elif score >= 40:
            return "Basic - Requires caution in agent applications"
        elif score >= 20:
            return "Limited - Significant agent blindness risk"
        else:
            return "Inadequate - Not recommended for agentic use"

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the report to a dictionary.

        Returns:
            Dict: Dictionary representation of the report
        """
        return {
            "source_name": self.source_name,
            "source_type": self.source_type,
            "source_metadata": self.source_metadata,
            "assessment_time": self.assessment_time.isoformat(),
            "overall_score": self.overall_score,
            "readiness_level": self.readiness_level,
            "dimension_results": self.dimension_results,
            "summary_findings": self.summary_findings,
            "summary_recommendations": self.summary_recommendations,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AssessmentReport":
        """
        Create a report from a dictionary.

        Args:
            data: Dictionary representation of a report

        Returns:
            AssessmentReport: Reconstructed report object
        """
        report = cls(
            source_name=data["source_name"],
            source_type=data["source_type"],
            source_metadata=data["source_metadata"],
            assessment_time=datetime.fromisoformat(data["assessment_time"]),
        )
        report.overall_score = data["overall_score"]
        report.readiness_level = data["readiness_level"]
        report.dimension_results = data["dimension_results"]
        report.summary_findings = data["summary_findings"]
        report.summary_recommendations = data["summary_recommendations"]
        return report

    def save_json(self, path: Union[str, Path]):
        """
        Save the report to a JSON file.

        Args:
            path: Path to save the report
        """
        with open(path, "w") as f:
            json.dump(self.to_dict(), f, indent=2)
        logger.info(f"Report saved to {path}")

    @classmethod
    def load_json(cls, path: Union[str, Path]) -> "AssessmentReport":
        """
        Load a report from a JSON file.

        Args:
            path: Path to the report file

        Returns:
            AssessmentReport: Loaded report
        """
        with open(path, "r") as f:
            data = json.load(f)
        return cls.from_dict(data)

    def generate_radar_chart(self, save_path: Optional[Union[str, Path]] = None):
        """
        Generate a radar chart visualization of the dimension scores.

        Args:
            save_path: Optional path to save the chart
        """
        # Extract dimension names and scores
        dimensions = list(self.dimension_results.keys())
        scores = [self.dimension_results[dim]["score"] for dim in dimensions]
        
        # Create radar chart
        fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={"polar": True})
        
        # Compute angles for each dimension
        angles = [n / float(len(dimensions)) * 2 * 3.14159 for n in range(len(dimensions))]
        angles += angles[:1]  # Close the loop
        
        # Add scores and close loop
        scores += scores[:1]
        
        # Plot data
        ax.plot(angles, scores, linewidth=2, linestyle="solid")
        ax.fill(angles, scores, alpha=0.25)
        
        # Fix axis to start at top and correct direction
        ax.set_theta_offset(3.14159 / 2)
        ax.set_theta_direction(-1)
        
        # Set axis labels
        plt.xticks(angles[:-1], [d.title() for d in dimensions])
        
        # Set y-axis
        ax.set_rlabel_position(0)
        plt.yticks([5, 10, 15, 20], ["5", "10", "15", "20"], color="grey", size=8)
        plt.ylim(0, 20)
        
        # Add title
        plt.title(
            f"Agent Data Readiness Index: {self.source_name}\n"
            f"Overall Score: {self.overall_score:.1f}/100 ({self.readiness_level.split(' - ')[0]})",
            size=15,
            y=1.1,
        )
        
        if save_path:
            plt.savefig(save_path, bbox_inches="tight")
            logger.info(f"Radar chart saved to {save_path}")
        return fig

    def save_html(self, path: Union[str, Path]):
        """
        Save the report as an HTML file.

        Args:
            path: Path to save the HTML report
        """
        # Get the directory where this module is located
        module_dir = Path(__file__).parent
        templates_dir = module_dir / "templates"
        
        # Check if the template file exists
        template_file = templates_dir / "report_template.html"
        if not template_file.exists():
            raise FileNotFoundError(f"Template file not found: {template_file}")
        
        # Configure Jinja2
        env = Environment(loader=FileSystemLoader(str(templates_dir)))
        template = env.get_template("report_template.html")
        
        # Generate radar chart and encode it in base64
        import tempfile
        import base64
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            self.generate_radar_chart(tmp.name)
            with open(tmp.name, "rb") as img_file:
                radar_b64 = base64.b64encode(img_file.read()).decode("utf-8")
        
        # Render HTML template
        html_content = template.render(
            report=self,
            radar_chart_b64=radar_b64,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        
        # Save the rendered HTML report
        with open(path, "w", encoding="utf-8") as f:
            f.write(html_content)
        logger.info(f"HTML report saved to {path}")

    def print_summary(self):
        """Print a summary of the report to the console."""
        print(f"\n=== Agent Data Readiness Index: {self.source_name} ===")
        print(f"Overall Score: {self.overall_score:.1f}/100")
        print(f"Readiness Level: {self.readiness_level}")
        print("\nDimension Scores:")
        for dim, results in self.dimension_results.items():
            print(f"  {dim.title()}: {results['score']:.1f}/20")
        
        print("\nKey Findings:")
        for finding in self.summary_findings:
            print(f"  - {finding}")
            
        print("\nTop Recommendations:")
        for rec in self.summary_recommendations:
            print(f"  - {rec}")
