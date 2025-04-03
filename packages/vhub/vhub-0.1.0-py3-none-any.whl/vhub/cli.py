import os
import sys
import json
import argparse
import hashlib
import datetime
import requests
import glob

DEFAULT_BASE_URL = 'http://localhost:6000/api'

def print_success(message):
    print(f"\033[92m{message}\033[0m")

def print_error(message):
    print(f"\033[91mError: {message}\033[0m")

def print_info(message):
    print(f"\033[94m{message}\033[0m")

def handle_response(response):
    if response.status_code >= 200 and response.status_code < 300:
        return response.json()
    else:
        try:
            error_data = response.json()
            print_error(error_data.get('error', f"Request failed with status code {response.status_code}"))
        except:
            print_error(f"Request failed with status code {response.status_code}: {response.text}")
        return None

def get_config():
    """Get the configuration from global config, local config, or defaults"""
    config = {
        'implementation': 'sqlite_fs',
        'base_url': DEFAULT_BASE_URL,
        'repo_name': os.path.basename(os.getcwd())
    }
    
    home_dir = os.path.expanduser("~")
    global_config_path = os.path.join(home_dir, '.vhub_global_config')
    
    try:
        if os.path.exists(global_config_path):
            with open(global_config_path, 'r') as f:
                global_config = json.load(f)
                config.update(global_config)
    except:
        pass
    
    try:
        if os.path.exists('.vhub/config'):
            with open('.vhub/config', 'r') as f:
                local_config = json.load(f)
                config.update(local_config)
    except:
        pass
    
    return config

def save_global_config(config):
    """Save the global configuration to ~/.vhub_global_config file"""
    home_dir = os.path.expanduser("~")
    global_config_path = os.path.join(home_dir, '.vhub_global_config')
    
    existing_config = {}
    try:
        if os.path.exists(global_config_path):
            with open(global_config_path, 'r') as f:
                existing_config = json.load(f)
    except:
        pass
    
    existing_config.update(config)
    
    with open(global_config_path, 'w') as f:
        json.dump(existing_config, f, indent=2)
    print_success(f"Global configuration saved to {global_config_path}")

def save_config(config):
    """Save the configuration to .vhub/config file"""
    os.makedirs('.vhub', exist_ok=True)
    with open('.vhub/config', 'w') as f:
        json.dump(config, f, indent=2)
    print_success(f"Configuration saved to {os.getcwd()}/.vhub/config")

def get_implementation():
    """Get the implementation from config file or default"""
    return get_config().get('implementation', 'sqlite_fs')

def get_base_url():
    """Get the base URL from config file or default"""
    return get_config().get('base_url', DEFAULT_BASE_URL)

def get_repo_name():
    """Get the repository name from current directory"""
    return get_config().get('repo_name', os.path.basename(os.getcwd()))

def generate_commit_id(data):
    """Generate a commit ID based on the commit data"""
    message = data.get("message", "")
    author = data.get("author", "")
    timestamp = data.get("timestamp", "")
    parent_id = data.get("parent_id", "")
    
    commit_string = f"{message}{author}{timestamp}{parent_id}"
    return hashlib.sha1(commit_string.encode()).hexdigest()

def get_last_commit_id():
    """Get the ID of the last commit in the current repository"""
    implementation = get_implementation()
    repo_name = get_repo_name()
    base_url = get_base_url()
    
    response = requests.get(f"{base_url}/{implementation}/commits/{repo_name}")
    if response.status_code == 200:
        commits = response.json()
        if commits and len(commits) > 0:
            return commits[0]['id']
    
    return None

def cmd_init(args):
    """Initialize a new repository"""
    implementation = args.implementation or get_implementation()
    repo_name = args.name or get_repo_name()
    base_url = args.base_url or get_base_url()
    
    response = requests.post(
        f"{base_url}/{implementation}/create_repo",
        json={"name": repo_name}
    )
    
    result = handle_response(response)
    if result:
        config = {
            'repo_name': repo_name,
            'implementation': implementation,
            'base_url': base_url
        }
        save_config(config)
        
        print_success(f"Initialized empty vHub repository '{repo_name}' using {implementation} implementation")
        print_info(f"Using API endpoint: {base_url}")
        return True
    
    return False

