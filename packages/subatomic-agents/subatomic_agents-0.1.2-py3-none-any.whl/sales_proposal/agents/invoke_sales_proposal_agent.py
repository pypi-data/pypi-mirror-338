from sales_proposal.agents.sales_proposal_agent import create_sales_proposal_agent

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_sales_proposal_agent():
    return create_sales_proposal_agent()