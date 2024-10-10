from langchain_core.tools import StructuredTool
from pydantic import BaseModel

def write_report(filename, html):
    with open(filename, "w") as f:
        f.write(html)

class WriteReportArgsSchema(BaseModel):
    filename: str
    html: str

write_report_tool = StructuredTool.from_function(
    func=write_report,
    name="write_report",
    description="Write a report to an html file. Use this tool whenever you need to write a report.",
    args_schema=WriteReportArgsSchema,
)
