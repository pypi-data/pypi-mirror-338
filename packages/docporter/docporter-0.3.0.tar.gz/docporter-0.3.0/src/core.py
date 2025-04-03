import os
import shutil
from git import Repo
from pathlib import Path
from urllib.parse import urlparse
import pyperclip
import fnmatch # For pattern matching

def is_github_url(source):
    """Check if the source is a GitHub URL."""
    try:
        result = urlparse(source)
        # Check for standard http/https/git/ssh schemes
        is_standard_url = all([
            result.scheme in ['http', 'https', 'git', 'ssh'],
            'github.com' in result.netloc
        ])
        # Check for scp-like syntax (e.g., git@github.com:user/repo.git)
        is_scp_like = '@' in source and 'github.com:' in source and not source.startswith(('http', 'ssh', 'git'))

        return is_standard_url or is_scp_like
    except Exception: # Catch potential parsing errors (e.g., invalid URL format)
        return False

def extract_repo_name(source):
    """Extract the repository name from GitHub URL or local path."""
    if is_github_url(source):
        # Handle standard URLs and scp-like syntax
        if '@' in source and ':' in source and not source.startswith(('http', 'ssh', 'git')):
             # Handle scp-like syntax: git@github.com:user/repo.git -> user/repo.git
             path_part = source.split(':')[-1]
        else:
             # Handle http, https, ssh, git schemes
             path_part = urlparse(source).path
        # Clean up path part: remove leading slash and .git suffix
        path_part = path_part.lstrip('/')
        return path_part.split('/')[-1].replace(".git", "")
    # Handle local path
    return Path(source).name

def validate_local_path(path):
    """Validate that the local path exists, is a directory, and is readable."""
    path = Path(path)
    if not path.exists():
        raise ValueError(f"Local path does not exist: {path}")
    if not path.is_dir():
        raise ValueError(f"Local path is not a directory: {path}")
    if not os.access(path, os.R_OK):
        raise ValueError(f"No read permission for local path: {path}")
    return path

def clone_repo(repo_url, destination_folder):
    """Clone the GitHub repository to the specified destination folder."""
    try:
        # Ensure the destination doesn't already exist or is empty
        dest_path = Path(destination_folder)
        if dest_path.exists():
             print(f"Warning: Destination folder '{destination_folder}' already exists. Removing it before cloning.")
             # Add error handling for removal in case of permission issues
             try:
                 shutil.rmtree(dest_path)
             except OSError as e:
                 print(f"Error removing existing directory '{destination_folder}': {e}. Please check permissions.")
                 exit(1)

        print(f"Cloning '{repo_url}'...")
        Repo.clone_from(repo_url, destination_folder, depth=1)
        print(f"Successfully cloned to '{destination_folder}'")
    except Exception as e:
        # Catch GitCommandError specifically if possible, or general Exception
        print(f"Error during git clone: {e}")
        exit(1)