def cmd_config(args):
    """Configure repository settings"""
    config = get_config()
    
    if args.list:
        print_info("Current configuration:")
        for key, value in config.items():
            print(f"  {key}: {value}")
        return True
    
    changes_made = False
    global_changes = False
    local_changes = not args.global_config
    
    if args.base_url:
        if args.global_config:
            global_changes = True
        else:
            local_changes = True
        config['base_url'] = args.base_url
        changes_made = True
        print_info(f"Base URL set to: {args.base_url}")
    
    if args.implementation:
        if args.global_config:
            global_changes = True
        else:
            local_changes = True
        config['implementation'] = args.implementation
        changes_made = True
        print_info(f"Implementation set to: {args.implementation}")
    
    if args.repo_name:
        if args.global_config:
            print_error("Repository name cannot be set globally")
        else:
            local_changes = True
            config['repo_name'] = args.repo_name
            changes_made = True
            print_info(f"Repository name set to: {args.repo_name}")
    
    if global_changes:
        global_config = {k: config[k] for k in config if k != 'repo_name'}
        save_global_config(global_config)
    
    if local_changes and changes_made:
        save_config(config)
    
    if not changes_made and not args.list:
        print_error("No configuration options provided")
    
    return changes_made or args.list

def cmd_list_repos(args):
    """List all repositories"""
    implementation = args.implementation or get_implementation()
    base_url = args.base_url or get_base_url()
    
    response = requests.get(f"{base_url}/{implementation}/repos")
    result = handle_response(response)
    
    if result:
        if len(result) == 0:
            print_info("No repositories found")
        else:
            print_info("Repositories:")
            for repo in result:
                print(f"  {repo}")
        return True
    
    return False

def cmd_add(args):
    """Add files to staging area"""
    if not os.path.exists('.vhub'):
        print_error("Not a vHub repository (or any of the parent directories)")
        return False
    
    staged_file = '.vhub/staged.json'
    staged = {}
    
    if os.path.exists(staged_file):
        with open(staged_file, 'r') as f:
            try:
                staged = json.load(f)
            except:
                staged = {}
    
    if args.files and args.files[0] == '.':
        files = []
        for ext in ['*.*', '*']:
            files.extend(glob.glob(ext))
        
        files = [f for f in files if not f.startswith('.vhub') and not f.startswith('.')]
    else:
        files = args.files
    
    if not files:
        print_error("No files specified")
        return False
    
    for file_path in files:
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                
                file_hash = hashlib.sha1(content.encode()).hexdigest()
                
                staged[file_path] = {
                    "hash": file_hash,
                    "content": content
                }
                
                print_info(f"Added {file_path}")
            except Exception as e:
                print_error(f"Failed to add {file_path}: {str(e)}")
        else:
            print_error(f"File {file_path} does not exist or is not a regular file")
    
    with open(staged_file, 'w') as f:
        json.dump(staged, f)
    
    return True

def cmd_status(args):
    """Show the working tree status"""
    if not os.path.exists('.vhub'):
        print_error("Not a vHub repository (or any of the parent directories)")
        return False
    
    staged_file = '.vhub/staged.json'
    staged = {}
    
    if os.path.exists(staged_file):
        with open(staged_file, 'r') as f:
            try:
                staged = json.load(f)
            except:
                staged = {}
    
    print_info("vHub Status")
    print_info("-----------")
    
    config = get_config()
    print_info(f"Repository: {config.get('repo_name')}")
    print_info(f"Base URL: {config.get('base_url')}")
    print_info(f"Implementation: {config.get('implementation')}")
    print_info("-----------")
    
    if staged:
        print_info("Changes to be committed:")
        for file_path in staged:
            print(f"  new file: {file_path}")
    else:
        print_info("No changes added to commit")
    
    return True

