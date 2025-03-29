#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crewai_stn_analysis.crew import CrewaiStnAnalysis

#warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

#!/usr/bin/env python
# src/crewai_stn_analysis/main.py

import os
from crewai_stn_analysis.crew import STNCrew

def run():
    """
    Run the STN analysis crew on a given topic.
    """
    os.makedirs("output", exist_ok=True)

    # Customize your topic (this value replaces {topic} in the YAML files)
    inputs = {
        "topic": "Search Trajectory Networks of GA, BO, and CPPN-NEAT in EvoGym"
    }

    crew = STNCrew()
    result = crew.crew().kickoff(inputs=inputs)

    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)
    print("\n\nReport saved to output/stn_analysis_report.md")

if __name__ == "__main__":
    run()
