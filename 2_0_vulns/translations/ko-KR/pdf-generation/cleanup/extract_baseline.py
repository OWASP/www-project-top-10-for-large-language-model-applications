import sys
import os
import json
import shutil

def generate_files(base_path):
    locale = os.path.basename(os.path.normpath(base_path))
    baseline_dir = os.path.join(base_path, "baseline")
    json_filename = f"custom_data_LLM_{locale}.json"
    json_path = os.path.join(baseline_dir, json_filename)

    if not os.path.exists(json_path):
        print(f"Error: JSON file '{json_filename}' not found in {baseline_dir}")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # ADD00_Cover.md
    doc_header = data.get("doc_header", "")
    doc_subtitles = data.get("doc_subtitles", [])
    cover_lines = [f"# {doc_header}\n"]
    cover_lines += [f"##### {subtitle}" for subtitle in doc_subtitles if subtitle.strip()]
    with open(os.path.join(base_path, "ADD00_Cover.md"), 'w', encoding='utf-8') as f:
        f.write("\n\n".join(cover_lines))

    # ADD01_Table_of_Contents.md
    toc_title = data.get("doc_toc_contents_title", "")
    with open(os.path.join(base_path, "ADD01_Table_of_Contents.md"), 'w', encoding='utf-8') as f:
        f.write(f"###### {toc_title}\n")

    # ADD02_Figures.md
    figures_title = data.get("doc_toc_figures_title", "")
    with open(os.path.join(base_path, "ADD02_Figures.md"), 'w', encoding='utf-8') as f:
        f.write(f"###### {figures_title}\n")

    # Rename Supplemental_Content.md → ADD04_Supplemental_Content.md
    supplemental_src = os.path.join(base_path, "Supplemental_Content.md")
    supplemental_dest = os.path.join(base_path, "ADD04_Supplemental_Content.md")
    if os.path.exists(supplemental_src):
        os.rename(supplemental_src, supplemental_dest)
        print(f"Renamed '{supplemental_src}' → '{supplemental_dest}'")

    # Delete baseline directory
    try:
        shutil.rmtree(baseline_dir)
        print(f"Deleted '{baseline_dir}' and its contents.")
    except Exception as e:
        print(f"Error deleting baseline directory: {e}")

    print("All files generated and cleanup complete.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_files.py <directory_path>")
    else:
        generate_files(sys.argv[1])