def cmd_commit(args):
    """Record changes to the repository"""
    if not os.path.exists('.vhub'):
        print_error("Not a vHub repository (or any of the parent directories)")
        return False
    
    staged_file = '.vhub/staged.json'
    
    if not os.path.exists(staged_file):
        print_error("No changes added to commit")
        return False
    
    with open(staged_file, 'r') as f:
        try:
            staged = json.load(f)
        except:
            print_error("No changes added to commit")
            return False
    
    if not staged:
        print_error("No changes added to commit")
        return False
    
    if not args.message:
        print_error("Aborting commit due to empty commit message")
        return False
    
    implementation = get_implementation()
    repo_name = get_repo_name()
    base_url = get_base_url()
    
    author = args.author or "Unknown <unknown@example.com>"
    
    parent_id = get_last_commit_id()
    
    timestamp = datetime.datetime.now().isoformat()
    
    data = {
        "repo_name": repo_name,
        "message": args.message,
        "author": author,
        "timestamp": timestamp,
        "files": staged,
        "parent_id": parent_id
    }
    
    data["id"] = generate_commit_id(data)
    
    response = requests.post(f"{base_url}/{implementation}/push", json=data)
    
    result = handle_response(response)
    if result:
        print_success(f"[{repo_name} {data['id'][:7]}] {args.message}")
        
        os.remove(staged_file)
        return True
    
    return False

def cmd_log(args):
    """Show commit logs"""
    if not os.path.exists('.vhub'):
        print_error("Not a vHub repository (or any of the parent directories)")
        return False
    
    implementation = get_implementation()
    repo_name = get_repo_name()
    base_url = get_base_url()
    
    response = requests.get(f"{base_url}/{implementation}/commits/{repo_name}")
    
    result = handle_response(response)
    if result:
        if not result:
            print_info("No commits yet")
            return True
        
        for commit in result:
            commit_id = commit.get('id', 'unknown')
            author = commit.get('author', 'Unknown')
            message = commit.get('message', 'No message')
            timestamp = commit.get('timestamp', '')
            
            print_info(f"commit {commit_id}")
            print(f"Author: {author}")
            print(f"Date:   {timestamp}")
            print()
            print(f"    {message}")
            print()
        
        return True
    
    return False

def cmd_clone(args):
    """Clone a repository"""
    if not args.source:
        print_error("Source repository name is required")
        return False
    
    implementation = args.implementation or get_implementation()
    target = args.target or args.source
    base_url = args.base_url or get_base_url()
    
    data = {
        "source_repo": args.source,
        "target_repo": target
    }
    
    response = requests.post(f"{base_url}/{implementation}/clone", json=data)
    
    result = handle_response(response)
    if result:
        print_success(f"Cloned repository '{args.source}' to '{target}'")
        
        if not os.path.exists(target):
            os.makedirs(target)
        
        os.chdir(target)
        
        config = {
            'repo_name': target,
            'implementation': implementation,
            'base_url': base_url
        }
        save_config(config)
        
        response = requests.get(f"{base_url}/{implementation}/commits/{target}")
        commits_result = handle_response(response)
        
        if commits_result and len(commits_result) > 0:
            all_files = {}
            
            for commit in reversed(commits_result):
                commit_id = commit['id']
                
                response = requests.get(f"{base_url}/{implementation}/commit/{target}/{commit_id}")
                commit_result = handle_response(response)
                
                if commit_result and 'files' in commit_result:
                    for file_path, file_data in commit_result['files'].items():
                        if 'content' in file_data:
                            all_files[file_path] = file_data['content']
            
            if all_files:
                for file_path, content in all_files.items():
                    file_dir = os.path.dirname(file_path)
                    if file_dir and not os.path.exists(file_dir):
                        os.makedirs(file_dir, exist_ok=True)
                    
                    with open(file_path, 'w') as f:
                        f.write(content)
                    print_info(f"Checked out: {file_path}")
                
                print_success(f"Checked out {len(all_files)} files from repository history")
            else:
                print_info("Repository is empty - no files to check out")
        else:
            print_info("Repository is empty - no commits found")
        
        return True
    
    return False

