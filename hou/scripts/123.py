import hou

# Houdini Startup Script (123.py runs when Houdini starts)
print("="*50)
print("🚀 [OpenPipe] Initializing Houdini Environment...")
print("- OPENPIPE_ROOT: " + hou.getenv("OPENPIPE_ROOT", "Not Set"))
print("- Standard HOUDINI_PATH activated successfully.")
print("="*50)
