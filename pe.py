 
 
# from codex_python_sdk import create_client
# prompte = "Open chrome and open youtube on BMW M3 "
# with create_client() as client:
#     # Ask Codex to reply with a specific output
#     result = client.responses_create(prompt=prompte)
#     print(result.text) 
# git add . && git commit -m "update" && git push
import sys
from codex_python_sdk import create_client
# make sure to import right
# Get prompt from command line; default if none provided
prompte = sys.argv[1] if len(sys.argv) > 1 else "Open chrome"
print("Your code will be executed: " , prompte)

with create_client() as client:
    # Ask Codex to reply with a specific output
    result = client.responses_create(prompt=prompte)
    print(result.text)
