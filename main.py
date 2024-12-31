from datetime import datetime

# Path to the README file
readme_file = "README.md"

# Placeholder in the README file
placeholder = "<!--LAST_UPDATED-->"

# Get the current timestamp in UTC
current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

# Read the current contents of the README file
with open(readme_file, "r", encoding="utf-8") as file:
    content = file.readlines()

# Update the placeholder with the current timestamp
updated_content = []
for line in content:
    if placeholder in line:
        updated_content.append(f"{placeholder} {current_time}\n")
    else:
        updated_content.append(line)

# Write the updated content back to the README file
with open(readme_file, "w", encoding="utf-8") as file:
    file.writelines(updated_content)

print(f"README.md updated with the current timestamp: {current_time}")
