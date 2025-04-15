from preswald import connect, get_df, text, table, plotly
import plotly.express as px
import pandas as pd

connect()

# Load the dataset
df = get_df("ai_job_market_insights")

# Add headers
text("# AI Job Market Insights")
text("Data explorer for AI job market trends")

# Show key statistics
text("## Key Statistics")
avg_salary = int(df["Salary_USD"].mean())
remote_percentage = int((df["Remote_Friendly"] == "Yes").mean() * 100)
high_risk_percentage = int((df["Automation_Risk"] == "High").mean() * 100)

text(f"- Average Salary: ${avg_salary:,}")
text(f"- Remote-Friendly Jobs: {remote_percentage}%")
text(f"- Jobs at High Automation Risk: {high_risk_percentage}%")

# Show top industries by average salary
text("## Top Industries by Average Salary")
industry_salary = df.groupby("Industry")["Salary_USD"].mean().reset_index()
industry_salary = industry_salary.sort_values("Salary_USD", ascending=False)
table(industry_salary)

# Create a bar chart for industry salaries
fig1 = px.bar(
    industry_salary,
    x="Industry",
    y="Salary_USD",
    title="Average Salary by Industry",
    labels={"Salary_USD": "Average Salary (USD)"}
)
plotly(fig1)

# Show most common job titles
text("## Most Common Job Titles")
job_counts = df["Job_Title"].value_counts().reset_index()
job_counts.columns = ["Job_Title", "Count"]
job_counts = job_counts.head(10)
table(job_counts)

# Show in-demand skills
text("## Most In-Demand Skills")
skill_counts = df["Required_Skills"].value_counts().reset_index()
skill_counts.columns = ["Skill", "Count"]
skill_counts = skill_counts.head(10)
table(skill_counts)