# Tax Model definitions
'''
tax_models = [
    ("W2", "W-2 Wage and Tax Statement"),
    ("W-4", "W-4 Employee's Withholding Certificate"),
    ("1095A", "Form 1095-A Health Insurance Marketplace Statement"),
    ("1095C", "Form 1095-C Employer-Provided Health Insurance Offer and Coverage"),
    ("1098", "Form 1098 Mortgage Interest Statement"),
    ("1098E", "Form 1098-E Student Loan Interest Statement"),
    ("1098T", "Form 1098-T Tuition Statement"),
    ("1099A", "Form 1099-A Acquisition or Abandonment of Secured Property"),
    ("1099B", "Form 1099-B Proceeds from Broker and Barter Exchange Transactions"),
    ("1099C", "Form 1099-C Cancellation of Debt"),
    ("1099CAP", "Form 1099-CAP Changes in Corporate Control and Capital Structure"),
    ("1099DIV", "Form 1099-DIV Dividends and Distributions"),
    ("1099G", "Form 1099-G Certain Government Payments"),
    ("1099H", "Form 1099-H Health Coverage Tax Credit (HCTC) Advance Payments"),
    ("1099INT", "Form 1099-INT Interest Income"),
    ("1099K", "Form 1099-K Payment Card and Third Party Network Transactions"),
    ("1099LS", "Form 1099-LS Reportable Life Insurance Sale"),
    ("1099LTC", "Form 1099-LTC Long-Term Care and Accelerated Death Benefits"),
    ("1099MISC", "Form 1099-MISC Miscellaneous Income"),
    ("1099NEC", "Form 1099-NEC Nonemployee Compensation"),
    ("1099OID", "Form 1099-OID Original Issue Discount"),
    ("1099PATR", "Form 1099-PATR Taxable Distributions Received from Cooperatives"),
    ("1099Q", "Form 1099-Q Payments from Qualified Education Programs"),
    ("1099QA", "Form 1099-QA Distributions from ABLE Accounts"),
    ("1099R", "Form 1099-R Distributions from Pensions, Annuities, Retirement or Profit-Sharing Plans"),
    ("1099S", "Form 1099-S Proceeds from Real Estate Transactions"),
    ("1099SA", "Form 1099-SA Distributions from an HSA, Archer MSA, or Medicare Advantage MSA"),
    ("1099SB", "Form 1099-SB Seller's Investment in Life Insurance Contract"),
    ("1099SSA", "Form SSA-1099 Social Security Benefit Statement"),
    ("1040", "Form 1040 U.S. Individual Income Tax Return"),
    ("1040Schedule1", "Schedule 1 Additional Income and Adjustments to Income"),
    ("1040Schedule2", "Schedule 2 Additional Taxes"),
    ("1040Schedule3", "Schedule 3 Additional Credits and Payments"),
    ("1040Schedule8812", "Schedule 8812 Credits for Qualifying Children and Other Dependents"),
    ("1040ScheduleA", "Schedule A Itemized Deductions"),
    ("1040ScheduleB", "Schedule B Interest and Ordinary Dividends"),
    ("1040ScheduleC", "Schedule C Profit or Loss from Business"),
    ("1040ScheduleD", "Schedule D Capital Gains and Losses"),
    ("1040ScheduleE", "Schedule E Supplemental Income and Loss"),
    ("1040ScheduleEIC", "Schedule EIC Earned Income Credit"),
    ("1040ScheduleF", "Schedule F Profit or Loss from Farming")
]
'''

# List of supported tax models (as named in Document Intelligence)

tax_models = ['W2', '1095A', '1099B', '1099DIV', '1099G', 
'1099INT', '1099MISC', '1099NEC', '1099R', '1099SSA']

unused_tax_models = [
    "W-4", "1095C", "1098", "1098E", "1098T",
    "1099A", "1099C", "1099CAP",
    "1099H", "1099K", "1099LS", "1099LTC",
    "1099OID", "1099PATR", "1099Q", "1099QA", "1099S", 
    "1099SA", "1099SB",
    "1040", "1040Schedule1", "1040Schedule2", "1040Schedule3",
    "1040Schedule8812", "1040ScheduleA", "1040ScheduleB",
    "1040ScheduleC", "1040ScheduleD", "1040ScheduleE",
    "1040ScheduleEIC", "1040ScheduleF"
]

# List of tax models built entirely within LLM

custom_tax_models = ["1099-CONSOLIDATED"]


def process_document(doc_type):
    """
    Determines which model to use based on document type.
    """
    if doc_type in tax_models:
        return f"Pass to Document Intelligence Prebuilt Tax Model for '{doc_type}'"
    elif doc_type in unused_tax_models:
        return "Label as 'Miscellaneous'"
    elif doc_type in custom_tax_models:
        return "Pass to LLM Extraction Model (to-be-built)"
    else:
        return "Label as 'Miscellaneous'"

# Example usage:
identified_docs = ["W2", "1099-CONSOLIDATED", "XYZ-Form"]

for doc in identified_docs:
    action = process_document(doc)
    print(f"Document: {doc} -> Action: {action}")