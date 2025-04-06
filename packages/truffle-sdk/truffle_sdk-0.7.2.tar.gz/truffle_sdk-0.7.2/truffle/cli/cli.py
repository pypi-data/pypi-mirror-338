import os 
import sys
import argparse
import getpass
import json 
import requests
import uuid
from typing import Optional
try:
    import logging
    requests_log = logging.getLogger("urllib3.connectionpool")
    requests_log.setLevel(logging.WARNING)
    requests_log.propagate = False
except Exception as e:
    pass 

from  pathlib import Path
from truffle.common import get_logger
from ..utils.logger import log
from ..utils.help import HelpMenu
from ..utils.formatter import Formatter

logger = get_logger()

def get_png_dimensions(file_path):
    with open(file_path, "rb") as f:
        signature = f.read(8)  
        if signature != b"\x89PNG\r\n\x1a\n":
            raise ValueError("Not a valid PNG file: " + file_path)
        f.read(4) 
        if f.read(4) != b"IHDR":
            raise ValueError("Invalid PNG structure: header not found in " + file_path)

        width = int.from_bytes(f.read(4), "big")
        height = int.from_bytes(f.read(4), "big")
        return width, height

def default_mainpy(proj_name : str) -> str:
    return str(r"""import truffle
import requests
from typing import List, Dict, Any
class PROJECT_NAME:
    def __init__(self):
        self.client = truffle.TruffleClient() # the client for using the SDK API, will be a global in next release
                                            # this allows you to perform LLM inference, text embeddings, ask the user for input, etc.
        self.notepad = "" # you can store state in your class, and it will be saved between tool calls and by the backend to reload saved tasks
    @truffle.tool(
        description="Replace this with a description of the tool.",
        icon="brain" # these are Apple SF Symbols, will be fontawesome icon names in next release, https://fontawesome.com/search?o=r&ic=free&ip=classic
    )
    @truffle.args(user_input="A description of the argument") #you can add descriptions to your arguments to help the model!
    def PROJECT_NAMETool(self, user_input: str) -> Dict[string, string]: # You have to type annotate all arguments and the return type
        def do_something(user_input):
            pass
        do_something(user_input) # you can do whatever you want in your tools, just make sure to return a value!
                                # add any imports you need at the top of the file and to the requirements.txt and they will be automatically installed
        return { "response" : "Hello, world!" }# all tools must return a value, and take at least one argument

    @truffle.tool("Adds two numbers together", icon="plus-minus")
    def Calculate(self, a: int, b: int) -> List[int]:
        return [a, b, a + b] 
    
    @truffle.tool("Returns a joke", icon="face-smile")
    def GetJoke(self, num_jokes : int) -> str:
        num_jokes = 1 if num_jokes < 1 else num_jokes # support for constraints on arguments is coming soon! 
        response = requests.get(f"https://v2.jokeapi.dev/joke/Programming,Misc?format=txt&amount={num_jokes}")
        if response.status_code != 200:
            print("JokeAPI returned an error: ", response.status_code) # any logs from your app are forwarded to the client
            raise ValueError("JokeAPI is down, try again later")   # any exceptions you raise are sent to the model automatically as well
        return response.content
    
    
    # an example of tools using state! you might want to use this to store things like API keys, or user preferences
    @truffle.tool("Take notes", icon="pencil")
    def TakeNote(self, note: str) -> str:
        self.notepad += note + "\n"
        return "Added note.\n Current notes: \n" + str(self.notepad)

    @truffle.tool("Read notes", icon="glasses")
    @truffle.args(clear_after="whether to clear notes after reading.")
    def ReadNotes(self, clear_after: bool) -> str:
        notes = self.notepad
        if clear_after is True:
            self.notepad = ""
        return "Current notes: \n" + str(notes)
        
    @truffle.tool("Searches with Perplexity", icon="magnifying-glass")
    @truffle.args(query="The search query")
    def PerplexitySearch(self, query: str) -> str:    
        self.client.tool_update("Searching perplexity...") # send an update to the client, will be displayed in the UI if version supports it
        return self.client.perplexity_search(query=query, model="sonar-pro") # SDK API provides free access to Perplexity
    
    # you can add as many tools as you want to your app, just make sure they are all in the same class, and have the @truffle.tool decorator
    # of course, you may also add any other methods you want to your class, they will not be exposed to the model but can be used in your tools
    # any files in your project directory will be included in the bundle, so you can use them in your tools as well, use relative paths from main.py
        

if __name__ == "__main__":
    truffle.run(PROJECT_NAME())
""").replace("PROJECT_NAME", proj_name)

def get_user_id():
    user_id_path = (
        f"/Users/{getpass.getuser()}/Library/Containers/com.deepshard.TruffleOS/Data/Library/Application Support/TruffleOS/magic-number.txt"
    )
    if not os.path.exists(user_id_path):
        print("No user ID found - please download and login to the Truffle client first")
        sys.exit(1)
    with open(user_id_path, "r") as f:
        user_id = f.read().strip()
    return user_id