def filter_documentation_files(repo_path, include_patterns=None, exclude_patterns=None, is_copy_operation=False):
    """
    Filter files in the repository or local folder. 
    For extract operations: Includes default doc types and specified include patterns, unless excluded.
    For copy operations: When include patterns are specified, ONLY includes files matching those patterns.
    Performs case-insensitive pattern matching.
    """
    # Default document types/names always considered for inclusion
    doc_extensions = {".md", ".mdx", ".rst", ".txt"}
    readme_prefix = "readme"

    doc_files = []
    repo_root = Path(repo_path).resolve()

    # Pre-lowercase patterns for efficient case-insensitive matching
    lc_include_patterns = [p.lower() for p in include_patterns] if include_patterns else None
    lc_exclude_patterns = [p.lower() for p in exclude_patterns] if exclude_patterns else None

    # Optional: Add debug prints to see what's being processed
    # print(f"DEBUG: Filtering in root: {repo_root}")
    # print(f"DEBUG: Lowercase Include patterns: {lc_include_patterns}")
    # print(f"DEBUG: Lowercase Exclude patterns: {lc_exclude_patterns}")

    for root, _, files in os.walk(repo_root):
        current_dir = Path(root).resolve()
        for file in files:
            full_path = current_dir / file
            # Check if it's actually a file (os.walk can yield directories sometimes, though less common in 'files')
            if not full_path.is_file():
                continue

            try:
                # Use normalized paths (forward slashes) for consistent matching across OS
                relative_path = str(full_path.relative_to(repo_root)).replace("\\", "/")
            except ValueError:
                # This can happen if symlinks point outside the repo root during walk
                print(f"Warning: Could not determine relative path for {full_path} within {repo_root}. Skipping.")
                continue

            filename_lower = file.lower()
            relative_path_lower = relative_path.lower() # Lowercase for matching

            # print(f"DEBUG: Checking file: {relative_path} (lowercase: {relative_path_lower})") # Debug

            # 1. Check Exclusions first (case-insensitive)
            is_excluded = False
            # Always exclude .git folders/files
            if '.git' in relative_path_lower:
                is_excluded = True
            elif lc_exclude_patterns:
                for pattern in lc_exclude_patterns:
                    # Check pattern against lowercased relative path and filename
                    if fnmatch.fnmatch(relative_path_lower, pattern) or fnmatch.fnmatch(filename_lower, pattern):
                        # print(f"DEBUG:   Excluded by pattern: {pattern}") # Debug
                        is_excluded = True
                        break
            if is_excluded:
                continue

            # 2. Determine if the file should be included
            should_include = False

            if is_copy_operation and lc_include_patterns:
                # For copy operations with include patterns, ONLY match those patterns
                for pattern in lc_include_patterns:
                    if fnmatch.fnmatch(relative_path_lower, pattern) or fnmatch.fnmatch(filename_lower, pattern):
                        should_include = True
                        break
            else:
                # For extract operations OR copy operations without include patterns
                # Check default doc types first
                is_default_doc = (
                    filename_lower.startswith(readme_prefix) or
                    full_path.suffix.lower() in doc_extensions
                )
                if is_default_doc:
                    should_include = True
                
                # Then check include patterns if they exist
                if not should_include and lc_include_patterns:
                    for pattern in lc_include_patterns:
                        if fnmatch.fnmatch(relative_path_lower, pattern) or fnmatch.fnmatch(filename_lower, pattern):
                            should_include = True
                            break

            # 3. Add the file if it passed exclusion and inclusion checks
            if should_include:
                # print(f"DEBUG:   ADDING file: {str(full_path)}") # Debug
                doc_files.append(str(full_path))
            # else:
                # print("DEBUG:   Skipping (not excluded, but failed inclusion checks)") # Debug

    # print(f"DEBUG: Found {len(doc_files)} files after filtering.") # Debug
    return doc_files


def copy_files(files, output_folder, repo_root):
    """Copy filtered documentation files to the output folder, preserving directory structure."""
    output_path = Path(output_folder)
    # Ensure repo_root is an absolute Path object for reliable relative path calculation
    repo_root_path = Path(repo_root).resolve()
    output_path.mkdir(parents=True, exist_ok=True) # Ensure output folder exists

    if not files:
        print("No files matched the criteria to copy.")
        return

    print(f"\nCopying {len(files)} files to {output_path}...")
    copied_count = 0
    error_count = 0
    for file in files:
        file_path = Path(file)
        try:
             # Calculate relative path correctly from the repo root provided
            relative_path = file_path.relative_to(repo_root_path)
        except ValueError:
             # This might happen if 'file' is somehow outside 'repo_root_path'
             print(f"Warning: Could not determine relative path for {file} based on root {repo_root_path}. Skipping copy.")
             error_count += 1
             continue

        dest_file_path = output_path / relative_path
        dest_dir = dest_file_path.parent

        try:
            dest_dir.mkdir(parents=True, exist_ok=True) # Ensure target directory exists
            shutil.copy2(file_path, dest_file_path) # copy2 preserves metadata
            # print(f"Copied: {relative_path}") # Verbose output
            copied_count += 1
        except Exception as e:
            print(f"Error copying file {relative_path}: {e}")
            error_count += 1

    print(f"Finished copying: {copied_count} files succeeded, {error_count} errors.")


