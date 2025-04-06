# Subatomic Agents API 

**Subatomic Agents** is a modular, enterprise-grade AI framework by [Subatomic](https://www.getsubatomic.ai) for automating and scaling business intelligence workflows using agent-based architectures.

*This package provides the **Sales Proposal Agent**, which transforms meeting transcripts and summaries into structured, client-ready sales proposals.*

---

## *🚀 Features*

- *Includes the Sales Proposal Agent for generating structured, client-ready proposals from meeting inputs*

---

## *📆 Installation*

*Install via *[*PyPI*](https://pypi.org/project/subatomic-agents/)*:*

```bash
pip install subatomic-agents
```

---

## *🧠 Usage*

```python
from sales_proposal import SalesProposalInput, SalesProposalGeneratorService

inputs = SalesProposalInput(
    meeting_summary_urls=[
        "https://docs.google.com/document/d/1J18PJ0EKi54VU3RfNaJpiO5GIaQ-6maf/edit"
    ],
    meeting_summary_file_types=["gdoc"],
    meeting_transcript_url=(
        "https://docs.google.com/document/d/1cGE1I7_eU2b2PoV2ojilKuhaWj5FpnHu/edit"
    ),
    meeting_transcript_file_type="gdoc"
)

service = SalesProposalGeneratorService(inputs)
result, status = service.generate()

print("FINAL RESULT =>", result)
```

---

## *📂 Output*

*Returns a structured JSON dictionary representing the sales proposal (excluding internal vector data).*\
*The result is also saved to **`sales_proposal_result.txt`**.*

---

## *➕ Extending the Framework*

*This framework is modular and designed for easy extension:*

- *Add new agents in **`agents/`***
- *Define prompt strategies in **`factories/`***
- *Extend the generation flow via **`SalesProposalGeneratorService`***

---

## *🧪 Requirements*

- *Python 3.9+*
- *Compatible with **`uv`**, **`pip`**, or **`poetry`**-based environments*

---

## *👥 Authors*

*Built by *[*Subatomic Technologies*](https://www.getsubatomic.ai)*

- *Karl Simon · *[*karl@getsubatomic.ai*](mailto:karl@getsubatomic.ai)*
- *Aaron Sosa · *[*wilfredo@getsubatomic.ai*](mailto:wilfredo@getsubatomic.ai)*

---