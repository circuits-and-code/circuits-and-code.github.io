import subprocess

if __name__ == '__main__':
    """Deploy the site for temp use"""
    cmd = "bundle exec jekyll serve"

    SITE_DIR = "."

    try:
        print(f"Running command: {cmd}")
        subprocess.run(cmd, shell=True, check=True, cwd=SITE_DIR)
    except subprocess.CalledProcessError as e:
        print(e)
        exit(1)