def delete_repo(repo_folder):
    """Delete the temporary cloned repository folder."""
    try:
        repo_folder_path = Path(repo_folder)
        if repo_folder_path.exists() and repo_folder_path.is_dir(): # Extra safety check
            print(f"Deleting temporary repository folder: {repo_folder}")
            shutil.rmtree(repo_folder_path)
            print(f"Successfully deleted {repo_folder}")
        else:
             # Avoid printing error if it was never created or already deleted
             # print(f"Temporary repository folder not found or not a directory: {repo_folder}")
             pass
    except Exception as e:
        # Log error but don't halt execution if cleanup fails
        print(f"Error deleting temporary repository folder {repo_folder}: {e}")


def extract_docs(source, output_folder=None, include_patterns=None, exclude_patterns=None):
    """Main function to extract documentation files from GitHub repository or local folder."""
    try:
        repo_name = extract_repo_name(source)
    except Exception as e:
        print(f"Error extracting repository name from source '{source}': {e}")
        exit(1)

    if not output_folder:
        output_folder = f"{repo_name}-docs"
    # Resolve output path early to make it absolute and create it
    output_path = Path(output_folder).resolve()
    try:
        output_path.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"Error creating output directory '{output_path}': {e}")
        exit(1)
    output_folder = str(output_path) # Use string representation later

    is_git = is_github_url(source)
    # Define temp_clone_dir name more robustly, based on current working directory
    temp_clone_dir = str(Path.cwd() / f"{repo_name}_temp_clone_docporter")

    repo_root = None # Initialize repo_root
    cloned = False # Flag to track if cloning occurred for cleanup

    try:
        if is_git:
            clone_repo(source, temp_clone_dir)
            repo_root = temp_clone_dir # repo_root is the path to the temp clone
            cloned = True
        else:
            local_path = validate_local_path(source) # Validation happens here
            repo_root = str(local_path.resolve()) # repo_root is the user-provided path
            print(f"Using local folder: {repo_root}")

        # Ensure repo_root is set before proceeding
        if not repo_root:
             # This should theoretically not be reached if validation/cloning works
             print("Error: Repository root path could not be determined.")
             exit(1)

        # Filter documentation files using the updated function
        print("\nFiltering files...")
        doc_files = filter_documentation_files(repo_root, include_patterns, exclude_patterns)

        # Copy documentation files to the output folder
        copy_files(doc_files, output_folder, repo_root) # Pass correct repo_root

        print(f"\nDocumentation extraction completed. Files saved to: {output_folder}")

    except (ValueError, OSError) as e: # Catch validation/filesystem errors
        print(f"Error: {e}")
        exit(1)
    except Exception as e: # Catch unexpected errors
         print(f"An unexpected error occurred: {e}")
         exit(1)
    finally:
        # Clean up only if cloning actually happened
        if cloned and Path(temp_clone_dir).exists():
            delete_repo(temp_clone_dir)


