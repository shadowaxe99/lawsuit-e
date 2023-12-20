def collect_lawsuit_details():
    """
    Collect detailed lawsuit information from the user.

    Returns:
        dict: A dictionary containing the collected lawsuit details.
    """
    details = {}

    details["Case Title"] = input("Enter the Case Title: ")
    details["Plaintiff Name"] = input("Enter the Plaintiff Name: ")
    details["Defendant Name"] = input("Enter the Defendant Name: ")
    details["Case Summary"] = input("Enter a Brief Summary of the Case: ")
    details["Key Facts"] = input("Enter the Key Facts (please list major points): ")
    details["Claims"] = input("Enter the Claims/Allegations: ")
    details["Evidence Summary"] = input("Enter a Summary of Evidence: ")
    details["Legal Grounds for Claims"] = input("Enter the Legal Grounds for Claims: ")
    details["Requested Relief"] = input("Enter the Requested Relief (compensation/damages/etc.): ")
    details["Jurisdiction"] = input("Enter the Jurisdiction (location of the lawsuit): ")
    details["Court Type"] = input("Enter the Type of Court (e.g., Small Claims, Federal, State): ")
    details["Previous Legal Actions"] = input("Have there been any previous legal actions? Describe: ")
    details["Any Other Relevant Information"] = input("Enter Any Other Relevant Information: ")

    return details


def review_and_edit(draft):
    """
    Allow section-wise review and edit of the draft.

    Args:
        draft (dict): The draft lawsuit document.

    Returns:
        dict: The edited draft lawsuit document.
    """
    edited_draft = {}

    for section, content in draft.items():
        print(f"Current {section}:")
        print(content)
        edited_content = input(f"Edit {section} (leave blank to keep as is): ").strip() or content
        edited_draft[section] = edited_content

    return edited_draft
