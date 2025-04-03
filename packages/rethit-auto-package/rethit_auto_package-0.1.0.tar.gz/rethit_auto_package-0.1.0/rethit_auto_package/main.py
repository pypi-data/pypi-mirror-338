import re
import os
import sys
import requests
import json
import shutil
from packaging.specifiers import SpecifierSet
from datetime import datetime

# Python 표준 라이브러리 목록
STANDARD_LIBS = {
    'modulefinder', 'glob', 'ast', 're', 'os', 'json', 'argparse', 'collections',
    'logging', 'sys', 'subprocess', 'datetime', 'concurrent', 'time', 'math',
    'random', 'shutil', 'pathlib', 'threading', 'functools', 'itertools'
}

# 1. 디렉토리 내 모든 소스에서 연관 패키지 추출
def extract_packages_from_directory(directory):
    packages = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    imports = re.findall(r'^\s*import\s+([\w.]+)|from\s+([\w.]+)\s+import', content, re.MULTILINE)
                    for imp in imports:
                        for pkg in imp:
                            if pkg and not pkg.startswith('.'):
                                top_level_pkg = pkg.split('.')[0]
                                packages.add(top_level_pkg)
    return packages - STANDARD_LIBS

# 2. PyPI에서 패키지 정보 가져오기 및 호환성 체크
def check_package_compatibility(packages):
    python_versions = ['3.6', '3.7', '3.8', '3.9', '3.10', '3.11', '3.12']
    package_info = {'by_version': {}, 'by_file': {}}
    valid_packages = set()

    for pkg in packages:
        url = f"https://pypi.org/pypi/{pkg}/json"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            latest_version = data['info']['version']
            releases = data['releases'][latest_version]
            
            compatible_versions = {}
            download_files = []
            for release in releases:
                requires_python = release.get('requires_python', '>=3.0') or '>=3.0'
                file_name = release['filename']
                download_files.append(file_name)
                
                spec = SpecifierSet(requires_python)
                for py_ver in python_versions:
                    if py_ver in spec:
                        if py_ver not in compatible_versions:
                            compatible_versions[py_ver] = []
                        compatible_versions[py_ver].append(f"{pkg}=={latest_version}")
            
            package_info['by_version'][pkg] = compatible_versions
            package_info['by_file'][pkg] = download_files
            valid_packages.add(f"{pkg}=={latest_version}")
        except requests.exceptions.RequestException as e:
            print(f"패키지 {pkg} 정보 가져오기 실패: {e}")
            package_info['by_version'][pkg] = {py_ver: [] for py_ver in python_versions}
            package_info['by_file'][pkg] = []
        except Exception as e:
            print(f"패키지 {pkg} 처리 중 오류: {e}")
            package_info['by_version'][pkg] = {py_ver: [] for py_ver in python_versions}
            package_info['by_file'][pkg] = []

    return package_info, valid_packages

# 3. 패키지 구조 생성 및 CLI 추가
def create_package_structure(project_name, source_dir, main_file_name, packages):
    os.makedirs(project_name, exist_ok=True)
    package_dir = f"{project_name}/{project_name}"
    os.makedirs(package_dir, exist_ok=True)

    # 소스 디렉토리 전체 복사 (원본 유지)
    for item in os.listdir(source_dir):
        src_path = os.path.join(source_dir, item)
        dst_path = os.path.join(package_dir, item)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
        else:
            shutil.copy2(src_path, dst_path)

    # 복사된 메인 파일에 CLI 코드 추가
    packaged_main_file = os.path.join(package_dir, main_file_name)
    with open(packaged_main_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cli_code = f"""
if __name__ == "__main__":
    main()
"""
    if "
if __name__ == "__main__":
    main()
" not in content:
        content += "\n" + cli_code
    else:
        content = content.replace("
if __name__ == "__main__":
    main()
", cli_code)

    with open(packaged_main_file, 'w', encoding='utf-8') as f:
        f.write(content)

    # __init__.py 생성
    with open(f"{package_dir}/__init__.py", 'w', encoding='utf-8') as f:
        f.write(f"__version__ = '0.1.0'\n")

    # pyproject.toml 생성
    pyproject_content = """[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"
"""
    with open(f"{project_name}/pyproject.toml", 'w', encoding='utf-8') as f:
        f.write(pyproject_content)

    # setup.py 생성
    setup_content = f"""from setuptools import setup, find_packages

setup(
    name="{project_name}",
    version="0.1.0",
    packages=find_packages(),
    install_requires={list(packages)},
    entry_points={{
        'console_scripts': [
            '{project_name} = {project_name}.{main_file_name.replace(".py", "")}:main',
        ],
    }},
    python_requires='>=3.6',
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool generated from source",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
"""
    with open(f"{project_name}/setup.py", 'w', encoding='utf-8') as f:
        f.write(setup_content)

    # README.md 생성
    with open(f"{project_name}/README.md", 'w', encoding='utf-8') as f:
        f.write(f"# {project_name}\n\nA CLI tool generated from source code.\n")

    # requirements.txt 생성
    with open(f"{project_name}/requirements.txt", 'w', encoding='utf-8') as f:
        f.write('\n'.join(packages))

# 메인 실행 함수
def main():
    if len(sys.argv) != 4:
        print("사용법: python script.py <target_source_directory> <source_main_file-name> <project_name>")
        sys.exit(1)

    source_dir = sys.argv[1]
    main_file_name = sys.argv[2]
    project_name = sys.argv[3]

    if not os.path.isdir(source_dir):
        print(f"오류: {source_dir} 디렉토리가 존재하지 않습니다.")
        sys.exit(1)
    
    main_file_path = os.path.join(source_dir, main_file_name)
    if not os.path.exists(main_file_path):
        print(f"오류: {main_file_path} 파일이 존재하지 않습니다.")
        sys.exit(1)

    # 1. 패키지 추출
    packages = extract_packages_from_directory(source_dir)
    print("추출된 패키지:", packages)

    # 2. 호환성 체크
    package_info, valid_packages = check_package_compatibility(packages)
    print("패키지 호환성 정보:")
    print(json.dumps(package_info, indent=2, ensure_ascii=False))

    # 3. 패키지 구조 생성 및 CLI 추가
    create_package_structure(project_name, source_dir, main_file_name, valid_packages)

    print(f"패키지 {project_name}이 생성되었습니다.")
    print("로컬 설치 방법:")
    print(f"cd {project_name} && pip install .")
    print("빌드 패키지 생성 방법:")
    print(f"cd {project_name} && python -m build")
    print("빌드된 패키지 설치 방법:")
    print(f"cd {project_name} && pip install dist/{project_name}-0.1.0-py3-none-any.whl")
    print(f"사용 방법: {project_name} <input_file>")

if __name__ == "__main__":
    main()