def cmd_show(args):
    """Show commit details"""
    if not os.path.exists('.vhub'):
        print_error("Not a vHub repository (or any of the parent directories)")
        return False
    
    implementation = get_implementation()
    repo_name = get_repo_name()
    base_url = get_base_url()
    
    commit_id = args.commit_id
    if not commit_id:
        commit_id = get_last_commit_id()
        if not commit_id:
            print_error("No commits found")
            return False
    
    response = requests.get(f"{base_url}/{implementation}/commit/{repo_name}/{commit_id}")
    
    result = handle_response(response)
    if result:
        commit_id = result.get('id', 'unknown')
        author = result.get('author', 'Unknown')
        message = result.get('message', 'No message')
        timestamp = result.get('timestamp', '')
        files = result.get('files', {})
        
        print_info(f"commit {commit_id}")
        print(f"Author: {author}")
        print(f"Date:   {timestamp}")
        print()
        print(f"    {message}")
        print()
        
        if files:
            print_info("Changes:")
            for file_path, file_data in files.items():
                print(f"  {file_path}")
                if args.show_content and 'content' in file_data:
                    print("---")
                    print(file_data['content'])
                    print("---")
        
        return True
    
    return False

def cmd_list_implementations(args):
    """List available implementations"""
    base_url = args.base_url or get_base_url()
    
    response = requests.get(f"{base_url}/implementation")
    
    result = handle_response(response)
    if result:
        print_info("Available implementations:")
        for impl in result:
            print(f"  {impl}")
        return True
    
    return False

def cmd_pull(args):
    """Pull changes from source repository to target repository"""
    if not os.path.exists('.vhub'):
        print_error("Not a vHub repository (or any of the parent directories)")
        return False
    
    implementation = get_implementation()
    target_repo = get_repo_name()
    source_repo = args.source
    base_url = get_base_url()
    
    if not source_repo:
        print_error("Source repository name is required")
        return False
    
    data = {
        "source_repo": source_repo,
        "target_repo": target_repo
    }
    
    response = requests.post(f"{base_url}/{implementation}/pull", json=data)
    
    result = handle_response(response)
    if result:
        print_success(f"Pulled changes from '{source_repo}' to '{target_repo}'")
        
        latest_commit_id = get_last_commit_id()
        if latest_commit_id:
            response = requests.get(f"{base_url}/{implementation}/commit/{target_repo}/{latest_commit_id}")
            commit_result = handle_response(response)
            
            if commit_result and 'files' in commit_result:
                for file_path, file_data in commit_result['files'].items():
                    file_dir = os.path.dirname(file_path)
                    if file_dir and not os.path.exists(file_dir):
                        os.makedirs(file_dir, exist_ok=True)

                    if 'content' in file_data:
                        with open(file_path, 'w') as f:
                            f.write(file_data['content'])
                        print_info(f"Updated: {file_path}")
                
                print_success(f"Checked out files from commit {latest_commit_id[:7]}")
        
        return True
    
    return False

def cmd_file_history(args):
    """Show history of changes to a file"""
    if not os.path.exists('.vhub'):
        print_error("Not a vHub repository (or any of the parent directories)")
        return False
    
    implementation = get_implementation()
    repo_name = get_repo_name()
    base_url = get_base_url()
    
    if not args.file_path:
        print_error("File path is required")
        return False
    
    response = requests.get(f"{base_url}/{implementation}/file_history/{repo_name}/{args.file_path}")
    
    result = handle_response(response)
    if result:
        if not result:
            print_info(f"No history found for {args.file_path}")
            return True
        
        print_info(f"History for {args.file_path}:")
        print()
        
        for entry in result:
            commit_id = entry.get('commit_id', 'unknown')
            commit_message = entry.get('commit_message', 'No message')
            author = entry.get('author', 'Unknown')
            timestamp = entry.get('timestamp', '')
            
            print_info(f"commit {commit_id}")
            print(f"Author: {author}")
            print(f"Date:   {timestamp}")
            print()
            print(f"    {commit_message}")
            
            if args.show_diff:
                if 'diff' in entry:
                    print()
                    print(entry['diff'])
            
            print()
        
        return True
    
    return False

