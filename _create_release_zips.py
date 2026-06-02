import zipfile
import os

def create_zip(base_dir, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(base_dir):
            for f in files:
                filepath = os.path.join(root, f)
                arcname = os.path.relpath(filepath, base_dir)
                zf.write(filepath, arcname)
    size_kb = os.path.getsize(output_path) / 1024
    print(f"Created: {output_path} ({size_kb:.1f} KB)")

root = "Z:/QYH_code/writing_style_skill"

create_zip(
    os.path.join(root, ".release-staging", "agent"),
    os.path.join(root, "dist", "writing-style-distiller-agent.zip")
)

create_zip(
    os.path.join(root, ".release-staging", "claude-code-project"),
    os.path.join(root, "dist", "writing-style-distiller-claude-code-project-skill.zip")
)

print("\nAll zips created. Listing dist/:")
for f in os.listdir(os.path.join(root, "dist")):
    fp = os.path.join(root, "dist", f)
    print(f"  {f}: {os.path.getsize(fp) / 1024:.1f} KB")
