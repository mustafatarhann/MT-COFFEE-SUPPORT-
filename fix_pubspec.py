with open('pubspec.yaml', 'r') as f:
    lines = f.readlines()

new_lines = []
seen_keys = set()
in_overrides = False

for line in lines:
    stripped = line.strip()
    if 'dependency_overrides:' in stripped:
        in_overrides = True
        new_lines.append(line)
        continue
    
    if in_overrides and ':' in stripped and not stripped.startswith('#'):
        key = stripped.split(':')[0].strip()
        if key in seen_keys:
            continue
        seen_keys.add(key)
    elif not in_overrides or stripped == '':
        if stripped == '':
            seen_keys.clear()
            in_overrides = False

    new_lines.append(line)

with open('pubspec.yaml', 'w') as f:
    f.writelines(new_lines)
