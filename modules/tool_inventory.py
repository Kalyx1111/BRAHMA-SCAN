import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXTRACTED_DIR = os.path.join(BASE_DIR, "extracted_tools")


# ==========================================
# LIST TOOLS
# ==========================================
def list_tools():

    if not os.path.exists(EXTRACTED_DIR):

        print("NO TOOLS DIRECTORY FOUND")
        return

    tools = os.listdir(EXTRACTED_DIR)

    if not tools:

        print("NO EXTRACTED TOOLS FOUND")
        return

    print("=" * 50)
    print("INSTALLED TOOLS")
    print("=" * 50)

    for tool in tools:

        print(f"- {tool}")


# ==========================================
# MAIN
# ==========================================
if __name__ == "__main__":

    list_tools()