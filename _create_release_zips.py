import zipfile
import os
import shutil

root = "Z:/QYH_code/writing_style_skill"
source_dir = os.path.join(root, ".claude", "skills", "writing-style-distiller")
staging_dir = os.path.join(root, ".release-staging")
dist_dir = os.path.join(root, "dist")

# --- 同步源文件到 release-staging ---

agent_dest = os.path.join(staging_dir, "agent", "writing-style-distiller")
project_dest = os.path.join(
    staging_dir, "claude-code-project", ".claude", "skills", "writing-style-distiller"
)

def sync_source_to_staging(src, dest):
    """清空目标目录后，从源目录完整复制（排除开发专用文件）。"""
    if os.path.exists(dest):
        shutil.rmtree(dest)
    # 排除不需要打包的开发文件
    exclude = {"verification-notes.md"}
    def ignore_fn(directory, files):
        return [f for f in files if f in exclude]
    shutil.copytree(src, dest, ignore=ignore_fn)
    print(f"Synced: {src} -> {dest}")

print("=== Syncing source to release-staging ===")
sync_source_to_staging(source_dir, agent_dest)
sync_source_to_staging(source_dir, project_dest)

# --- 创建发布 zip ---

os.makedirs(dist_dir, exist_ok=True)

def create_zip(base_dir, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for dirpath, dirs, files in os.walk(base_dir):
            for f in files:
                filepath = os.path.join(dirpath, f)
                arcname = os.path.relpath(filepath, base_dir)
                zf.write(filepath, arcname)
    size_kb = os.path.getsize(output_path) / 1024
    print(f"Created: {output_path} ({size_kb:.1f} KB)")

print("\n=== Creating release zips ===")
create_zip(
    os.path.join(staging_dir, "agent"),
    os.path.join(dist_dir, "writing-style-distiller-agent.zip")
)
create_zip(
    os.path.join(staging_dir, "claude-code-project"),
    os.path.join(dist_dir, "writing-style-distiller-claude-code-project-skill.zip")
)

print("\nAll zips created. Listing dist/:")
for f in os.listdir(dist_dir):
    fp = os.path.join(dist_dir, f)
    print(f"  {f}: {os.path.getsize(fp) / 1024:.1f} KB")
