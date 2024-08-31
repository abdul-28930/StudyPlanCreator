from analyzer import process_curriculum_file, analyze_curriculum
from docCreator import create_learning_plan

def main():
    file_path = input("Please enter the path to your curriculum file (.pdf or .docx): ")

    curriculum_text = process_curriculum_file(file_path)

    analysis_text = analyze_curriculum(curriculum_text)

    create_learning_plan(analysis_text)

    print("Learning plan document has been created as a PDF.")

if __name__ == "__main__":
    main()
