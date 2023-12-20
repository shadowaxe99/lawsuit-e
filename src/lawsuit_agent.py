from gpt4_lawsuit_writer import GPT4LawsuitWriter
from user_interface_module import collect_lawsuit_details, review_and_edit
from write_file_tool import WriteFileTool


class LawsuitAgent:
    def __init__(self):
        self.lawsuit_writer = GPT4LawsuitWriter()
        self.write_file_tool = WriteFileTool()

    def gather_user_input(self):
        return collect_lawsuit_details()

    def analyze_case(self, user_data):
        return self.lawsuit_writer.analyze_case(user_data)

    def generate_lawsuit_draft(self, case_analysis):
        return self.lawsuit_writer.generate_lawsuit_draft(case_analysis)

    def review_and_edit_draft(self, draft):
        return review_and_edit(draft)

    def finalize_document(self, edited_draft):
        return self.lawsuit_writer.finalize_document(edited_draft)

    def write_lawsuit_document(self, final_document, file_path):
        payload = {
            "file_path": file_path,
            "code": final_document
        }
        self.write_file_tool.run(payload, config, llm, query_response)

def main():
    lawsuit_agent = LawsuitAgent()
    user_data = lawsuit_agent.gather_user_input()
    case_analysis = lawsuit_agent.analyze_case(user_data)
    draft = lawsuit_agent.generate_lawsuit_draft(case_analysis)
    edited_draft = lawsuit_agent.review_and_edit_draft(draft)
    final_document = lawsuit_agent.finalize_document(edited_draft)
    lawsuit_agent.write_lawsuit_document(final_document, "path/to/lawsuit_document.txt")

if __name__ == "__main__":
    main()
