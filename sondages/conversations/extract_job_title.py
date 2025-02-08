import json
import os
import pandas as pd
from collections import defaultdict

# Flag pour activer ou désactiver le débogage
DEBUG = False

def debug_print(message):
    if DEBUG:
        print(message)

def extract_job_titles_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return extract_job_titles_and_candidates(data, file_path)

def extract_job_titles_and_candidates(json_data, file_path):
    job_info = []
    candidate_name = None
    job_title = None

    for entry in json_data:
        message = entry.get('message', '')
        debug_print(f"Processing message: {message}")

        if entry['role'] == 'Recruteur' and "vous postulez pour le poste de" in message:
            start_index = message.find("vous postulez pour le poste de") + len("vous postulez pour le poste de")
            job_title = message[start_index:].split(',')[0].strip()
            debug_print(f"Found job title: {job_title}")

        if entry['role'] == 'Recruteur' and "Bonjour" in message:
            # Extract candidate name after "Bonjour "
            candidate_name = message.split("Bonjour ")[1].split(',')[0].strip()
            debug_print(f"Found candidate name: {candidate_name}")

        if job_title and candidate_name:
            job_info.append({
                'Job Title': job_title,
                'File': os.path.basename(file_path),
                'Candidate Name': candidate_name
            })
            debug_print(f"Appending job info: {job_info[-1]}")
            # Reset to avoid duplication in the same file
            job_title = None
            candidate_name = None

    return job_info

def extract_job_info_from_directory(directory_path):
    job_dict = defaultdict(lambda: {'Files': [], 'Candidate Names': []})
    files_analyzed_count = 0

    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)
            files_analyzed_count += 1
            debug_print(f"Processing file: {file_path}")
            job_info = extract_job_titles_from_file(file_path)

            for info in job_info:
                job_dict[info['Job Title']]['Files'].append(info['File'])
                job_dict[info['Job Title']]['Candidate Names'].append(info['Candidate Name'])

    # Convert to DataFrame for better visualization
    df = pd.DataFrame([
        {
            'Job Title': job_title,
            'Files': ', '.join(files),
            'Candidate Names': ', '.join(candidate_names)
        }
        for job_title, files_candidates in job_dict.items()
        for files, candidate_names in [(files_candidates['Files'], files_candidates['Candidate Names'])]
    ])

    return df.reset_index(drop=True), files_analyzed_count, len(job_dict)

def save_report_to_markdown(df, files_analyzed_count, job_count, output_path):
    os.makedirs(output_path, exist_ok=True)
    markdown_path = os.path.join(output_path, 'rapport_postes_candidats.md')

    with open(markdown_path, 'w', encoding='utf-8') as md_file:
        md_file.write("# Rapport des Postes et Candidats\n\n")
        md_file.write(f"**Nombre de fichiers analysés :** {files_analyzed_count}\n\n")
        md_file.write(f"**Nombre de postes trouvés :** {job_count}\n\n")
        md_file.write(df.to_markdown(index=False))

    print(f"Rapport généré et enregistré à : {markdown_path}")

# Parcourir les fichiers JSON dans le répertoire courant
directory_path = './'
job_info_df, files_analyzed_count, job_count = extract_job_info_from_directory(directory_path)

# Sauvegarder le rapport au format Markdown
output_directory = './output'
save_report_to_markdown(job_info_df, files_analyzed_count, job_count, output_directory)
