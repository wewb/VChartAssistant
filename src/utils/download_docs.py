import os
import git
import shutil
from pathlib import Path

def download_docs():
    # 设置临时目录和目标目录
    temp_dir = "temp_repo"
    docs_dir = "data/docs"
    repo_url = "https://github.com/VisActor/VChart.git"
    docs_path = "docs/assets"
    
    try:
        # 创建目标目录
        Path(docs_dir).mkdir(parents=True, exist_ok=True)
        
        # 克隆仓库
        print("Cloning repository...")
        repo = git.Repo.clone_from(repo_url, temp_dir, branch='develop')
        
        # 复制文档
        source_path = os.path.join(temp_dir, docs_path)
        print(f"Copying documents from {source_path} to {docs_dir}")
        
        # 遍历并复制所有 markdown 文件
        for root, _, files in os.walk(source_path):
            for file in files:
                if file.endswith('.md'):
                    src_file = os.path.join(root, file)
                    # 保持目录结构
                    rel_path = os.path.relpath(src_file, source_path)
                    dst_file = os.path.join(docs_dir, rel_path)
                    
                    # 确保目标目录存在
                    os.makedirs(os.path.dirname(dst_file), exist_ok=True)
                    shutil.copy2(src_file, dst_file)
                    print(f"Copied: {rel_path}")
        
        print("Documents downloaded successfully!")
        
    except Exception as e:
        print(f"Error: {str(e)}")
    
    finally:
        # 清理临时目录
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

if __name__ == "__main__":
    download_docs()
