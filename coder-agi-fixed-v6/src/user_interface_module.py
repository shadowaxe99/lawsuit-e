def collect_lawsuit_details():
    """
    Collect detailed lawsuit information from the user.
    """
    print("Please answer the following questions to provide detailed information about your lawsuit:")

    # Detailed data collection
    details = {}
    details["Case Title"] = input("Case Title: ")
    
    # Plaintiff and Defendant Details
    details["Plaintiff Name"] = input("Plaintiff Name: ")
    details["Defendant Name"] = input("Defendant Name: ")

    # Detailed Case Information
    details["Case Summary"] = input("Brief Summary of the Case: ")
    details["Key Facts"] = input("Key Facts (please list major points): ")
    details["Claims"] = input("Claims/Allegations: ")
    details["Evidence Summary"] = input("Summary of Evidence: ")
    
    # Legal Grounds
    details["Legal Grounds for Claims"] = input("Legal Grounds for Claims: ")
    details["Requested Relief"] = input("Requested Relief (compensation/damages/etc.): ")
    
    # Jurisdiction and Court Details
    details["Jurisdiction"] = input("Jurisdiction (location of the lawsuit): ")
    details["Court Type"] = input("Type of Court (e.g., Small Claims, Federal, State): ")

    # Additional Information
    details["Previous Legal Actions"] = input("Have there been any previous legal actions? Describe: ")
    details["Any Other Relevant Information"] = input("Any Other Relevant Information: ")

    return details

def review_and_edit(draft):
    """
    Allow detailed section-wise review and edit of the draft.
    """
    print("\nReview and Edit the Draft Lawsuit Document:\n")
    
    # Section-wise editing
    edited_draft = {}
    for section, content in draft.items():
        print(f"Current {section}:")
        print(content)
        edited_draft[section] = input(f"Edit {section} (leave blank to keep as is): ").strip() or content

    # Constructing the edited draft
    return "\n".join(edited_draft.values())