def cmd_checkout(args):
    """Checkout a specific commit"""
    if not os.path.exists('.vhub'):
        print_error("Not a vHub repository (or any of the parent directories)")
        return False
    
    implementation = get_implementation()
    repo_name = get_repo_name()
    base_url = get_base_url()
    
    commit_id = args.commit_id
    if not commit_id:
        print_error("Commit ID is required")
        return False
    
    response = requests.get(f"{base_url}/{implementation}/check_commit/{repo_name}/{commit_id}")
    exists = handle_response(response)
    if not exists or exists.get('exists') is not True:
        print_error(f"Commit {commit_id} not found")
        return False
    
    response = requests.get(f"{base_url}/{implementation}/commit/{repo_name}/{commit_id}")
    result = handle_response(response)
    
    if result and 'files' in result:
        for file_path, file_data in result['files'].items():
            file_dir = os.path.dirname(file_path)
            if file_dir and not os.path.exists(file_dir):
                os.makedirs(file_dir, exist_ok=True)
            
            if 'content' in file_data:
                with open(file_path, 'w') as f:
                    f.write(file_data['content'])
                print_info(f"Checked out: {file_path}")
        
        print_success(f"Checked out files from commit {commit_id[:7]}")
        
        with open('.vhub/current_commit', 'w') as f:
            f.write(commit_id)
        
        return True
    
    return False

def cmd_delete_repo(args):
    """Delete a repository"""
    implementation = args.implementation or get_implementation()
    repo_name = args.repo_name
    base_url = args.base_url or get_base_url()
    
    if not repo_name:
        print_error("Repository name is required")
        return False
    
    if not args.force:
        confirm = input(f"Are you sure you want to delete repository '{repo_name}'? This cannot be undone. [y/N]: ")
        if confirm.lower() != 'y':
            print_info("Operation cancelled")
            return False
    
    response = requests.delete(f"{base_url}/{implementation}/delete_repo/{repo_name}")
    
    result = handle_response(response)
    if result:
        print_success(f"Repository '{repo_name}' deleted")
        return True
    
    return False

