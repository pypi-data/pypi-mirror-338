import asyncio
import websockets
import json
import aiohttp
from typing import Dict, Any
from dataclasses import dataclass, asdict
import logging
from datetime import datetime
import os
import sys

API_URL = "wss://run.pyboxs.com/kaiobuu"

# Define paths within user's home directory
BASE_DIR = os.path.expanduser("~/.kagent-cli")
OUTS_DIR = os.path.join(BASE_DIR, "outs")
TEMP_DIR = os.path.join(BASE_DIR, "temp")
CONFIG_FILE = os.path.join(BASE_DIR, "config")
WORKSPACE_DIR = os.path.join(BASE_DIR, "workspace")

# Create directories if they don't exist
os.makedirs(OUTS_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(WORKSPACE_DIR, exist_ok=True)

# Configure logging
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_filename = os.path.join(LOG_DIR, f"kaiocli_{timestamp}.log")
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)

# Console colors
class Colors:
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

@dataclass
class ClientRequest:
    request_id: str
    data: Dict[str, Any]

@dataclass
class ClientResponse:
    request_id: str
    error: bool
    data: Dict[str, Any]

class KaioAgentSession:
    def __init__(self, url: str):
        self.url = url
        self.session_id = None
        self.websocket = None
        self.pending_requests: Dict[str, asyncio.Future] = {}

    async def connect(self):
        self.websocket = await websockets.connect(f"{self.url}/session")
        handshake = await self.websocket.recv()
        self.session_id = json.loads(handshake)["session_id"]
        self.save_session_id()
        logging.info(f"Connected. Session ID: {self.session_id}")
        print(f"\n{Colors.YELLOW}{self.session_id}{Colors.ENDC}")

    def save_session_id(self):
        with open(CONFIG_FILE, 'w') as f:
            f.write(self.session_id)

    @staticmethod
    def load_session_id():
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                return f.read().strip()
        return None

    async def process_messages(self):
        while True:
            try:
                message = await self.websocket.recv()
                request = json.loads(message)
                response = await self.handle_request(request)
                await self.websocket.send(json.dumps(asdict(response)))
            except websockets.exceptions.ConnectionClosed:
                break

    async def handle_request(self, request: Dict[str, Any]) -> ClientResponse:
        client_request = ClientRequest(**request)
        action = client_request.data['action']
        if action == 'command':
            result = await self.execute_command(client_request.data['command'])
        elif action == 'read':
            result = await self.read_file(client_request.data['path'])
        elif action == 'write':
            result = await self.write_file(client_request.data['path'], client_request.data['content'])
        else:
            result = {"error": "Unknown action"}

        return ClientResponse(
            request_id=client_request.request_id,
            error="error" in result,
            data=result
        )

    async def execute_command(self, command: str) -> Dict[str, Any]:
        logging.info(f"Executing command: {command}")
        print(f"\r[{datetime.now().strftime('%H:%M:%S')}] COMMAND: {command} - {Colors.BLUE}Running{Colors.ENDC}", end="")
        sys.stdout.flush()

        process = await asyncio.create_subprocess_shell(
            command,
            cwd=WORKSPACE_DIR,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        loading_task = asyncio.create_task(self.loading_animation())
        stdout, stderr = await process.communicate()
        loading_task.cancel()

        result = {
            "return_code": process.returncode,
            "stdout": stdout.decode(),
            "stderr": stderr.decode()
        }

        if process.returncode == 0:
            logging.info(f"Command executed successfully: {command}")
            print(f"\r[{datetime.now().strftime('%H:%M:%S')}] COMMAND: {command} - {Colors.BOLD}{Colors.GREEN}DONE{Colors.ENDC}")
        else:
            logging.error(f"Command failed: {command}")
            print(f"\r[{datetime.now().strftime('%H:%M:%S')}] COMMAND: {command} - {Colors.RED}Failed!{Colors.ENDC}")

        logging.info(f"Command output: {result}")
        return result
        
    async def loading_animation(self):
        dots = ['.', '..', '...']
        i = 0
        try:
            while True:
                print(f"\r[{datetime.now().strftime('%H:%M:%S')}] COMMAND: Running{Colors.BLUE}{dots[i]}{Colors.ENDC}", end="")
                sys.stdout.flush()
                await asyncio.sleep(0.5)
                i = (i + 1) % 3
        except asyncio.CancelledError:
            pass

    async def read_file(self, path: str) -> Dict[str, Any]:
        logging.info(f"Reading file: {path}")
        try:
            with open(path, 'r') as file:
                content = file.read()
            result = {"content": content}
            logging.info(f"File read successfully: {path}")
        except Exception as e:
            result = {"error": str(e)}
            logging.error(f"Error reading file {path}: {str(e)}")
        return result

    async def write_file(self, path: str, content: str) -> Dict[str, Any]:
        logging.info(f"Writing file: {path}")
        try:
            with open(path, 'w') as file:
                file.write(content)
            result = {"size": len(content)}
            logging.info(f"File written successfully: {path}")
        except Exception as e:
            result = {"error": str(e)}
            logging.error(f"Error writing file {path}: {str(e)}")
        return result

class KaioAgentClient:
    def __init__(self, url: str = API_URL):
        self.url = url
        self.session = KaioAgentSession(url)

    async def start_session(self):
        await self.session.connect()
        asyncio.create_task(self.session.process_messages())
        while True:
            await asyncio.sleep(1)