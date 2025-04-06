"""Analytics models for form processing."""

import logging
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field, field_validator

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("models.analytics")


class AnalyticsResult(BaseModel):
    """
    Analytics result for form processing.

    This model contains insights, recommendations, and other analytical
    results based on the completed form data.
    """
    analysis: str = Field(..., description="Detailed analysis of the form data")
    recommendations: List[str] = Field(default_factory=list, description="Recommendations based on analysis")
    score: Optional[int] = Field(default=None, description="Numerical score (0-10)")
    insights: Dict[str, Any] = Field(default_factory=dict, description="Extracted insights")
    strengths: List[str] = Field(default_factory=list, description="Identified strengths")
    weaknesses: List[str] = Field(default_factory=list, description="Identified weaknesses")
    opportunities: List[str] = Field(default_factory=list, description="Identified opportunities")
    risks: List[str] = Field(default_factory=list, description="Identified risks")
    next_steps: List[str] = Field(default_factory=list, description="Suggested next steps")

    @field_validator("score")
    @classmethod
    def validate_score(cls, v: Optional[int]) -> Optional[int]:
        """Validate score is between 0 and 10."""
        if v is not None and not 0 <= v <= 10:
            logger.warning(f"Score out of range (0-10): {v}, clamping to valid range")
            return max(0, min(v, 10))
        return v

    def get_summary(self) -> str:
        """Get a summary of the analytics result."""
        summary_parts = [self.analysis]

        if self.score is not None:
            summary_parts.append(f"Score: {self.score}/10")

        if self.recommendations:
            summary_parts.append("\nKey recommendations:")
            for i, rec in enumerate(self.recommendations[:3], 1):
                summary_parts.append(f"{i}. {rec}")

        if self.next_steps:
            summary_parts.append("\nNext steps:")
            for i, step in enumerate(self.next_steps[:3], 1):
                summary_parts.append(f"{i}. {step}")

        return "\n".join(summary_parts)

    @classmethod
    def create_empty(cls) -> "AnalyticsResult":
        """Create an empty analytics result."""
        return cls(
            analysis="No analysis available yet.",
            recommendations=["Complete the form to receive recommendations."],
            next_steps=["Continue filling out the form."]
        )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AnalyticsResult":
        """Create an instance from a dictionary, handling missing fields."""
        # Ensure required fields are present
        if "analysis" not in data:
            data["analysis"] = "Analysis not provided."

        # Create instance
        try:
            return cls(**data)
        except Exception as e:
            logger.error(f"Error creating AnalyticsResult from dict: {e}")
            return cls.create_empty()