def main():
    parser = argparse.ArgumentParser(
        description='vHub - A Git-like version control system',
        usage='''vh <command> [<args>]

The vHub commands are:
   init       Initialize a new repository
   add        Add file contents to the staging area
   commit     Record changes to the repository
   status     Show the working tree status
   log        Show commit logs
   clone      Clone a repository
   show       Show commit details
   pull       Pull changes from another repository
   checkout   Checkout a specific commit
   history    Show file history
   repos      List all repositories
   delete     Delete a repository
   config     Configure repository settings
   implementations List available implementations
''')
    
    parser.add_argument('command', help='Command to run')
    
    args = parser.parse_args(sys.argv[1:2])
    
    if args.command == 'init':
        parser = argparse.ArgumentParser(description='Initialize a new repository')
        parser.add_argument('--name', '-n', help='Repository name')
        parser.add_argument('--implementation', '-i', help='Implementation to use')
        parser.add_argument('--base-url', '-u', help=f'Base API URL (default: {DEFAULT_BASE_URL})')
        
        args = parser.parse_args(sys.argv[2:])
        
        cmd_init(args)
    
    elif args.command == 'config':
        parser = argparse.ArgumentParser(description='Configure repository settings')
        parser.add_argument('--list', '-l', action='store_true', help='List current configuration')
        parser.add_argument('--base-url', '-u', help='Set base API URL')
        parser.add_argument('--implementation', '-i', help='Set implementation')
        parser.add_argument('--repo-name', '-n', help='Set repository name')
        parser.add_argument('--global', '-g', dest='global_config', action='store_true', 
                            help='Set configuration globally for all repositories')
        
        args = parser.parse_args(sys.argv[2:])
        
        cmd_config(args)
    
    elif args.command == 'add':
        parser = argparse.ArgumentParser(description='Add file contents to the staging area')
        parser.add_argument('files', nargs='+', help='Files to add')
        
        args = parser.parse_args(sys.argv[2:])
        
        cmd_add(args)
    
    elif args.command == 'commit':
        parser = argparse.ArgumentParser(description='Record changes to the repository')
        parser.add_argument('-m', '--message', required=True, help='Commit message')
        parser.add_argument('-a', '--author', help='Author information')
        
        args = parser.parse_args(sys.argv[2:])
        
        cmd_commit(args)
    
    elif args.command == 'status':
        parser = argparse.ArgumentParser(description='Show the working tree status')
        
        args = parser.parse_args(sys.argv[2:])
        
        cmd_status(args)
    
    elif args.command == 'log':
        parser = argparse.ArgumentParser(description='Show commit logs')
        
        args = parser.parse_args(sys.argv[2:])
        
        cmd_log(args)
    
    elif args.command == 'clone':
        parser = argparse.ArgumentParser(description='Clone a repository')
        parser.add_argument('source', help='Source repository name')
        parser.add_argument('target', nargs='?', help='Target repository name')
        parser.add_argument('--implementation', '-i', help='Implementation to use')
        parser.add_argument('--base-url', '-u', help=f'Base API URL (default: {DEFAULT_BASE_URL})')
        
        args = parser.parse_args(sys.argv[2:])
        
        cmd_clone(args)
    
    elif args.command == 'show':
        parser = argparse.ArgumentParser(description='Show commit details')
        parser.add_argument('commit_id', nargs='?', help='Commit ID')
        parser.add_argument('--content', '-c', dest='show_content', action='store_true', help='Show file content')
        
        args = parser.parse_args(sys.argv[2:])
        
        cmd_show(args)
    
    elif args.command == 'repos':
        parser = argparse.ArgumentParser(description='List all repositories')
        parser.add_argument('--implementation', '-i', help='Implementation to use')
        parser.add_argument('--base-url', '-u', help=f'Base API URL (default: {DEFAULT_BASE_URL})')
        
        args = parser.parse_args(sys.argv[2:])
        
        cmd_list_repos(args)
    
    elif args.command == 'implementations':
        parser = argparse.ArgumentParser(description='List available implementations')
        parser.add_argument('--base-url', '-u', help=f'Base API URL (default: {DEFAULT_BASE_URL})')
        
        args = parser.parse_args(sys.argv[2:])
        
        cmd_list_implementations(args)
    
    elif args.command == 'pull':
        parser = argparse.ArgumentParser(description='Pull changes from source repository')
        parser.add_argument('source', help='Source repository name')
        
        args = parser.parse_args(sys.argv[2:])
        
        cmd_pull(args)
    
    elif args.command == 'history':
        parser = argparse.ArgumentParser(description='Show file history')
        parser.add_argument('file_path', help='Path to file')
        parser.add_argument('--diff', '-d', dest='show_diff', action='store_true', help='Show diffs')
        
        args = parser.parse_args(sys.argv[2:])
        
        cmd_file_history(args)
    
    elif args.command == 'checkout':
        parser = argparse.ArgumentParser(description='Checkout a specific commit')
        parser.add_argument('commit_id', help='Commit ID')
        
        args = parser.parse_args(sys.argv[2:])
        
        cmd_checkout(args)
    
    elif args.command == 'delete':
        parser = argparse.ArgumentParser(description='Delete a repository')
        parser.add_argument('repo_name', help='Repository name')
        parser.add_argument('--implementation', '-i', help='Implementation to use')
        parser.add_argument('--base-url', '-u', help=f'Base API URL (default: {DEFAULT_BASE_URL})')
        parser.add_argument('--force', '-f', action='store_true', help='Force deletion without confirmation')
        
        args = parser.parse_args(sys.argv[2:])
        
        cmd_delete_repo(args)
    
    else:
        print_error(f"Unknown command: {args.command}")
        parser.print_help()
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())