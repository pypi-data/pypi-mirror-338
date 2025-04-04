#!/usr/bin/env python3

import os
import argparse
import subprocess
import re

class GitIgnoreParser:
    """Parser for .gitignore files that handles pattern matching"""
    
    def __init__(self):
        self.patterns = []
    
    def add_patterns_from_file(self, gitignore_path):
        """Read patterns from a .gitignore file"""
        if not os.path.isfile(gitignore_path):
            return
        
        try:
            with open(gitignore_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    # Skip empty lines and comments
                    if not line or line.startswith('#'):
                        continue
                        
                    # Skip overly broad patterns
                    if line == '*' or line == '**':
                        # print(f"DEBUG: Skipping overly broad pattern: {line}")
                        continue
                    
                    # Handle negation (!)
                    is_negation = line.startswith('!')
                    if is_negation:
                        line = line[1:]
                    
                    # print(f"DEBUG: Adding pattern from {os.path.basename(gitignore_path)}: {line}")
                    
                    # Convert .gitignore pattern to regex pattern
                    pattern = self._convert_pattern_to_regex(line)
                    self.patterns.append((pattern, is_negation))
        except Exception as e:
            print(f"Warning: Could not parse {gitignore_path}: {e}")
    
    def _convert_pattern_to_regex(self, pattern):
        """Convert a .gitignore pattern to a regex pattern"""
        # Handle directory-specific pattern
        if pattern.endswith('/'):
            pattern = pattern[:-1]
            dir_only = True
        else:
            dir_only = False
        
        # Handle patterns starting with /
        if pattern.startswith('/'):
            pattern = pattern[1:]  # Remove the leading /
            anchored = True
        else:
            anchored = False
        
        # Special case: if pattern is just a file extension
        if pattern.startswith('*.'):
            pattern = re.escape(pattern[2:]) + '$'
            return re.compile(pattern)
            
        # Escape special characters except * and ?
        pattern = re.escape(pattern)
        
        # Convert * and ** wildcards to regex
        pattern = pattern.replace('\\*\\*/', '(.*/)?')
        pattern = pattern.replace('\\*\\*', '.*')
        pattern = pattern.replace('\\*', '[^/]*')
        pattern = pattern.replace('\\?', '[^/]')
        
        # Build the final pattern
        if anchored:
            pattern = '^' + pattern  # Match only at the start
        else:
            # For non-anchored patterns, match either at the start or in subdirectories
            pattern = '^(.*/)?(' + pattern + ')'
        
        # Add suffix for directory-only patterns
        if dir_only:
            pattern = pattern + '(/.*)?$'
        else:
            pattern = pattern + '$'
        
        # print(f"DEBUG: Converted gitignore pattern to regex: {pattern}")
        return re.compile(pattern)
    
    def is_ignored(self, path, is_dir=False):
        """Check if a path is ignored according to the gitignore rules"""
        # Default is not ignored
        ignored = False
        
        # Normalize path for matching
        path = path.rstrip('/')
        
        # Don't ignore the root directory
        if path == '.' or path == '':
            return False
            
        for pattern, is_negation in self.patterns:
            matched = pattern.search(path) is not None
            if matched:
                # print(f"DEBUG: Pattern '{pattern.pattern}' matched path '{path}'")
                # Negation pattern overrides previous ignores
                if is_negation:
                    ignored = False
                else:
                    ignored = True
        
        return ignored

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Generate a visual tree structure of a Git repository")
    parser.add_argument("-d", "--depth", type=int, default=0, 
                        help="Set maximum directory depth (default: unlimited)")
    parser.add_argument("-i", "--ignore", action="append", default=[],
                        help="Ignore specified path pattern (can be used multiple times)")
    parser.add_argument("-a", "--all", action="store_true",
                        help="Show hidden files (starting with .)")
    parser.add_argument("-g", "--git-only", action="store_true",
                        help="Show only files tracked by Git")
    parser.add_argument("--respect-gitignore", action="store_true", default=True,
                        help="Respect .gitignore files (default: True)")
    parser.add_argument("--no-respect-gitignore", action="store_false", dest="respect_gitignore",
                        help="Don't respect .gitignore files")
    parser.add_argument("directory", nargs="?", default=".",
                        help="Target directory (default: current directory)")
    return parser.parse_args()

def is_git_repo(directory):
    """Check if the given directory is a Git repository."""
    try:
        result = subprocess.run(
            ["git", "-C", directory, "rev-parse", "--is-inside-work-tree"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip() == "true"
    except subprocess.CalledProcessError as e:
        print(f"Error: Not a Git repository or git command failed: {e}")
        return False

def get_git_tracked_files(directory):
    """Get all files tracked by Git in the given directory."""
    try:
        result = subprocess.run(
            ["git", "-C", directory, "ls-files", "--full-name"],
            capture_output=True, text=True, check=True
        )
        return {os.path.normpath(os.path.join(directory, file)) for file in result.stdout.splitlines()}
    except subprocess.CalledProcessError as e:
        print(f"Error: Not a Git repository or git command failed: {e}")
        return set()

def collect_gitignore_patterns(base_dir):
    """Collect .gitignore patterns from the repository"""
    parser = GitIgnoreParser()
    
    # First add the root .gitignore
    root_gitignore = os.path.join(base_dir, '.gitignore')
    if os.path.isfile(root_gitignore):
        # print(f"DEBUG: Reading patterns from {root_gitignore}")
        parser.add_patterns_from_file(root_gitignore)
    
    # Find all .gitignore files in the repository
    for root, dirs, files in os.walk(base_dir):
        # Skip .git directory
        if '.git' in dirs:
            dirs.remove('.git')
        
        if '.gitignore' in files and root != base_dir:  # Avoid adding root .gitignore twice
            gitignore_path = os.path.join(root, '.gitignore')
            # print(f"DEBUG: Reading patterns from {gitignore_path}")
            parser.add_patterns_from_file(gitignore_path)
    
    return parser

def should_ignore(path, base_dir, ignore_patterns, show_hidden, git_only, git_files, gitignore_parser=None):
    """Determine if a path should be ignored based on the given criteria."""
    # Make path relative to base_dir for consistent pattern matching
    abs_path = os.path.abspath(path)
    rel_path = os.path.relpath(abs_path, base_dir)
    
    # Always ignore the .git directory
    if rel_path == '.git' or rel_path.startswith('.git/') or rel_path.startswith('.git\\'):
        return True
    
    # Check user-defined ignore patterns
    for pattern in ignore_patterns:
        if pattern in rel_path:
            # print(f"DEBUG: Ignoring {rel_path} due to user pattern: {pattern}")
            return True
    
    # Skip hidden files unless --all is specified
    if not show_hidden and os.path.basename(rel_path).startswith('.'):
        # print(f"DEBUG: Ignoring hidden file/directory: {rel_path}")
        return True
    
    # Check if ignored by .gitignore
    if gitignore_parser is not None:
        normalized_path = rel_path.replace('\\', '/')
        is_dir = os.path.isdir(abs_path)
        if gitignore_parser.is_ignored(normalized_path, is_dir):
            # print(f"DEBUG: {rel_path} ignored by .gitignore rules")
            return True
    
    # If git-only mode is active, check if the file is tracked by Git
    if git_only and abs_path not in git_files and not os.path.isdir(abs_path):
        # print(f"DEBUG: {rel_path} not tracked by git")
        return True
    
    return False

def print_tree(directory, prefix="", depth=1, max_depth=0, ignore_patterns=None, 
               show_hidden=False, git_only=False, git_files=None, base_dir=None,
               gitignore_parser=None):
    """Print the directory tree recursively."""
    if ignore_patterns is None:
        ignore_patterns = []
    
    if base_dir is None:
        base_dir = directory
    
    # Check max depth
    if max_depth > 0 and depth > max_depth:
        return
    
    # Get entries in the directory
    try:
        entries = sorted(os.listdir(directory))
    except PermissionError:
        print(f"{prefix}├── Error: Permission denied")
        return
    except FileNotFoundError:
        print(f"{prefix}├── Error: Directory not found")
        return
    
    # Filter entries based on criteria
    filtered_entries = []
    for entry in entries:
        full_path = os.path.join(directory, entry)
        if not should_ignore(full_path, base_dir, ignore_patterns, show_hidden, git_only, git_files, gitignore_parser):
            filtered_entries.append(entry)
    
    # Process each entry
    count = len(filtered_entries)
    for idx, entry in enumerate(filtered_entries, 1):
        full_path = os.path.join(directory, entry)
        is_last = (idx == count)
        
        # Determine prefix characters
        if is_last:
            current_prefix = "└── "
            next_prefix = "    "
        else:
            current_prefix = "├── "
            next_prefix = "│   "
        
        # Print current entry
        print(f"{prefix}{current_prefix}{entry}")
        
        # Recursively process directories
        if os.path.isdir(full_path) and not os.path.islink(full_path):
            print_tree(
                full_path, 
                prefix + next_prefix, 
                depth + 1, 
                max_depth, 
                ignore_patterns, 
                show_hidden, 
                git_only, 
                git_files, 
                base_dir,
                gitignore_parser
            )

def main():
    """Main function."""
    args = parse_arguments()
    
    # Normalize and validate target directory
    target_dir = os.path.abspath(args.directory)
    if not os.path.isdir(target_dir):
        print(f"Error: Directory '{target_dir}' not found.")
        return 1
    
    # Check if git-only mode can be used
    if args.git_only and not is_git_repo(target_dir):
        print(f"Error: '{target_dir}' is not a Git repository.")
        return 1
    
    # Get repository name and print it
    repo_name = os.path.basename(target_dir)
    print(f"{repo_name}/")
    
    # Get Git tracked files if needed
    git_files = set()
    if args.git_only:
        git_files = get_git_tracked_files(target_dir)
    
    # Parse .gitignore files if needed
    gitignore_parser = None
    if args.respect_gitignore:
        gitignore_parser = collect_gitignore_patterns(target_dir)
    
    # Print the tree
    print_tree(
        target_dir, 
        "", 
        1, 
        args.depth, 
        args.ignore, 
        args.all, 
        args.git_only, 
        git_files, 
        target_dir,
        gitignore_parser
    )
    
    return 0

if __name__ == "__main__":
    exit(main())