def upload():
    try:
        # Get project name from manifest in current directory
        manifest_path = Path(".") / "manifest.json"
        if not manifest_path.exists():
            log.error("Not in a project directory")
            sys.exit(1)
        
        try:
            manifest = json.loads(manifest_path.read_text())
            project_name = manifest.get('name')
            if not project_name:
                log.error("Project name not found in manifest.json")
                sys.exit(1)
        except json.JSONDecodeError:
            log.error("Invalid manifest.json format")
            sys.exit(1)
        except Exception as e:
            log.error(f"Error reading manifest.json: {e}")
            sys.exit(1)

        # Look for .truffle file in current directory
        bundle_path = Path(".") / f"{project_name}.truffle"
        
        if not bundle_path.exists():
            log.error(f"{project_name}.truffle not found in current directory")
            log.detail("Run 'truffle build' first to create the build file")
            sys.exit(1)
        
        log.main(f"Uploading {project_name}")

        URL = "https://overcast.itsalltruffles.com:2087"
        user_id = get_user_id()
        
        try:
            params = {"user": user_id}
            response = requests.post(
                URL, params=params, data=bundle_path.read_bytes(), verify=False
            )
            if response.status_code == 200:
                log.success("***********")
                log.success("Upload successful - check your client for installation errors and confirmation")
                log.success("***********")
                sys.exit(0)
            else:
                log.error(f"Upload failed with status code {response.status_code}")
                sys.exit(1)
        except FileNotFoundError:
            log.error(f"File not found: {bundle_path}")
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            log.error(f"Upload failed: {e}")
            sys.exit(1)
        except Exception as e:
            log.error(f"Upload failed: unknown error: {e}")
            sys.exit(1)
    except Exception as e:
        log.error(f"Unexpected error: {e}")
        sys.exit(1)

def build():
    builddir = Path(".")
    if not builddir.exists():
        log.error(f"Path {builddir} does not exist - cannot build")
        sys.exit(1)
    if not builddir.is_dir():
        log.error("Path is not a directory, please provide a directory to build")
        sys.exit(1)

    def check_file(p : Path):
        name = p.name
        if name == "manifest.json":
            manifest = json.loads(p.read_text())
            required_keys = [
                'name', 'description', 'app_bundle_id', 'manifest_version'
            ]
            for key in required_keys:
                if key not in manifest:
                    log.error(f"Missing key {key} in manifest.json")
                    sys.exit(1)
            if 'developer_id' not in manifest:
                manifest['developer_id'] = get_user_id()
                with open(p, 'w') as f:
                    json.dump(manifest, f, indent=2)
            return manifest['name']  # Return project name from manifest
        elif name == "requirements.txt":
            reqs = p.read_text().strip().split("\n")
            banned_reqs = ["truffle", "grpcio", "protobuf"]
            for r in reqs:
                if not r: continue  # Skip empty lines
                for banned in banned_reqs:
                    if r.find(banned) != -1:
                        log.error(f"Do not include {banned} in requirements.txt")
                        sys.exit(1)
        elif name == "main.py":
            main_text = p.read_text()
            if main_text.find("import truffle") == -1:
                log.error("Missing import truffle in main.py")
                sys.exit(1)
            if main_text.find("truffle.run") == -1:
                log.error("Missing truffle.run call in main.py")
                sys.exit(1)
            if main_text.find("class") == -1:
                log.error("Missing class definition in main.py")
                sys.exit(1)

    def must_exist(p : Path):
        if not p.exists() or not p.is_file():
            log.error(f"Missing file: {p} - invalid project")
            sys.exit(1)
        return check_file(p)

    project_name = None
    for f in APP_FILES:
        result = must_exist(builddir / f)
        if f == "manifest.json":
            project_name = result

    for file in builddir.iterdir():
        try:
            if file.is_file():
                size = file.stat().st_size
                if size > (1024 * 1024 * 10): 
                    log.warning(f"Unexpectedly large file {file}, did you mean to include this?")
                    sys.exit(1)
        except Exception as e:
            continue
    
    def make_zip(src_dir : Path, dst_file : Path):
        if not src_dir.exists() or not src_dir.is_dir():
            log.error(f"Invalid source directory: {src_dir}")
            sys.exit(1)
        if os.system(f'zip -r {dst_file} {src_dir} -x "*.DS_Store" {str(src_dir) + "/*.truffle"}') != 0:
            log.warning("zip returned non-zero exit code! build may have failed")
        return dst_file

    bundle = make_zip(builddir, builddir / f"{project_name}.truffle")
    log.success(f"Built project {project_name} to {bundle}")
    log.detail(f"upload with 'truffle upload'")
    sys.exit(0)

APP_FILES = [
    "manifest.json",
    "requirements.txt",
    "main.py",
    "icon.png",
]

