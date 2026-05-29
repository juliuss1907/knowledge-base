import re

def load_taxonomy(tags_file):
    with open(tags_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    main_tags = {}
    sub_tags = {}
    
    sections = re.split(r'## \d+\.', text)
    print(f"DEBUG: Total sections found: {len(sections)}")
    
    for i, section in enumerate(sections):
        print(f"DEBUG: Section {i} contains 'Pool A': {'Pool A' in section}")
        print(f"DEBUG: Section {i} contains 'Pool B': {'Pool B' in section}")
        if 'Pool A' in section:
            for line in section.split('\n'):
                if line.startswith('|') and '---' not in line and 'Tag' not in line:
                    print(f"DEBUG: Processing Pool A line: {line}")
                    parts = line.split('|')
                    if len(parts) >= 3:
                        tag = parts[1].strip().lstrip('#')
                        desc = parts[2].strip()
                        main_tags[tag] = desc
        elif 'Pool B' in section:
            for line in section.split('\n'):
                if line.startswith('|') and '---' not in line and 'Tag' not in line:
                    print(f"DEBUG: Processing Pool B line: {line}")
                    parts = line.split('|')
                    if len(parts) >= 3:
                        tag = parts[1].strip().lstrip('#')
                        desc = parts[2].strip()
                        sub_tags[tag] = desc
                
    return main_tags, sub_tags

main_allowed, sub_allowed = load_taxonomy('TAGS.md')
print(f"RESULT main_allowed: {main_allowed}")
print(f"RESULT sub_allowed: {sub_allowed}")