def copy_llm_format(source, include_patterns=None, exclude_patterns=None):
    """Copy documentation in LLM ingestible format to clipboard."""
    try:
        repo_name = extract_repo_name(source)
    except Exception as e:
        print(f"Error extracting repository name from source '{source}': {e}")
        exit(1)

    is_git = is_github_url(source)
    # Define temp_clone_dir name
    temp_clone_dir = str(Path.cwd() / f"{repo_name}_temp_clone_docporter_llm")
    llm_format = ""
    repo_root = None
    cloned = False # Flag for cleanup

    try:
        if is_git:
            clone_repo(source, temp_clone_dir)
            repo_root = temp_clone_dir
            cloned = True
        else:
            local_path = validate_local_path(source)
            repo_root = str(local_path.resolve())
            print(f"Using local folder: {repo_root}")

        if not repo_root:
             print("Error: Repository root path could not be determined.")
             exit(1)

        # Filter documentation files
        print("\nFiltering files...")
        doc_files = filter_documentation_files(repo_root, include_patterns, exclude_patterns, is_copy_operation=True)

        if not doc_files:
             print("\nNo files matched the specified criteria. Nothing to copy.")
             # Ensure cleanup happens even if no files found
             if cloned and Path(temp_clone_dir).exists():
                 delete_repo(temp_clone_dir)
             return # Exit early

        # Format documentation files
        print(f"\nFormatting {len(doc_files)} files for LLM...")
        # Print filenames in format expected by tests
        for f in doc_files:
            print(f"Processing: {Path(f).name}")
        llm_format_parts = ["<documents>"]
        repo_root_path = Path(repo_root).resolve() # Ensure it's a Path object and absolute
        read_error_count = 0

        for i, file in enumerate(doc_files):
             file_path = Path(file).resolve() # Resolve to handle potential relative paths from filter step
             relative_path_str = "UNKNOWN_PATH" # Default
             try:
                  # Ensure the file path is actually within the repo_root before making relative
                 if not file_path.is_relative_to(repo_root_path):
                     print(f"Warning: File {file_path} is outside the expected root {repo_root_path}. Skipping.")
                     read_error_count += 1
                     continue
                 # Use posix path (forward slashes) for the source tag, more standard
                 relative_path_str = file_path.relative_to(repo_root_path).as_posix()
             except ValueError as e:
                 print(f"Error calculating relative path for {file_path} against root {repo_root_path}: {e}. Skipping.")
                 read_error_count += 1
                 continue

             try:
                content = ""
                # Try reading with UTF-8 first, fallback to latin-1 if it fails
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                except UnicodeDecodeError:
                     # print(f"Warning: Could not read {relative_path_str} as UTF-8, trying latin-1.")
                     try:
                         with open(file_path, "r", encoding="latin-1") as f:
                             content = f.read()
                     except Exception as read_e:
                          print(f"Error reading file {relative_path_str} even with latin-1: {read_e}")
                          read_error_count += 1
                          continue # Skip this file
                except OSError as read_e:
                     print(f"Error opening/reading file {relative_path_str}: {read_e}")
                     read_error_count += 1
                     continue # Skip this file


                llm_format_parts.append(f'<document index="{i+1}">')
                llm_format_parts.append(f'<source>{relative_path_str}</source>')
                llm_format_parts.append('<document_content>')
                # Basic XML escaping for content (&, <, >)
                content = content.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                llm_format_parts.append(content)
                llm_format_parts.append('</document_content>')
                llm_format_parts.append('</document>')

             except Exception as proc_e: # Catch errors during formatting/appending
                print(f"Error processing file content for {relative_path_str}: {proc_e}")
                read_error_count += 1
                continue # Skip problematic files

        llm_format_parts.append("</documents>")
        llm_format = "\n".join(llm_format_parts)

        if read_error_count > 0:
            print(f"Warning: Encountered errors reading {read_error_count} files.")

        # Copy to clipboard
        try:
            pyperclip.copy(llm_format)
            print(f"\nCopied LLM format ({len(doc_files) - read_error_count} documents processed) to clipboard.")
        except pyperclip.PyperclipException as e:
            # Handle cases where clipboard is not available (e.g., servers, headless environments)
            print(f"\nWarning: Could not copy to clipboard: {e}")
            print("LLM Formatted Text will be printed below (first 3000 chars):\n---")
            print(llm_format[:3000] + ("..." if len(llm_format) > 3000 else ""))
            print("---")
        except Exception as e:
            # Catch other potential errors during the copy operation
            print(f"\nError during clipboard operation: {e}")

    except (ValueError, OSError) as e: # Catch validation/filesystem errors
        print(f"Error: {e}")
        exit(1)
    except Exception as e: # Catch unexpected errors
         print(f"An unexpected error occurred: {e}")
         exit(1)
    finally:
        # Clean up only if cloning actually happened
        if cloned and Path(temp_clone_dir).exists():
            delete_repo(temp_clone_dir)