def init_project(name: Optional[str] = None, description: Optional[str] = None):
    try:
        # Display the Truffle banner
        fmt = Formatter()
        print(fmt.truffle_banner())
        
        # Get desktop path
        path = get_desktop_path()
        log.detail(f"Using desktop path: {path}")
        
        # Get and process project name
        if name is None:
            log.prompt("Project name", end="")
            name = input()
        else:
            log.detail(f"Using provided name: {name}")
            
        # Process name - replace spaces with hyphens
        name = name.strip().replace(" ", "-")
        
        # Validate project name
        if not name or not name.replace('-', '').replace('_', '').isalnum():
            log.error("Invalid project name")
            log.detail("Project name must contain only letters, numbers, hyphens, and underscores")
            sys.exit(1)
        
        # Get project description
        if description is None:
            log.prompt("Description", end="")
            description = input()
        else:
            log.detail(f"Using provided description: {description}")
        
        # Create project directory
        project_dir = Path(path) / name
        if project_dir.exists():
            log.error("Project creation failed")
            log.detail(f"Directory already exists: {project_dir}")
            sys.exit(1)
        
        try:
            project_dir.mkdir(parents=True)
            log.created_file(str(project_dir))
        except Exception as e:
            log.error("Project creation failed")
            log.detail(f"Could not create directory: {e}")
            sys.exit(1)
        
        # Create manifest.json
        manifest = {
            "name": name,
            "description": description,
            "app_bundle_id": f"com.truffle.{name}",
            "manifest_version": "1.0",
            "example_prompts": []
        }
        
        try:
            manifest_path = project_dir / "manifest.json"
            manifest_path.write_text(json.dumps(manifest, indent=2))
            log.created_file("manifest.json")
        except Exception as e:
            log.error("Project creation failed")
            log.detail(f"Could not create manifest.json: {e}")
            sys.exit(1)
        
        # Create requirements.txt
        try:
            reqs_path = project_dir / "requirements.txt"
            reqs_path.write_text("")
            log.created_file("requirements.txt")
        except Exception as e:
            log.error("Project creation failed")
            log.detail(f"Could not create requirements.txt: {e}")
            sys.exit(1)
        
        # Create main.py
        try:
            main_path = project_dir / "main.py"
            main_path.write_text(default_mainpy(name))
            log.created_file("main.py")
        except Exception as e:
            log.error("Project creation failed")
            log.detail(f"Could not create main.py: {e}")
            sys.exit(1)
        
        # Create icon.png placeholder
        try:
            icon_path = project_dir / "icon.png"
            icon_path.touch()  # Just create an empty file
            log.created_file("icon.png")
        except Exception as e:
            log.error("Project creation failed")
            log.detail(f"Could not create icon.png: {e}")
            sys.exit(1)
        
        log.success("Project initialized successfully")
        log.detail(f"Run 'cd {project_dir}' to start working")
        log.detail("Run 'truffle build' when ready to build your project")
    except Exception as e:
        log.error("Unexpected error")
        log.detail(str(e))
        sys.exit(1)

def get_desktop_path():
    """Get the path to the user's desktop directory."""
    if sys.platform == "darwin":  # macOS
        return os.path.expanduser("~/Desktop")
    elif sys.platform == "win32":  # Windows
        return os.path.join(os.path.expanduser("~"), "Desktop")
    elif sys.platform == "linux":  # Linux
        return os.path.join(os.path.expanduser("~"), "Desktop")
    else:
        # Fallback to current directory if platform is unknown
        logger.warning(f"Unknown platform {sys.platform}, using current directory as fallback")
        return os.getcwd()

def cli():
    parser = argparse.ArgumentParser(prog="truffle", description="Truffle SDK CLI", add_help=False)
    subparsers = parser.add_subparsers(dest="action", description="the CLI action: upload / init / or build", help="The action to perform")
    
    def add_subcommand(name : str, help : str):
        p = subparsers.add_parser(name, help=help, add_help=False)
        if name == "init":
            # Add name as positional argument that can contain multiple words, but make it optional
            p.add_argument("name", nargs="*", help="Name of your app (spaces will be converted to hyphens)")
            p.add_argument("-d", "--description", help="Description of what your app does")
        # Add help argument to each subparser
        p.add_argument("-h", "--help", action="store_true", help="Show help message")
    
    actions = {
         "upload" : {"help": "Upload the project to the cloud", "fn": upload} ,
         "init" : {"help": "Initialize a new project", "fn": init_project},
         "build" : {"help": "Build the project in current directory", "fn": build},
    }

    for name, args in actions.items():
        add_subcommand(name, args["help"])

    # Add help argument to main parser
    parser.add_argument("-h", "--help", action="store_true", help="Show help message")

    args = parser.parse_args()
    
    # Show help menu if --help is used or no action specified
    if args.help or not args.action:
        help_menu = HelpMenu()
        help_menu.show_help()
        sys.exit(0)
    
    cmd = actions[args.action]
    if args.action == "init":
        # Join multiple words with spaces before passing to init_project
        name = " ".join(args.name) if args.name else None
        cmd["fn"](name, args.description)
    else:
        cmd["fn"]()

def main():
    cli()

if __name__ == "__main__":
    main()

